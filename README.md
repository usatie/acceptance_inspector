# acceptance_inspector

0. フォルダ構成について
Dave AllenさんとVincent Brasherさんがしてくれている録音場合は以下のような構成にしてください。
単語リストは`./freelancers/freelancer_name/`にcsvファイルで保存すること、
提出されたmp3ファイルは全て、`./freelancers/freelancer_name/files_to_submit/`にすることが必要です。
```
acceptance_inspector/
　├ freelancers/
　│　├ Dave Allen/
　│　│　├ list.csv
　│　│　└ files_to_submit/
　│　│　   ├ devastating.mp3
　│　│　   ├ refigirator.mp3
　│　│　   └ pronunciation.mp3
　│　│
　│　└ Vincent Brasher/
　│　 　├ list.csv
　│　 　└ files_to_submit/
　│　 　   ├ devastating.mp3
　│　 　   ├ refigirator.mp3
　│　 　   └ pronunciation.mp3
　│
　├acceptance_inspector.py
　└etc...
```

1. まずはpythonファイルを実行し、誰のファイルを検収するのか選んでください。
```
 $ python acceptance_inspector.py
```
![](https://github.com/usatie/acceptance_inspector/blob/master/Assets/select_file.png)

2. 何単語すでに録音されているのか、入力してください。
![](https://github.com/usatie/acceptance_inspector/blob/master/Assets/set_num.png)

3. 実行結果では、「リスト内に存在しないのにあるファイル」「リストにあるのに、見つからないファイル」「違うフォーマットで保存されているファイル」が表示されます。
表示された場合は明らかにミスなので、ファイル名の修正や追加が必要になります。
例えば、結果が出た時こんな結果が出た時はスペルミスをしていたことがすぐにわかります。
![](https://github.com/usatie/acceptance_inspector/blob/master/Assets/result.png)
