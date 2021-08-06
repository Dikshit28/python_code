from moviepy.editor import VideoFileClip, concatenate_videoclips

def combine(folder_path, video_list, output_name):
    clips = [VideoFileClip(folder_path+video+".mp4") for video in video_list]
    final=concatenate_videoclips(clips)
    final.write_videofile(f"./final/{output_name}.mp4")