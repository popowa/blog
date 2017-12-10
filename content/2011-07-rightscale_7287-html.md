Title: RightScaleを解き明かす\~サーバテンプレートの諸設定をしよう\~
Date: 2011-07-27 04:46
Authors: ayakomuro
Tags:  RightScale, RightScale解体新書
Slug:2011/07/rightscale_7287
Status: published






RightScaleの一番の醍醐味であるサーバテンプレートを分解して、どのようになっているか見て行きましょう。全部見終わったときは、「あ〜なるほど」と思って頂けると思います。



  



[]



  



「デザイン」-\>「サーバテンプレート」をクリックします。



  



[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss.png "ss"){.alignnone
.size-full .wp-image-1259 width="251"
height="71"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss.png)



  



見たいサーバテンプレートをクリックします。今回は「LAMP All-In-One with
wordpress JP- 11H1 v1」（複製を作ったもの）になります。



  



サーバテンプレートには以下のタブがあります。



  

-   イメージ
-   Repos
-   スクリプト
-   アラート
-   入力
-   Xref
-   Revisions

  
  

### 「イメージ」タブ

  
このサーバテンプレートに紐付けられているサーバイメージが表示されています。チェックボックスを他の物に選択する事で、他のサーバイメージ（例えば他のOSが良い場合など）を選ぶ事が出来ます。また「Add
MultiCloud
Image」をクリックすると、警告が出た後、マルチクラウドを選択出来るようになります。私はDebianが好きなので、Ubuntuを選択します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/images-300x177.png "images"){width="300"
height="177"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/images.png)  
  

### 「Repos」タブ

  
ここは主にレポジトリ情報を保持する場所です。そして大体保持している内容としてはChef
CookbooksとOSのディストリビューションのレポジトリになります。（例えば/etc/apt/source.listsに追加するパッケージのレポジトリ先、という感じです）  
  
   
  
![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/Repos.png "Repos"){width="91"
height="55"}  
  
RightScaleが提供しているサーバイメージに関しては彼らのOSのレポジトリがあり、独自のレポジトリを使いたい、というニーズがなければ通常はそのままです（逆を返せば、サーバーイメージのメンテナンスをRightScaleがしてくれている、という事になります）  
  
Chefに関してはきっちり触った事が無いので、調査してまた別の記事を書いてみたいと思います。  
  

### 「スクリプト」タブ

  
ここはサーバテンプレートがデプロイメントに入ってサーバを立てる時に実行されるスクリプト、また運用中、サーバを停止する時のスクリプト入っています。  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/script.png "script"){width="111"
height="52"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/script.png)  

-   Boot Scripts：サーバを立ち上げる時に実行されるスクリプト
-   Operational Scripts: 運用中に実行するであろうスクリプト
-   Decommission Scripts（ライトイメージv3以降で利用可能）:
    サーバを停止する時に使うスクリプト

  
以下がスクリプトの１例です。  
鉛筆のアイコンは、編集、虫眼鏡は中を見る、×は削除です。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/script_line.png "script_line"){width="577"
height="21"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/script_line.png)  
  
   
  
またスクリプトの実行する順番を変える事が出来ます。スクリプトは上から順に実行されます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/script_sort.png "script_sort"){width="75"
height="26"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/script_sort.png)  
  
スクリプトの例を以下に乗せます。他にも色々あるので除いてみてください。  
スクリプトページを開いた際に出る項目は以下のものがあります。  
  
Packages:
スペースで区切られたインストールされるパッケージリストになります（例：mysql-server
mysql-devel）ブート時にyumやapt/aptitude等で一括インストールされます  
  
Inputs：ここではサーバテンプレートで使われる値を変数にして、ユーザーに入力をゆだねる事が出来ます。例えばアプリケーションのパスだったり、MySQLのユーザーアカウント情報などを変数化して、後ほど入力で選ぶ事が出来ます。（例：OPT\_PHP\_MODULES\_LIST）  
  

> スクリプトタイトル：RightScript WEB PHP install - 11H1  
>
>     #!/bin/bash -e
>     #通常はライトスクリプトはbashかperl、rubyが使われる事が多いです。
>     #もし一行目に#!がなければ、#!/bin/bash -eが使われます。
>
>   
>
>     # Copyright (c) 2007-2011 by RightScale Inc., all rights reserved worldwide
>     #コピーライト
>     # Test for a reboot,  if this is a reboot just skip this script.
>     #ライトスクリプトの説明
>
>   
>
>     if test "$RS_REBOOT" = "true" ; then　<= もしリブードだったら
>       echo "Skip Php Modules install on reboot."　<= PHPモジュールインストールはスキップするよ、とエコー
>       logger -t RightScale "Php Modules Install,  skipped on a reboot." <= ログに記録
>       exit 0 <= 終了
>     fi
>
>     if [ $RS_DISTRO = ubuntu ]; then <= もしディストリビューションがUbuntuだったら
>       apt-get install -y php5 php5-mysql php-pear libapache2-mod-php5 $OPT_PHP_MODULES_LIST <= パッケージをインストール
>       a2enmod php5 <= PHP5のモジュールを有効化する
>       a2enmod proxy_http <= proxy_httpモジュールを有効化する
>       /etc/init.d/apache2 force-reload <= Apache2を強制リロード
>     elif [ $RS_DISTRO = centos ]; then <= もしCentOSだったら
>       yum install -y php php-mysql php-pear $OPT_PHP_MODULES_LIST <= パッケージをインストール
>        php_conf=/etc/httpd/conf.d/php.conf <=変数作成
>       if [ -f /etc/httpd/conf.d/php.disabled ]; then　<=PHP設定の確認、無効になっていたら、有効にする
>            echo "Enabling PHP configuration..."
>            mv -f /etc/httpd/conf.d/php.disabled $php_conf
>      fi
>      if [ -f $php_conf ]; then <= php.conf設定がなければ、諸設定をする
>          perl -p -i -e 's/#LoadModule php5_module modules/libphp5.so/LoadModule php5_module modules/libphp5.so/' $php_conf
>           perl -p -i -e 's/#DirectoryIndex index.php/DirectoryIndex default.php index.php/' $php_conf
>             perl -p -i -e 's/#AddHandler php5-script .php/AddHandler php5-script .php/' $php_conf
>           perl -p -i -e 's/#AddType text/html .php/AddType text/html .php/' $php_conf
>         fi
>      # delete default welcome
>        if [ -e /etc/httpd/conf.d/welcome.conf ]; then <= ディフォルトのウェルカムページを削除する
>           rm -f /etc/httpd/conf.d/welcome.conf
>        fi
>     fi
>
>     logger -t RightScale "Installed Php Modules."　<= ログに記録
>
>   

  
  

