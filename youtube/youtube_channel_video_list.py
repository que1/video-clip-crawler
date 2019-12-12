#!/user/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json


def get_html_text(url):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'http://www.google.com.hk/'
    }
    response = requests.get(url, headers=headers)
    bs_obj = BeautifulSoup(response.content, "html5lib")
    script_list = bs_obj.findAll("script")

    need_obj = None
    for script in script_list:
        if script.get_text().find("gridVideoRenderer") >= 0:
            need_obj = script
            break
        else:
            continue

    if need_obj is None:
        print("error: get html none")
        return None

    js_code = str(need_obj.get_text())
    return js_code


def get_yt_initial_data_json(js_code):
    if js_code is None:
        return None

    lines = js_code.split("window[\"ytInitialPlayerResponse")

    if len(lines) <= 1:
        print("error: initial data - " + js_code)
        return None

    line = lines[0]
    init_data = line.replace("window[\"ytInitialData\"] = ", "").replace(";", "").strip()
    return init_data


def parse_yt_initial_data_json(init_data):
    if init_data is None:
        print("error：initial data is none")
        return None

    json_obj = json.loads(init_data)
    if json_obj is None:
        print("error: parse init data json error")
        return None

    tab_renderer_list = None
    if 'contents' in json_obj.keys():
        contents = json_obj['contents']
        if 'twoColumnBrowseResultsRenderer' in contents.keys():
            two_column_browse_results_renderer = contents['twoColumnBrowseResultsRenderer']
            if 'tabs' in two_column_browse_results_renderer.keys():
                tab_renderer_list = two_column_browse_results_renderer['tabs']

    if (tab_renderer_list is None) or (len(tab_renderer_list) == 0):
        print("error: contents-tabRenderer_list-tabs none, json - " + init_data)
        return None

    return parse_tab_renderer_data_json(tab_renderer_list)



def parse_tab_renderer_data_json(tab_renderer_list):
    if tab_renderer_list is None:
        return None

    video_list = list()
    for tabRenderer in tab_renderer_list:
        if 'tabRenderer' not in tabRenderer.keys():
            continue
        tab = tabRenderer['tabRenderer']
        if 'selected' not in tab.keys():
            continue
        if tab['selected'] is True:
            content = tab['content']
            section_list_renderer = content['sectionListRenderer']
            section_contents =  section_list_renderer['contents']
            item_section_renderer = section_contents[0]['itemSectionRenderer']
            item_contents = item_section_renderer['contents']
            grid_renderer = item_contents[0]['gridRenderer']
            items = grid_renderer["items"]
            for item in items:
                grid_video_renderer = item['gridVideoRenderer']
                video_id = grid_video_renderer["videoId"]
                video_list.append("https://www.youtube.com/watch?v=" + video_id)

    return video_list





if __name__ == '__main__':
    channel_url = "https://www.youtube.com/user/BobaTurbo/videos"

    text = get_html_text(channel_url)
    json_str = get_yt_initial_data_json(text)
    video_list = parse_yt_initial_data_json(json_str)
    index = 1
    for video_url in video_list:
        print("[{0}] {1}".format(index, video_url))
        index += 1