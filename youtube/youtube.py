#!/user/bin/env python3
# -*- coding: utf-8 -*-

import time
import format_date
import youtube_channel_video_list
import youtube_video_download



def download_video(channel_url, local_file_path):
    print("[{0}] -------------begin parse video list-------------".format(format_date.get_current_time()))
    text = youtube_channel_video_list.get_html_text(channel_url)
    json_str = youtube_channel_video_list.get_yt_initial_data_json(text)
    video_list = youtube_channel_video_list.parse_yt_initial_data_json(json_str)
    index = 1
    for video_url in video_list:
        print("[{0}] {1}".format(index, video_url))
        index += 1
    print("[{0}] ------------- parse video list end -------------".format(format_date.get_current_time()))

    index = 1
    for video_url in video_list:
        print("[{0}] -------------begin download: {1}-------------".format(format_date.get_current_time(), index))
        youtube_video_download.download_video_without_exception(video_url, local_file_path)
        print("[{0}] ------------- download end: {1} -------------".format(format_date.get_current_time(), index))
        index += 1
        time.sleep(60 * 2)


if __name__ == '__main__':
    channel_url = "https://www.youtube.com/channel/UCr4ZqhqR6cGVSpxN59gLaZQ/videos"
    local_file_path = "F:\\vide_clip_downloads\\"

    print("[{0}] -------------start-------------".format(format_date.get_current_time()))
    download_video(channel_url, local_file_path)
    print("[{0}] ------------- end -------------".format(format_date.get_current_time()))