「アラート」タブ
----------------

  
アラートは、サーバのCPU/メモリ/容量/アプリの状態/特定のファイルの状態によって、警告メールを飛ばす設定が出来ます。NagiosやZabbixの部分だと思って頂ければいいと思います。アラートはモニターされているサーバーのみ利用する事が出来ます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/alert.png "alert"){width="91"
height="48"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/alert.png)  
  
タイトル、コンディション、鉛筆のアイコンは編集、Xマークは削除になります。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/alert_2.png "alert_2"){.alignnone
.size-full .wp-image-1261 width="502"
height="37"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/alert_2.png)  
  
タイトルの右横にある(i)にマウスオーバーするとアラートの説明が表示されます。  
例えばApacheやトラフィックに負荷がかかっていて、現在のプロセスに空きスロットがない場合にアラートを送ります。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/alert_description.png "alert_description"){.alignnone
.size-full .wp-image-1262 width="390"
height="29"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/alert_description.png)  
  
トリガーになる値を変更したい場合は、変更ボタン（鉛筆）をクリックすると値を入力する画面に遷移します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/alert_edit.jpg "alert_edit"){.alignnone
.size-full .wp-image-1265 width="505"
height="151"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/alert_edit.jpg)  
  
アラートは、サーバテンプレート、サーバアレイ、サーバそのものにも追加する事が出来ます。またアラートは実際に稼働した後は、有効/無効、メンテナンス等で１時間off/24時間offをする事が出来ます。  
  
アラートに達する状態が起こった場合、以下のアクションがサポートされています。  

-   メールを送る
-   サーバをリブードする
-   サーバを再ロンチする
-   ライトスクリプトを走らせる
-   サーバアレイに呼び出してスケールアップする（サーバアレイは有償エディションしか使えません
    X
-   サーバアレイを呼び出してスケールダウンする

  
  

「入力」タブ
------------

  
入力タブでは、ライトスクリプトで使われる変数の設定をする事が出来ます。使われる場所はChef
Cookbook、ライトスクリプトになり、入力必須で未入力な場所は赤い線が出ています。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input.png "input"){.alignnone
.size-full .wp-image-1266 width="63"
height="46"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input.png)  
  
変数名とその値、またどこで使われているかを選択する事が出来ます。  
  
変数名  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input_title.png "input_title"){.alignnone
.size-full .wp-image-1269 width="165"
height="37"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input_title.png)  
  
その値のタイプ（Ignore: 利用しない / Env: サーバの環境値 / Array: 配列 /
Cred: 証明書で作成した値 、Key: SSHの鍵）  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input_select.png "input_select"){.alignnone
.size-full .wp-image-1267 width="75"
height="111"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input_select.png)  
  
Credを選択してみます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input_select_2.png "input_select_2"){.alignnone
.size-full .wp-image-1268 width="195"
height="107"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input_select_2.png)  
  
どこで使われているかの説明とリンク  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input_used.png "input_used"){.alignnone
.size-full .wp-image-1270 width="487"
height="56"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input_used.png)  
  

「Xref」タブ
------------

  
これは稼働中、非稼働のサーバで使われているサーバテンプレートのリファレンスを表示します。利用しているクラウド構築の一覧としても見る事が出来ます。これは運用の記事でも再度取り上げたいと思います。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/xref.png "xref"){.alignnone
.size-full .wp-image-1271 width="67"
height="47"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/xref.png)  
  

「Revision」タブ
----------------

  
Revisionタブではコミットされたサーバテンプレートの履歴を見る事が出来ます。特定のバージョンのスナップショットを見る事が出来ます。これも運用の記事で再度取り上げたいと思います。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/revison.png "revison"){.alignnone
.size-full .wp-image-1273 width="100"
height="45"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/revison.png)  
  
現在HEAD（最新）しかないので、一行しか表示されません。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/revision_list.png "revision_list"){.alignnone
.size-full .wp-image-1272 width="199"
height="60"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/revision_list.png)  
  

コミット
--------

  
変更や追加、削除が終われば、コミットをして、リビジョンを確定させます。  
  
コメントを入力する枠、またあればマルチクラウドを紐付ける設定を確定させるか、などのオプションが出てきます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/commit.png "commit"){.alignnone
.size-full .wp-image-1274 width="75"
height="29"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/commit.png)  
  
コミットすると、\[HEAD\]だった物が\[Rev1\]になって、変更をした物が\[HEAD\]になります。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/revision.png "revision"){.alignnone
.size-full .wp-image-1275 width="299"
height="47"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/revision.png)  
  
   
  
   
  
   
  
   
  
   
  
 
