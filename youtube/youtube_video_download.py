#!/usr/bin/env python3
# -*- coding: utf8 -*-

from pytube import YouTube
import format_date

def download_video(url, local_file_path):
    yt = YouTube(url)
    stream = yt.streams.first()

    player_config_args = yt.player_config_args
    author = player_config_args['player_response']['videoDetails']['author']
    video_id = player_config_args['player_response']['videoDetails']['videoId']  #yt.video_id
    watch_url = yt.watch_url
    title = player_config_args['player_response']['videoDetails']['title']       #yt.title
    filename_prefix = author + " -- "

    print("[{0}] author: {1}".format(format_date.get_current_time(), author))
    print("[{0}] video_id: {1}".format(format_date.get_current_time(), video_id))
    print("[{0}] watch_url: {1}".format(format_date.get_current_time(), watch_url))
    print("[{0}] title: {1}".format(format_date.get_current_time(), title))
    print("[{0}] download_url: {1}".format(format_date.get_current_time(), stream.url))
    print("[{0}] local_file_path: {1}{2}{3}.mp4".format(format_date.get_current_time(), local_file_path, filename_prefix, title))
    stream.download(output_path=local_file_path, filename_prefix=filename_prefix)


def download_video_without_exception(url, local_file_path):
    try:
        download_video(url, local_file_path)
    except Exception:
        print("error: download url " + url)



if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=1o0eRERjUNY"
    local_file_path = "/Users/q/doc/video_clip/"
    print("-------------begin-------------")
    download_video_without_exception(url, local_file_path)
    print("------------- end -------------")