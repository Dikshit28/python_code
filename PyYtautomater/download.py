import urllib.request
from datetime import date

def downloader(video_urls,usernames):
    # Returns the current local date
    today = date.today()
    folder_path = "./reels-"+str(today)+"/"
    for i in range(len(video_urls)):
        print("Downloading "+usernames[i])
        urllib.request.urlretrieve(video_urls[i],folder_path+usernames[i]+".mp4")