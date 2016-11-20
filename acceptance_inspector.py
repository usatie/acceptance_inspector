#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
from pick import pick


def get_words_list(path):
    list = pd.read_csv(path)
    return list[:num]

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
    invalidFiles = [x for x in os.listdir(sound_files_path) if x.endswith('.mp3') == False and x != '.DS_Store']
    return paths,invalidFiles

def inspect_sound_files(sound_files, directory_path, words, invalid_files):
    rgx             = '^(' + '|'.join(sound_files) + ')$'
    english_words   = list(words['english_label'])
    
    # 正しい名前でファイルが存在するかどうかをチェック
    words['isFileExists'] = words['english_label'].str.contains(rgx)
    
    # 違うフォーマットのファイルが存在するかどうかをチェック（wav, mp4以外の違うフォーマットがあれば追加する）
    invalid_files = [x.replace('.wav', '') for x in invalid_files]
    invalid_files = [x.replace('.mp4', '') for x in invalid_files]
    print(invalid_files)
    rgx_invalid     = '^(' + '|'.join(invalid_files) + ')$'
    words['isInvalidFormat'] = words['english_label'].str.contains(rgx_invalid)
    
    # csvに保存
    words.to_csv(os.path.join(directory_path, 'inspection_result.csv'))
    
    # リストに載っていない単語の音源が入っていれば見つける
    target_list     = list(words['english_label'])
    not_listed_files = [x for x in sound_files if x not in target_list]
    
    # フォーマット違いでもなく、単純に足りていないファイルがあれば見つける
    missing_words = words[(words['isFileExists'] == False) & (words['isInvalidFormat'] == False)]
    missing_files = list(missing_words['english_label'])
    
    return not_listed_files, missing_files


if __name__ == "__main__":
    # 単語を抽出してくるファイルとエクスポート先のファイルを選択
    title                           = 'Please choose the csv file to inspect acceptance.'
    freelancer_path                 = 'freelancers'
    options                         = get_csv_list()
    option, index                   = pick(options, title)
    
    print('How many words have been recorded? (value must be int)')
    num                             = int(input())
    words_list                      = get_words_list(option)
    sound_files, invalid_files      = get_sound_files_list(option)
    not_listed_files, missing_files = inspect_sound_files(sound_files,
                                                          os.path.dirname(option),
                                                          words_list,
                                                          invalid_files)

    if len(invalid_files) > 0:
        print('These files have invalid format : \n\t' + ',\n\t'.join(invalid_files))

    if len(not_listed_files) > 0:
        print('These files are not listed : \n\t' + ',\n\t'.join(not_listed_files))

    if len(missing_files) > 0:
        print('These files are missing : \n\t' + ',\n\t'.join(missing_files))

