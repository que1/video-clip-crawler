#!/usr/bin/env python3
# -*- coding: utf8 -*-

from pytube import YouTube
import format_date
import traceback

def download_video(url, local_file_path):
    yt = YouTube(url)
    stream = yt.streams.first()

    player_config_args = yt.player_config_args
    author = player_config_args['player_response']['videoDetails']['author']
    video_id = player_config_args['player_response']['videoDetails']['videoId']  #yt.video_id
    watch_url = yt.watch_url
    title = player_config_args['player_response']['videoDetails']['title']       #yt.title
    filename_prefix = author + " -- "

    try:
        print("[{0}] author: {1}".format(format_date.get_current_time(), author))
        print("[{0}] video_id: {1}".format(format_date.get_current_time(), video_id))
        print("[{0}] watch_url: {1}".format(format_date.get_current_time(), watch_url))
        print("[{0}] title: {1}".format(format_date.get_current_time(), title))
        print("[{0}] download_url: {1}".format(format_date.get_current_time(), stream.url))
        print("[{0}] local_file_path: {1}{2}{3}.mp4".format(format_date.get_current_time(), local_file_path, filename_prefix, title))
    except Exception:
        print("error: " + traceback.format_exc())
    stream.download(output_path=local_file_path, filename_prefix=filename_prefix)


def download_video_without_exception(url, local_file_path):
    try:
        download_video(url, local_file_path)
    except Exception:
        print("error: " + traceback.format_exc())



if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=H7LjyMhuvSk"
    local_file_path = "F:\\vide_clip_downloads\\"
    print("-------------begin-------------")
    download_video_without_exception(url, local_file_path)
    print("------------- end -------------")