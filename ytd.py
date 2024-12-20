import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def baixar_video(url, destino="."):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),  # Diretório de saída
            'format': 'bestvideo[height<=1080]+bestaudio/best',  # Forçar baixar o melhor vídeo até 1080p e o melhor áudio
            'noplaylist': False,  # Evitar baixar playlists
            'ffmpeg_location': r'C:\ffmpeg\bin\ffmpeg.exe',  # Caminho para o FFmpeg (ajuste conforme necessário)
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Sucesso", "Download concluído!")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {e}")

# Função chamada ao clicar no botão de download
def on_download_button_click():
    url_video = url_entry.get()
    if url_video:
        destino = destino_entry.get()
        if not destino:
            destino = default_directory  # Se não houver diretório selecionado, usa o diretório do script
        baixar_video(url_video, destino)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL.")

# Função para selecionar o diretório de destino
def escolher_diretorio():
    diretorio = filedialog.askdirectory(title="Escolha o diretório de destino")
    if diretorio:
        destino_entry.delete(0, tk.END)
        destino_entry.insert(0, diretorio)

# Definir o diretório padrão como o diretório onde o arquivo está
default_directory = os.path.dirname(os.path.realpath(__file__))

# Configuração da janela principal do Tkinter
root = tk.Tk()
root.title("Downloader de Vídeos do YouTube")

# Configuração do layout
url_label = tk.Label(root, text="Digite a URL do vídeo do YouTube:")
url_label.grid(row=0, column=0, pady=10, padx=10)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, pady=10, padx=10)

destino_label = tk.Label(root, text="Selecione o diretório de destino:")
destino_label.grid(row=1, column=0, pady=10, padx=10)

# Frame para organizar a entrada de diretório e o botão
destino_frame = tk.Frame(root)
destino_frame.grid(row=1, column=1, pady=10, padx=10)

destino_entry = tk.Entry(destino_frame, width=40)
destino_entry.grid(row=0, column=0, padx=5)

# Preencher o campo de diretório com o diretório onde o arquivo está
destino_entry.insert(0, default_directory)

destino_button = tk.Button(destino_frame, text="Escolher", command=escolher_diretorio)
destino_button.grid(row=0, column=1, padx=5)

download_button = tk.Button(root, text="Baixar Vídeo", command=on_download_button_click)
download_button.grid(row=2, column=0, columnspan=2, pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
