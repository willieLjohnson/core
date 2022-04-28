import string
import requests
from dataclasses import dataclass

response = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyDRiD0RkKyffuk6uptt_C5FCmYY-mxsKDM&channelId=UCiXhjiUOoJzPg3GVAc54YWg&part=snippet,id&order=date&maxResults=20')

json_response = response.json()
videos = json_response["items"]

@dataclass
class Video:
    videoId: string
    thumbnail: string
    title: string
    description: string
    

for video in videos:
    if "video" in video["id"]["kind"]:
        vid = Video(video["id"]["videoId"], video["snippet"]["thumbnails"]["high"]["url"], video["snippet"]["title"], video["snippet"]["description"])
        print(vid)