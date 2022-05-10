import youtube_dl
import os
import time
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
# google api key
apikey='AIzaSyANalyqf0T7iVWzs1x_BtJnR5ga8Oym1Kg'

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


def downloadPlaylist(url): 
    query = parse_qs(urlparse(url).query, keep_blank_values=True)
    playlist_id = query["list"][0]

    #print(f'get all playlist items links from {playlist_id}')
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = apikey)

    request = youtube.playlistItems().list(
        part = "snippet",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()

    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    print(f"total: {len(playlist_items)}")
    for t in playlist_items:
        vidurl =f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
        print(vidurl)
        downloadVideo(vidurl)
        time.sleep(3)

url = 'https://youtube.com/playlist?list=PLveUSFqkZWtOn2lswEoeO6-Dn43m-Zy-d'
downloadPlaylist(url)


