import yt_dlp
import os
import customtkinter as ctk
from tkinter import messagebox
from tkinter import filedialog
import re
import platform

# Configurar o caminho do FFmpeg baseado no sistema operacional
if platform.system() == "Windows":
    FFMPEG_PATH = "C:/ffmpeg/bin/ffmpeg.exe"
    if os.path.exists(FFMPEG_PATH):
        os.environ["PATH"] = os.environ["PATH"] + os.pathsep + os.path.dirname(FFMPEG_PATH)
elif platform.system() == "Linux":
    # Para Termux/Linux
    FFMPEG_PATH = "/usr/bin/ffmpeg"
    if not os.path.exists(FFMPEG_PATH):
        FFMPEG_PATH = "/data/data/com.termux/files/usr/bin/ffmpeg"

def validar_url(url):
    padrao = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=|playlist\?list=)?([^&=%\?]{11}|[^&=%\?]{34})'
    return bool(re.match(padrao, url))

def eh_playlist(url):
    return 'playlist?list=' in url

def obter_formatos_disponiveis(url):
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'ffmpeg_location': os.path.dirname(FFMPEG_PATH) if os.path.exists(FFMPEG_PATH) else None
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if eh_playlist(url):
                return []  # Não mostrar formatos para playlist
            formatos = []
            for formato in info.get('formats', []):
                if formato.get('ext') in ['mp4', 'webm'] and formato.get('vcodec') != 'none':
                    descricao = f"{formato.get('height', 'N/A')}p ({formato['ext']}) - {formato.get('vcodec', 'N/A')}"
                    formatos.append({
                        'format_id': formato['format_id'],
                        'descricao': descricao
                    })
            return formatos
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao obter formatos: {e}")
        return []

def baixar_video(url, destino=".", formato_id=None, apenas_audio=False):
    try:
        if not validar_url(url):
            messagebox.showerror("Erro", "URL inválida!")
            return

        ydl_opts = {
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
            'ffmpeg_location': os.path.dirname(FFMPEG_PATH) if os.path.exists(FFMPEG_PATH) else None,
            'merge_output_format': 'mp4',
            'prefer_ffmpeg': True,
            'postprocessors': [],
            'noplaylist': not eh_playlist(url),  # Permitir playlist se a URL for de playlist
        }

        if apenas_audio:
            ydl_opts.update({
                'format': 'bestaudio',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        elif formato_id and not eh_playlist(url):
            ydl_opts['format'] = f"{formato_id}+bestaudio[ext=m4a]/best"
            ydl_opts['postprocessors'].append({
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            })
        else:
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            ydl_opts['postprocessors'].append({
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            })

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if eh_playlist(url):
                info = ydl.extract_info(url, download=False)
                total_videos = len(info['entries'])
                messagebox.showinfo("Playlist", f"Iniciando download de {total_videos} vídeos...")
            ydl.download([url])

        messagebox.showinfo("Sucesso", "Download concluído!")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {e}")

def atualizar_formatos():
    url = url_entry.get()
    if url and validar_url(url):
        if eh_playlist(url):
            formato_menu.configure(state="disabled")
            formato_menu.set("Playlist - Formato Automático")
        else:
            formato_menu.configure(state="normal")
            formatos = obter_formatos_disponiveis(url)
            global formato_ids
            formato_ids = [f['format_id'] for f in formatos]
            formato_menu.configure(values=[f['descricao'] for f in formatos])
            if formatos:
                formato_menu.set(formatos[0]['descricao'])
    else:
        formato_menu.configure(values=[])
        formato_menu.set("")

def escolher_diretorio():
    diretorio = filedialog.askdirectory(title="Escolha o diretório de destino")
    if diretorio:
        destino_entry.delete(0, ctk.END)
        destino_entry.insert(0, diretorio)

def on_download_button_click():
    url_video = url_entry.get()
    if url_video:
        destino = destino_entry.get()
        if not destino:
            destino = default_directory
        
        formato_id = None
        if not apenas_audio_var.get():
            # Obter o índice do formato selecionado
            formato_selecionado = formato_menu.get()
            try:
                indice = [f['descricao'] for f in obter_formatos_disponiveis(url_video)].index(formato_selecionado)
                formato_id = formato_ids[indice]
            except (ValueError, IndexError):
                formato_id = None

        baixar_video(url_video, destino, formato_id, apenas_audio_var.get())
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL.")

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Definir o diretório padrão baseado no sistema operacional
if platform.system() == "Windows":
    default_directory = os.path.join(os.path.expanduser("~"), "Downloads")
else:
    default_directory = os.path.expanduser("~/Downloads")

# Configuração da janela principal
root = ctk.CTk()
root.title("Downloader de Vídeos do YouTube")
root.geometry("700x400")

# Configuração do layout
url_label = ctk.CTkLabel(root, text="Digite a URL do vídeo do YouTube:")
url_label.grid(row=0, column=0, pady=10, padx=10)

url_entry = ctk.CTkEntry(root, width=400)
url_entry.grid(row=0, column=1, pady=10, padx=10)
url_entry.bind('<KeyRelease>', lambda e: atualizar_formatos())

destino_label = ctk.CTkLabel(root, text="Selecione o diretório de destino:")
destino_label.grid(row=1, column=0, pady=10, padx=10)

destino_frame = ctk.CTkFrame(root)
destino_frame.grid(row=1, column=1, pady=10, padx=10)

destino_entry = ctk.CTkEntry(destino_frame, width=300)
destino_entry.grid(row=0, column=0, padx=5)
destino_entry.insert(0, default_directory)

destino_button = ctk.CTkButton(destino_frame, text="Escolher", command=escolher_diretorio)
destino_button.grid(row=0, column=1, padx=5)

# Frame para opções de download
opcoes_frame = ctk.CTkFrame(root)
opcoes_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

formato_label = ctk.CTkLabel(opcoes_frame, text="Qualidade do vídeo:")
formato_label.grid(row=0, column=0, padx=5)

formato_var = ctk.StringVar()
formato_menu = ctk.CTkOptionMenu(opcoes_frame, variable=formato_var, values=[])
formato_menu.grid(row=0, column=1, padx=5)

apenas_audio_var = ctk.BooleanVar()
apenas_audio_check = ctk.CTkCheckBox(opcoes_frame, text="Apenas Áudio (MP3)", variable=apenas_audio_var)
apenas_audio_check.grid(row=0, column=2, padx=5)

download_button = ctk.CTkButton(root, text="Baixar Vídeo", command=on_download_button_click)
download_button.grid(row=3, column=0, columnspan=2, pady=20)

# Iniciar o loop da interface gráfica
formato_ids = []  # Lista global para armazenar os format_ids
root.mainloop()
