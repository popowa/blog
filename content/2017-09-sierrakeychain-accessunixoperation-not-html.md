Title: SierraのKeychain AccessでUNIX[Operation not permitted] と言われた時の対応
Date: 2017-09-11 00:12
Authors: ayakomuro
Tags:  Mac
Slug:2017/09/sierrakeychain-accessunixoperation-not
Status: published

Mac Book Air, Sierraで、Wifiパスワードをなかなか覚えてくれない事象があったので、調べて解決した。

現象

-   Wifiのパスワードを何度入れても覚えてくれない
-   Keychain
    Accessで古いwifi情報を消そうとしたら（一見消せそうに見えるんだけど）UNIX\[Operation
    not permitted\]と言われて、結局消せない

解決方法

1.  可能であればHDのバックアップをする（私は基本全部をWorkDocsか外部HDに入れているのでやらなかった）
2.  再起動しながらCommand + Rを押し続ける
3.  リカバリーモードが出て、言語を聞かれるので好きな言語を選ぶ
4.  OS再起動、ディスクユーティリティーとかのウィンドウが出るが、メニューバーからコマンドプロンプトを選択する
5.  以下のコマンドを入れて、実行する（エンターキーを押す）  
   csrutil disable
6.  特にアウトプットはないので、再度再起動
7.  Keychain accessで古い情報が消せるのを確認
8.  再度再起動しながらCommand+R
9.  先ほどと同じようにコマンドプロンプトを出して以下のコマンドを実行する  
   csrutil enable
10. また再起動。これでKeychain accessがうまく動くようになる







参考記事





-   [Cannot Delete Key from System Keychain \| Official Apple Support
    Communities ](https://discussions.apple.com/thread/7357200?start=0&tstart=0)
