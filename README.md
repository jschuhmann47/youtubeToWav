# Youtube to WAV

## About

This tool uses youtube-dl and ffmpeg to easily download a Youtube audio in WAV format.  

## Requisites

You'll need:

- Python
- youtube-dl module
- ffmpeg-python module

You can install both via pip:  

`pip install youtube-dl`

`pip install ffmpeg-python`

To download the program, clone it in the directory that you want:
`git clone https://github.com/jschuhmann47/youtubeToWav.git`

## Usage

Open your terminal and navigate to the location of the script. Then write
`python main.py`
and the program will start.

You'll be asked to insert a Youtube link. Paste it and press enter. The program will download and convert the video to `.m4a` and then to `.wav`. The `.wav` will be in the same folder with the name `output.wav`
