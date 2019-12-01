Title: MacユーザーがWorkSpacesを使ってみた感想と学び
Date: 2017-04-04 01:25
Authors: ayakomuro
Tags:  AWS, workspaces
Slug:2017/04/macworkspaces
Status: published

15年程度Macを使っていた、Macユーザーがどこまで現在の端末を使ってWorkSpacesを使えるか試してみました。


#### 手元の端末

Mac Book Air (英語キーボード）

![画像](https://3.bp.blogspot.com/-lnhqtQrcPY8/WMX1DbYRAXI/AAAAAAAAfpU/UI6z4oa_8gMpRMiq411YeS6b85GCM19mQCLcB/s320/macbook-air-gallery2-2014_GEO_JP.jpeg)

外付けキーボード（英語）

![画像](https://1.bp.blogspot.com/-nmiLrAfvX1A/WOL0e9ae_LI/AAAAAAAAgZo/SVDVuW3GWogROTqgXCdTIxoVYIomlqrmACLcB/s320/us.jpg)
MagicMouse(オフィス） and/or Touchpad（家）

![画像](https://3.bp.blogspot.com/-sayGIPn1uvs/WOL0qPBDZoI/AAAAAAAAgZs/xh5vgBCwfsAKMCwsQOLgh6075KloZm5LwCLcB/s200/apple-magic-mouse.jpg)
![画像](https://2.bp.blogspot.com/-ypv8QzqjsZ0/WOL03NDNrpI/AAAAAAAAgZw/UqNtAkjtFToKjuWUR6Ddcysblq4_JWiGQCLcB/s200/41mi36PRTTL._SL1210_.jpg)

#### 用意したAWS WorkSpaces

-   Microsoft Windows 7 ＋Microsoft Office Professional 2010 
-   プロフェッショナルプラン
-   特にVPNなどは貼っておらず通常の利用方法
-   あとで時間課金に変更した

### 解決した課題 - WorkSpaces特有の問題



音声・画像共有を行えるかどうか





スカイプが利用出来た（音声は可能である。カメラは対応していない）

Google Hangoutも可能（カメラは対応していないが画面共有は可能）

-   こちらの声がハウリングしているらしいが、その際に使っていたApple
    EarPodは音を拾いやすいらしいので、音を下げるとハウリングしないらしい
-   何か問題があれば音声入力設定でTeradiciのを選ぶと大体解決する

カメラは使えないのでこれはもうどうしようもない





Windows Updateがちゃんと行えるかどうか





-   Windows
    UpdateをするとWorkSpacesがUnhealthyになる、という事象を聞いていたが、だいたい17分程度で完了した（3月9日に初回アップデートを実施）
-   その後何度か実施をしたが特にUnhealthyになる事はなかった（再起動等が必要ではあったが）





バックアップを考える





-   Dドライブが12時間おきにバックアップされている＆必要データは都度BOXにアップロードしていたので、既存バックアップでよしとした
-   [よくある質問 - Amazon
    WorkSpaces](https://aws.amazon.com/jp/workspaces/faqs/)



プリンターから出力出来るかどうか







-   ローカルプリンターに対応しているのでUSBで接続しているプリンターおよびネットワークにあるプリンターは印刷が可能なのだが、WorkSpacesからExcelの内容を印刷しようとするとWorkSpacesクライアントが落ちる。
-   PDFにしてWorkSpacesから印刷をするといけるので、当分はこれでしのげそうだけど、MS
    Officeから直接印刷出来るのが望ましい・・・



テンキーが使えない

-   Macのクライアントをアップデートしたら直った
-   [AWS Developer Forums: Workspaces IOS X Keyboard Issue... ](https://forums.aws.amazon.com/thread.jspa?threadID=149523)



BOXが使えない


-   会社の決まりでなぜかBOX Tools Installerを入れなければいけない。
-   そのまま実行しても入らないので管理者で実行する、でインストールを行う


### 解決した課題 - Windows OS特有の問題（Macユーザー故に知らない）

英語キーボード設定で日本語を入力出来るかどうか

Windowsで英語キーボードにする方法

-   地域と言語 \> キーボードと言語 \> キーボードの変更を確認
-   残すキーボードとしてはUSと日本語のIMEのキーボードだけでとりあえずいける

日本語入力する方法

切り替えはAlt+Shiftで可能だが、Appleの英語キーボードだと微妙な位置にありとても使いづらいので、Mac
OSみたいにCommand  +
Spaceで出来ないか調べたらAppleキーボードをWindowsで使うアプリがあった

-   [AppleKbWinの詳細情報 : Vector
    ソフトを探す！ ](http://www.vector.co.jp/soft/winnt/util/se394317.html)
-   確かに入れたIMEに切り替えが出来るか少し遅い（これはしょうがない）



Windowsのフォントがダサい





-   変更出来るらしいので変更してみた
-   [Windows7のフォント変更･設定方法･スムージング解除まとめ -
    ぼくんちのTV
    別館](http://freesoft.tvbok.com/windows7/desktop/font_smoothing.html)

 MagicMouseの横スクロールが出来ない





-   Shiftを押しながらすれば出来るらしい（え！？不便じゃない！？）



ファイルを削除するショートカットキー







-   ショートカットキーはやはり違うのでこれは覚えるしかないのかも・・
-   [Windows 用キーボード
    ショートカット ](https://support.microsoft.com/ja-jp/help/126449/keyboard-shortcuts-for-windows)





スクリーンショットの取り方が分からない





-   これも覚えるしかない・・・
-   [Snipping Tool を使ってスクリーン ショットをキャプチャする - Windows
    ヘルプ ](https://support.microsoft.com/ja-jp/help/13776/windows-use-snipping-tool-to-capture-screenshots)











### やって良かった事



仕事用のSingleSignOnを入れる - OneLogin





-   Chromeをインストールし、プラグインを入れる事で現状と変わらず認証が行えた。
-   OneLoginに認証情報設定していないアプリがあることに再認識をし、設定し直した事で、WorkSpacesに関わらずどの端末でもアプリにログイン出来るようになった（今までブラウザーに保存していたりクッキーが残っていたりで、認証をしていなかった例も少なからずあった）





Googleアカウントにブックマークと登録し同期させる





-   すぐにブラウザーがいつものブラウザーになるのでオススメ
-   [端末間で Chrome のデータを同期する - パソコン - Chrome
    ヘルプ ](https://support.google.com/chrome/answer/165139?co=GENIE.Platform%3DDesktop&hl=ja)





BOXに全データを置き、ローカルには日をまたぐデータは置かない





-   仕事のやり方の一つに、面倒だけど毎回必要なデータはBOXからダウンロード、作業、アップロードをしているので、特定の端末にしかないデータがないのは結果端末依存にならなかったので良かった



### 気づいた事



Chromebookはプリンターを認識しないので、印刷が限定的になる

WorkSpacesクライアントを閉じても向こうのOSが終了する訳ではないので、前日の作業からすぐに始められるのはとても効率がよい

MFA対応したいが、サーバーが必要なので、自分一人の為にサーバー立てるのもな〜〜と迷い中

-   [Google Authenticator を使って Amazon WorkSpaces
    に多要素認証ログイン ](http://aws.typepad.com/sajp/2014/10/google-authenticator.html)

今回パフォーマンスを選んでみたが、日常的な仕事だとその一つ下のスタンダードでもいいかも。

Datadogを入れて負荷を見ていたけども、ウェブ会議とかExcelでビボットテーブル作っているときぐらいしか負荷が高くない

-   でもメモリがずっと張り付いているのはなんでだろう？？

[popowa:
DatadogでWorkSpacesを監視する ](http://blog.popowa.com/2017/03/datadogworkspaces.html)



### 結論



-   WorkSpacesで仕事出来るが、端末を選ぶ
-   MacユーザーはWorkSpacesに慣れる前に、まずWindowsに慣れなければいけない
