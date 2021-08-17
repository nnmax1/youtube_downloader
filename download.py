import youtube_dl
import os

def downloadVideo(url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    with ydl:
        result = ydl.extract_info(
            url, 
            download=True 
        )
    files = []
    # if playlist
    if 'entries' in result:
        for video in result['entries']:
            # rename files
            filename= str(video['title'])+".mp4"
            files.append(filename)
            os.rename(str(video['id'])+".mp4",filename)
    # if 1 video
    else:
        # Just a video
        video = result
        # rename each file
        filename= str(video['title'])+".mp4" 
        files.append(filename)
        os.rename(str(video['id'])+".mp4",filename)
    return files

