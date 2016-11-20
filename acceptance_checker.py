#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
from pick import pick


def get_words_list(path):
    list = pd.read_csv(path)
    return list

def get_csv_list():
    directories = [os.path.join(freelancer_path, x) for x in os.listdir(freelancer_path)]
    directories = [x for x in directories if os.path.isdir(x)]
    files = []
    for directory in directories:
        files += [os.path.join(directory, x) for x in os.listdir(directory) if x.endswith('.csv')]
    return files

def get_sound_files_list(path):
    dir_path = os.path.dirname(path)
    sound_files_path = os.path.join(dir_path, 'files_to_submit')
    paths = [x.replace('.mp3', '') for x in os.listdir(sound_files_path) if x.endswith('.mp3')]
    return paths

def inspect_sound_files(sound_files, directory_path):
    rgx = '^(' + '|'.join(sound_files) + ')$'
    print(rgx)
    list['isFileExists'] = list['english_label'].str.contains(rgx)
    list.to_csv(os.path.join(directory_path, 'inspection_result.csv'))

if __name__ == "__main__":
    # 単語を抽出してくるファイルとエクスポート先のファイルを選択
    title = 'Please choose the csv file to inspect acceptance.'
    freelancer_path = 'freelancers'
    options         = get_csv_list()
    option, index   = pick(options, title)
    list            = get_words_list(option)
    sound_files     = get_sound_files_list(option)
    inspect_sound_files(sound_files, os.path.dirname(option))
