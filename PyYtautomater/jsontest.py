import json

#open demo2.txt file and read data
with open('demo2.txt', 'r') as f:
    data = f.read()

json_data=json.loads(data)
video_url=json_data['graphql']['shortcode_media']['video_url']
username=json_data['graphql']['shortcode_media']['owner']['username']

print(video_url,username)