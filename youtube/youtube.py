#!/user/bin/env python3
# -*- coding: utf-8 -*-


import time
import datetime
import youtube_channel_video_list
import youtube_video_download


def download_video(channel_url, local_file_path):
    print("[{0}] -------------begin parse video list-------------".format(get_current_time()))
    text = youtube_channel_video_list.get_html_text(channel_url)
    json_str = youtube_channel_video_list.get_yt_initial_data_json(text)
    video_list = youtube_channel_video_list.parse_yt_initial_data_json(json_str)
    index = 1
    for video_url in video_list:
        print("[{0}] {1}".format(index, video_url))
        index += 1
    print("[{1}] ------------- parse video list end -------------".format(get_current_time()))

    index = 1
    for video_url in video_list:
        print("[{0}] -------------begin download: {1}-------------".format(get_current_time(), index))
        youtube_video_download.download_video(video_url, local_file_path)
        print("[{0}] ------------- download end: {1} -------------".format(get_current_time(), index))
        index += 1
        time.sleep(60 * 3)


def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


if __name__ == '__main__':
    channel_url = "https://www.youtube.com/channel/UC3rfj7rzQS5w9EmXHqT5sKQ/videos"
    local_file_path = "/Users/q/doc/video_clip/"

    print("[{0}] -------------start-------------".format(get_current_time()))
    download_video(channel_url, local_file_path)
    print("[{0}] ------------- end -------------".format(get_current_time()))
