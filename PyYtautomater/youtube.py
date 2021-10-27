#Youtube video uploader via google data api
import datetime
from Google import Create_Service,convert_to_RFC_datetime
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

upload_date_time = datetime.datetime(2021, 9, 15, 12, 30, 0).isoformat('T')
def create_body(title, description):
    request_body = {
        'snippet': {
            'categoryId': 19,
            'title': title,
            'description': description,
            'tags': ['test'],
        },
        'status': {
            'privacyStatus': 'unlisted',
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False
    }
    return request_body

def upload_video(request_body,video_file,thumbnail_file):
    mediafile = MediaFileUpload(f"./final/{video_file}.mp4")
    try:
        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediafile
        ).execute()
    except Exception as e:
        print(e)
        return None
    try:
        service.thumbnails().set(
            videoId=response_upload.get('id'),
            media_body=MediaFileUpload(f"./final/{thumbnail_file}.jpg")
        ).execute()
    except Exception as e:
        print(e)
        return None

    return response_upload

request_body=create_body('test','test')
response_upload=upload_video(request_body,'file1','file1')

#TASK CREATED WAITING FOR PRIVATE LOCKED TO BE SOLVED AND THEN MAKE IT A CRON JOB THAT RUNS EVERY 24 HOURS
