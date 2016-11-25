#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pick import pick

def get_sound_directory_list():
    directories = [os.path.join(freelancer_path, x) for x in os.listdir(freelancer_path)]
    directories = [x for x in directories if os.path.isdir(x)]
    files = []
    for directory in directories:
        files += [os.path.join(directory, x) for x in os.listdir(directory) if x.endswith('files_to_submit')]
    return files

def get_sound_files_list(path):
    paths = [os.path.join(path,x) for x in os.listdir(path) if x.endswith('.mp3')]
    return paths

def rename_files(paths):
    for path in paths:
        directory = os.path.dirname(path)
        file = os.path.basename(path)
        file = file.lower()
        newpath = os.path.join(directory, file)
        os.rename(path, newpath)


if __name__ == "__main__":
    # 単語を抽出してくるファイルとエクスポート先のファイルを選択
    title                           = 'Please choose the csv file to inspect acceptance.'
    freelancer_path                 = 'freelancers'
    options                         = get_sound_directory_list()
    option, index                   = pick(options, title)

    sounds                          = get_sound_files_list(option)
    rename_files(sounds)
