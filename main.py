from __future__ import unicode_literals
import youtube_dl
import ffmpeg



ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'output.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
    #'logger': logger(),
    #'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    url=input("Enter Youtube URL: ")
    ydl.download([url])
    stream = ffmpeg.input('output.m4a')
    stream = ffmpeg.output(stream, 'output.wav')

#a