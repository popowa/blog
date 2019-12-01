Title: 2017年のAWSリリース一覧
Date: 2017-12-16 10:45
Tags: AWS
Slug: 2017/12/2017-aws-release
Authors: ayakomuro
Summary: 2017年のAWSリリース一覧を自分用に図にまとめてみた方法とその結果👀

## 動機
[九州インフラ交流勉強会(Kixs) Vol.006](https://kixs.connpass.com/event/69643/)で発表資料作成する為に色々調べたりまとめて見ました。


## 情報収集はpythonに任せた

まずリリースはここで詳細を見ることが可能

- [2017 年（日本語)](https://aws.amazon.com/jp/about-aws/whats-new/2017/)
- [2017(英語)](https://aws.amazon.com/about-aws/whats-new/2017/)

日本語のページは4月以前のリストが表示されていないので全部みたいなら英語ページしかない。

まずはタグクラウドみたいに単語を出せたらいいな、と思い、調べたら簡単に出来そうだったので、すぐに作成する事が出来た。

- [blog/graph-wordcloud.py](https://github.com/popowa/blog/blob/master/code/aws-release/graph-wordcloud.py)

（Githubのコンテンツをembedする方法が分からない・・・）

その後より分かりやすく形態素解析からの文字出現率計算してグラフにしようと以下を試した。

- [Janome](http://mocobeta.github.io/janome/): 英語対応してないことに2時間ぐらいやって気づいたのは痛い
- [polyglot](http://polyglot.readthedocs.io/en/latest/index.html): AWSの製品名って汎用的な単語を使っている事が多く、正しく名詞、固有名詞として取り出せない事がまたもや判明！
- [Matplotlib: Python plotting](https://matplotlib.org/)：簡単にグラフ化出来た。これすごい。これからこのツール触っていきたい

もしかしたら[neologd](https://github.com/neologd)みたいに自分で辞書を追加すればよかったかもしれないけど、とりあえずは公式の製品一覧を基準に数の出現率を数えた。

- [blog/graph-piechart.py](https://github.com/popowa/blog/blob/master/code/aws-release/graph-piechart.py)

問題はタイトルで正式名称が使われていない可能性もあるし、必ずしも正しい訳ではないのはちょっと残念な所・・・

次に期待！

## 資料出来た！

[2017年AWSリリースここ掘れワンワン5分バージョン〜re:Inventは知らない子ですね〜](https://slideship.com/users/@popowa/presentations/2017/12/JjvQ18kV8p4BBkBPNTaWpo/)

## めちゃくちゃ参考になったページ
- [pyenvとvirtualenvで環境構築した時にmatplotlib.pyplotが使えなかった時の対処法](https://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49)
