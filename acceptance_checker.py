#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
from pick import pick


def get_words_list(path):
    list = pd.read_csv(path, header=None)
    print(list)
#    words = []
#    with open(path, 'r') as f:
#        reader = csv.reader(f)
#        header = next(reader) # ヘッダー行をスキップする
#        for row in reader:
#            words += [x for x in row if x != '' and x != '']
    return list


if __name__ == "__main__":
    # 単語を抽出してくるファイルとエクスポート先のファイルを選択
    title = 'Please choose the csv file to extract words from.'
    freelancer_path = 'freelancers'
    
    directories = [os.path.join(freelancer_path, x) for x in os.listdir(freelancer_path)]
    directories = [x for x in directories if os.path.isdir(x)]
    print(directories)
    files = []
    for directory in directories:
        files += [os.path.join(directory, x) for x in os.listdir(directory) if x.endswith('.csv')]
    options     = files
    option, index = pick(options, title)
    words = get_words_list(option)
    print(words)
