Aqui está o README.md completo em formato Markdown:

# YouTube Video Downloader 🎥💻

Este projeto é uma ferramenta para baixar vídeos do YouTube utilizando a biblioteca `yt-dlp` e uma interface gráfica feita com `Tkinter` em Python. A interface permite que o usuário insira a URL do vídeo e escolha o diretório de destino para salvar o arquivo. Durante o download, a ferramenta exibe o tempo estimado restante. ⏳

## Funcionalidades ✨

- Baixar vídeos do YouTube em alta qualidade (até 1080p). 🔝
- Interface gráfica simples com `Tkinter`. 🖥️
- Escolher o diretório de destino para salvar o vídeo. 📂
- Exibição do tempo estimado de download. ⏱️

## Ferramentas Usadas 🛠️

- **yt-dlp**: Biblioteca Python para baixar vídeos do YouTube e outros sites. 📥
- **Tkinter**: Biblioteca padrão do Python para criar interfaces gráficas. 🎨
- **FFmpeg**: Utilizado pelo `yt-dlp` para manipulação de áudio e vídeo, caso necessário. 🎬

## Como Rodar 🚀

### 1. Pré-requisitos 📋

Certifique-se de que você tem o Python 3 instalado em sua máquina. Para verificar, abra o terminal e execute:

```bash
python --version

2. Instalar Dependências 📦

Instale as bibliotecas necessárias usando pip. Abra o terminal e execute o seguinte comando:

pip install yt-dlp

3. Instalar o FFmpeg 🎞️

O yt-dlp pode precisar do FFmpeg para baixar vídeos com áudio e vídeo em alta qualidade. Você pode fazer o download do FFmpeg no site oficial ou, se estiver usando um sistema baseado em Linux, pode instalá-lo com o seguinte comando:

Para Ubuntu/Debian:

sudo apt update
sudo apt install ffmpeg

Para Windows:

Baixe o FFmpeg do site oficial.

Extraia o conteúdo do arquivo ZIP em uma pasta de sua escolha.

Adicione o caminho para o executável do FFmpeg (por exemplo, C:\ffmpeg\bin\ffmpeg.exe) nas variáveis de ambiente do sistema.


4. Rodar o Script ▶️

Após as dependências estarem instaladas, você pode rodar o script Python. Abra o terminal e navegue até o diretório onde o arquivo Python (downloader.py) está localizado. Em seguida, execute:

python downloader.py

Isso abrirá a interface gráfica do Tkinter, onde você poderá inserir a URL do vídeo do YouTube e escolher o diretório de destino para o download.

5. Como Usar 📝

Digite a URL do vídeo do YouTube no campo fornecido. 🌐

Escolha o diretório de destino onde o vídeo será salvo. Se não escolher, o vídeo será salvo no mesmo diretório onde o script está. 📁

Clique no botão "Baixar Vídeo" para iniciar o download. ⬇️

Durante o download, o tempo estimado será mostrado na interface. ⏳


6. Usando no Termux 📱

Se você deseja executar este projeto em um dispositivo Android utilizando o Termux, siga as etapas abaixo para configurá-lo corretamente:

6.1 Instale o Termux

Baixe o Termux da Google Play Store ou do F-Droid.

6.2 Atualize e Instale Dependências

Abra o Termux e atualize os pacotes com os comandos:

pkg update && pkg upgrade
pkg install python ffmpeg git

6.3 Instale a Biblioteca yt-dlp

Use o pip para instalar a biblioteca yt-dlp:

pip install yt-dlp

6.4 Clone o Repositório

Baixe o projeto para o Termux usando o comando git clone:

git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio

6.5 Execute o Script

Execute o script Python diretamente no Termux com o seguinte comando:

python downloader.py

6.6 Observação

O Termux não possui uma interface gráfica nativa, então a interface Tkinter não será exibida. Se necessário, modifique o script para funcionar apenas no modo CLI (linha de comando).

Para utilizar um diretório específico como destino, modifique o parâmetro destino diretamente no script ou passe argumentos na linha de comando.


Por exemplo, altere diretamente no script:

destino = "/sdcard/Downloads"

Ou, se preferir, ajuste o script para aceitar argumentos via linha de comando.

Problemas Comuns no Termux ⚠️

1. Erro ao encontrar o FFmpeg: Certifique-se de que o FFmpeg está instalado no Termux (pkg install ffmpeg).


2. Permissões negadas: Garanta que o Termux tenha permissão para acessar o armazenamento:
```bash
termux-setup-storage```



Agora você pode utilizar o projeto diretamente no Termux para baixar vídeos do YouTube no seu dispositivo Android! 🎉

Licença 🛡️

Este projeto é licenciado sob a Apache License. 📝
