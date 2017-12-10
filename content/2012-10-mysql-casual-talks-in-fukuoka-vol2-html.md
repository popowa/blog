Title: MySQL Casual Talks in Fukuoka vol.2 に参加した
Date: 2012-10-21 14:41
Authors: ayakomuro
Tags:  MySQL, 国内イベント, 福岡
Slug:2012/10/mysql-casual-talks-in-fukuoka-vol2
Status: published

Cloud Days

Fukuokaに出展をした後、日本オラクルさんでMySQL Casual Fukuoka
が開催される、という事で、参加してきました。







\#まとめが無かったので、今しがたまとめてみた





> [MySQL Casual Talks Vol.2
> \#mysql\_casual\_fukuoka](http://togetter.com/li/393674 "MySQL Casual Talks Vol.2 #mysql_casual_fukuoka")

[] 内容としてはATNDの通りで

-   AWSでMySQL(5.6)のベンチ by @Spring\_MTさん
-   MySQL Connect 2012での新着情報(予定) by @RKajiyama さん
-   5.6のレプリケーション周りを試してみた by @matsumana  
-   AWSでMySQL使うときの話とか by @debility さん
-   MySQL for Excel の紹介 by @yyamasaki1さん
-   カジュアルにネクストキーロック　by @kitakohさん

という感じでした[。slideshareはこちらのページ](http://spring-mt.tumblr.com/post/33874028810/mysql-casual-talks-in-fukuoka-vol-2-talk)を見るとよいでしょう。

まずですね、今回もMySQL5.6の機能検証などが目玉トピックだったのですが、やはりMySQL5.6はすごい。機能大杉。メジャーアップデートじゃないのが未だに理解出来ない。

### 1) MyISAM＼(\^o\^)／

まとめにもありますが、MyISAMは居なくはならないが、積極的な開発は行なわれないそうです（アーキテクチャが古いというのも理由の一つにあるそう）。

InnoDBの力の入れ具合といったら、ハンパない感じですので、今後MySQLを使う案件があれば迷わずInnoDBを選ぶのがよいと思います（むしろMyISAM選ぶのは何もメリットがないと思われる）

### 2) OracleはMySQLに力入れてるよ★

以前、bugfixの報告内容が詳細でなく、もしかしたらOracleはMySQLを終わらせようとしているのではないか！？という記事が出ましたが、そんな事ないそうです。  
積極的に開発してますよーという事でした。

時々MySQL for
Excelというニッチなプラグインを作ったりもしているようです。

### 3) MySQL 5.6 on RDSはいつに。。？

こんなに胸熱な5.6がRDSに乗るのはいつになるのでしょうか。RDSに関しては、Oracleの人と、AWSの人がどのような役割分担でやっているのかちょっと分からない（中の人）という事だったので、これまらユーザーの声が大きければ移植されるのでしょうか。

MultiAZも5.6のGTIDとかで実装するのであれば、それ以下のバージョンとはちょっと違うインプリになりそうだなぁなんて思ったりもしました。PostgreSQL
on RDS とMySQL 5.6 on
RDSが出てくれれば何も文句言わないので、ぜひAWSな方々ご検討お願いします！！

という訳で今回のMySQL Casual Talks in Fukuoka
vol.2[も]非常に面白かったです。  
Cloud Daysのイベントなければ懇親会にいきたかったのだが。。。次回は是非！

会場を貸してくれた日本オラクル様、登壇者の皆さん、主催者の@Spring\_MTさん、参加者の皆さん、どうも有り難うございました！！！

ウェンディーと写真も撮ったよ♥　もふもふしてた。

[![](http://3.bp.blogspot.com/-1ZnOXAnPELY/UIQHgTDgHYI/AAAAAAAAUqg/1ZiRh0qhals/s400/IMAG0906.jpg){width="400"
height="238"}](http://3.bp.blogspot.com/-1ZnOXAnPELY/UIQHgTDgHYI/AAAAAAAAUqg/1ZiRh0qhals/s1600/IMAG0906.jpg)


