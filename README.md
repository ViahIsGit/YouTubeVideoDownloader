
# YouTube Video Downloader 🎥💻

Este projeto é uma ferramenta para baixar vídeos do YouTube utilizando a biblioteca `yt-dlp` e uma interface gráfica feita com `Tkinter` em Python. A interface permite que o usuário insira a URL do vídeo e escolha o diretório de destino para salvar o arquivo. Durante o download, a ferramenta exibe o tempo estimado restante. ⏳

## Funcionalidades ✨

- Baixar vídeos do YouTube em alta qualidade (até 1080p). 🔝
- Interface gráfica simples com `Tkinter`. 🖥️
- Escolher o diretório de destino para salvar o vídeo. 📂

## Ferramentas Usadas 🛠️

- **yt-dlp**: Biblioteca Python para baixar vídeos do YouTube e outros sites. 📥
- **Tkinter**: Biblioteca padrão do Python para criar interfaces gráficas. 🎨
- **FFmpeg**: Utilizado pelo `yt-dlp` para manipulação de áudio e vídeo, caso necessário. 🎬

## Como Rodar 🚀

### 1. Pré-requisitos 📋

Certifique-se de que você tem o Python 3 instalado em sua máquina. Para verificar, abra o terminal e execute:

```bash
python --version
```

### 2. Instalar Dependências 📦

Instale as bibliotecas necessárias usando `pip`. Abra o terminal e execute o seguinte comando:

```bash
pip install yt-dlp
```

### 3. Instalar o FFmpeg 🎞️

O `yt-dlp` pode precisar do FFmpeg para baixar vídeos com áudio e vídeo em alta qualidade. Você pode fazer o download do FFmpeg no [site oficial](https://ffmpeg.org/download.html) ou, se estiver usando um sistema baseado em Linux, pode instalá-lo com o seguinte comando:

**Para Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install ffmpeg
```

**Para Windows:**

- Baixe o FFmpeg do [site oficial](https://ffmpeg.org/download.html).
- Extraia o conteúdo do arquivo ZIP em uma pasta de sua escolha.
- Adicione o caminho para o executável do FFmpeg (por exemplo, `C:\ffmpeg\bin\ffmpeg.exe`) nas variáveis de ambiente do sistema.

**Para Android:**

Baixe um aplicativo que suporte o FFmpeg, como o Termux.

Abra o Termux e execute os comandos abaixo para instalar o FFmpeg:
```bash
pkg update && pkg upgrade  
pkg install ffmpeg```

Após a instalação, você pode usar o FFmpeg diretamente no Termux para processar arquivos multimídia.


Se necessário, forneça permissões de acesso a arquivos para que o Termux possa acessar seus vídeos ou áudios no dispositivo.


### 4. Rodar o Script ▶️

Após as dependências estarem instaladas, você pode rodar o script Python. Abra o terminal e navegue até o diretório onde o arquivo Python ([YTD.py](ytd.py)) está localizado. Em seguida, execute:

```bash
python ytd.py
```

Isso abrirá a interface gráfica do Tkinter, onde você poderá inserir a URL do vídeo do YouTube e escolher o diretório de destino para o download.

### 5. Como Usar 📝

- **Digite a URL do vídeo do YouTube** no campo fornecido. 🌐
- **Escolha o diretório de destino** onde o vídeo será salvo. Se não escolher, o vídeo será salvo no mesmo diretório onde o script está. 📁
- Clique no botão **"Baixar Vídeo"** para iniciar o download. ⬇️
- Durante o download, o **tempo estimado** será mostrado na interface. ⏳

## Licença 🛡️

Este projeto é licenciado sob a [Apache](LICENSE). 📝
