# Youtube to WAV

## About

This tool uses youtube-dl and ffmpeg to easily download a Youtube audio in WAV format.  

## Requisites

You'll need:

- Python
- ffmpeg
- yt-dlp module
- ffmpeg-python module

On Linux you can download python and ffmpeg from your package manager.

On Windows:
- [Python link](https://www.python.org/downloads/)
- [ffmpeg link](https://ffmpeg.org/download.html)

You should also add `ffmpeg` to the PATH. [Here is a guide](https://github.com/ytdl-org/youtube-dl#on-windows-how-should-i-set-up-ffmpeg-and-youtube-dl-where-should-i-put-the-exe-files)

For the modules you can install both via pip (both OS):  

`pip install yt-dlp`

`pip install ffmpeg-python`

To download the program, clone it in the directory that you want:

`git clone https://github.com/jschuhmann47/youtubeToWav.git`

## Usage

Open your terminal and navigate to the location of the script. Then write
`python youtubetowav.py`
and the program will start.

You'll be asked to insert a Youtube link. Paste it and press enter. The program will download and convert the video to `.m4a` and then to `.wav`. The `.wav` will be in the same folder with the filename being the title of the video plus its ID.

For example, this URL: `https://www.youtube.com/watch?v=sO4vI8P88NM`

will output `Thriller [sO4vI8P88NM].wav`

Optionally you can pass the URL directly as a main argument.

For example:
`python youtubetowav.py https://www.youtube.com/watch?v=SDk1RA4g8CA`
