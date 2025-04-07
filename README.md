# YouTube Video Downloader

Um aplicativo simples para baixar vídeos e playlists do YouTube, com interface gráfica para Windows e suporte a linha de comando para Android (Termux).

## Características

- Interface gráfica amigável (Windows)
- Suporte a download de vídeos individuais e playlists
- Opção de download apenas do áudio (MP3)
- Seleção de qualidade de vídeo
- Compatível com Windows e Android (Termux)

## Requisitos

### Para Windows:

1. Python 3.7 ou superior
2. FFmpeg

#### Instalação no Windows:

1. Instale o Python do [site oficial](https://www.python.org/downloads/)

2. Instale o FFmpeg:
   - Baixe o FFmpeg do [site oficial](https://ffmpeg.org/download.html)
   - Extraia os arquivos para `C:/ffmpeg/`
   - O executável deve estar em `C:/ffmpeg/bin/ffmpeg.exe`

3. Instale as dependências:
```bash
pip install yt-dlp customtkinter
```

### Para Android (Termux):

1. Instale o Termux da [F-Droid](https://f-droid.org/packages/com.termux/)

2. No Termux, execute:
```bash
pkg update && pkg upgrade
pkg install python ffmpeg
pip install yt-dlp
```

## Como Usar

### No Windows:

1. Execute o programa:
```bash
python ytd.py
```

2. Cole a URL do vídeo ou playlist do YouTube
3. Escolha o diretório de destino (opcional)
4. Selecione a qualidade do vídeo (não disponível para playlists)
5. Marque "Apenas Áudio" se quiser baixar só o áudio
6. Clique em "Baixar Vídeo"

### No Android (Termux):

1. Execute o programa:
```bash
python ytd.py
```

## Solução de Problemas

### Windows:
- Se o FFmpeg não for encontrado, verifique se está instalado em `C:/ffmpeg/bin/`
- Se houver erro de módulos não encontrados, execute: `pip install -r requirements.txt`

### Android/Termux:
- Se houver erro de permissão, execute: `termux-setup-storage`
- Se o FFmpeg não for encontrado, reinstale com: `pkg reinstall ffmpeg`

## Notas

- Para playlists, a qualidade é automaticamente definida como a melhor disponível
- O download de playlists pode levar mais tempo
- Os arquivos são salvos com o título original do vídeo

## Licença

Este projeto é distribuído sob a licença Apache.
