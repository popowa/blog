Title: RightScaleを解き明かす\~ライトスクリプトを見てみよう\~
Date: 2011-07-31 09:27
Authors: ayakomuro
Tags:  Chef, Puppet, RightLink, RightScale, RightScale解体新書
Slug:2011/07/rightscale_31
Status: published

前回サーバテンプレートを使ってサーバを立ててみました。それではサーバテンプレートを構成している個々のスクリプトを見てみたいと思います。  

  
[]「デザイン」から「サーバテンプレート」を選択します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/server_template.png "server_template"){.alignnone
.size-full .wp-image-1322 width="153"
height="66"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/server_template.png)  
  
対象サーバサーバテンプレートを選択します。スクリプトタブを選択します。  
  
スクリプトの書き方  

-   シェルスクリプトです。
-   perlとか使えます。
-   Inputで入力した値は \"\$DB\_PASSWORD\"になります。
-   実行した値を変数として使いたい場合は \"[\$(grep -lir \"missingok\"
    \$logrotate\_file)]\"という風にします
-   直前に実行したコマンドの値は \"(\$?)\"になる
-   パッケージ毎の起動は、/etc/init.d/パッケージ
    restart（Debian系特有）ではなく、serviceを使って起動する
-   スクリプト内で設定された関数や、変数は引き継がれない事を前提にする。他のスクリプトに依存はせず、面倒でもスクリプト単体で、動くようにしておく
-   サーバテンプレートに対応させるサーバイメージを複数ディストリビューションにする場合は、分岐を入れる  
   （Debian系だとapt-get、CentOS系だとyumなど）
-   同じディストリビューションでもバージョンによってパッケージの依存関係が違っていたりするので、もし依存関係が違っていたら、個別にバージョンを確認し、必要なパッケージのインストール等を行う必要がある

  
**日本語化してみたライトスクリプト（随時追加）**  

-   [SYS Timezone set - 11H1
    JST](http://www.popowa.com/archives/1326 "ライトスクリプト: SYS Timezone set – 11H1 JST [rev 2]")
-   [SYS Syslog remote logging
    client](http://www.popowa.com/archives/1329 "ライトスクリプト：SYS Syslog remote logging client")
-   [MAIL Postfix local
    delivery](http://www.popowa.com/archives/1332 "ライトスクリプト：MAIL Postfix local delivery")

  
   
  
[**RightLink**]  
  
RightScaleが提供するサーバイメージ(v5以上)にはRightLinkというパッケージがはいっています。  
RightLinkは
ライトスクリプトとChefを動かす為のエージェントです。拡張してPuppetとかも動かす事が出来ます。  
  
MITライセンスで公開されているオープンソースです（[レポジトリはこちら](https://github.com/rightscale/right_link)）  
  
RightLink込みのサーバイメージの作り方はまた今度記事を書きたいと思います。  
  
個々のコマンドのバイナリは /usr/bin/rs\_のprefixであります。  
  
[**RightLinkのコマンド**]  
  
ほとんどのコマンドには以下のオプションがついています。  

-   \--verbose, -v  \#デバック情報を出力する
-   \--help \#ヘルプを出す
-   \--version \#パッケージのログを出す

  
rs\_log\_level（[サポートページ](http://support.rightscale.com/12-Guides/RightLink/RightLink_Command_Line_Utilities#rs_log_level)）  

-   ログレベルの設定
-   オプション  
   \--identify, -l \#ログ出力レベルを設定する  
   例：rs\_log\_level \--log-level debug

  
rs\_run\_recipe（[サポートページ](http://support.rightscale.com/12-Guides/RightLink/RightLink_Command_Line_Utilities#rs_run_recipe)）  

-   rs\_run\_right\_script（ライトスクリプト用）
    rs\_run\_recipe（Chef用）
-   スクリプトを実行させる  

    -   rs\_run\_recipe \--identity, -i ID \[\--json, -j JSON\_FILE\]
        \[\--verbose, -v\]
    -   rs\_run\_recipe \--name, -n NAME \[\--json, -j JSON\_FILE\]
        \[\--verbose, -v\]

      

-   オプション  
   \--identity, -i ID \#
    ライトスクリプトもしくはサーバテンプレートに設定されているChefのレシピのIDを取得する  
   \--name, -n 名前
    \#ライトスクリプトもしくはChefレシピ名(IDで上書きされている)  
   \--json, -j JSON\_FILE
    \#レシピを実行する前にJSONファイルを属性として取り込む  
   \--parameter, -p NAME=type:VALUE
    \#ライトスクリプトのInputを定義、もしくは上書きする（run\_right\_scriptのみ利用可能）

  
rs\_shutdown（サポートページ）  

-   インスタンスに対して再起動、停止、終了のリクエストを送ります
-   オプション  
   \--reboot, -r \#再起動のリクエストを送る  
   \--stop, -s
    \#停止のリクエストを送る（ルートディバイスがEBS等である際に利用出来ます）  
   \--terminate, -t \#終了リクエストを送る  
   \--immediately, -i \#リクエストを今すぐに実行させる  
   \--deferred, -d \#他のスクリプトが終了するまで待つ

  
rs\_tag（[サポートページ](http://support.rightscale.com/12-Guides/RightLink/RightLink_Command_Line_Utilities#rs_tag)）  

-   タグの一覧、追加、削除を現在のインスタンスや、クエリに対して行う事が出来る
-   オプション  
   \--list, -l \#現在のインスタンスのタグ一覧を表示する  
   \--add, -a タグ \#タグを追加する  
   例：rs\_tag \--add \'options:tags=awesome\'  
   \--remove -r タグ \#タグを削除する  
   例: rs\_tag \--remove \'options:tag=awesome\'  
   \--query, -q タグリスト
    \#デプロイメントのインスタンスのタグ情報を取得する

  

    一般的なパッケージ

  

    lsb_release

  

-   Linuxのバージョンを確認する
-   オプション  
   -v, \--help \#ヘルプを出力  
   -v, \--version  \#システムがサポートしているLSBモジュール
    を表示する  
   -i, \--id \#ディストリビューターの名前  
   出力例：Distributor ID: Ubuntu  
   -d, \--description \#ディストリビューションの説明を表示  
   出力例：Description: Ubuntu 10.04.2 LTS  
   -r, \--release \#ディストリビューションのリリース番号を表示  
   出力例：Release: 10.04  
   -c, \--codename \#コードネームを表示  
   出力例：Codename: lucid  
   -a, \--all \#上記情報を全部出す  
   -s,\--short \#短くして表示

  

    mknod（manページ）

  

-   指定したタイプのスペシャルファイルを作成します

  
 
