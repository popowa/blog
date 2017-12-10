Title: 
Date: 2013-05-27 23:09
Authors: ayakomuro
Tags:  S3
Slug:2013/05/awss3windows
Status: published


AWSのS3をWindowsで使う+時々WindowsでS3をエクスプローラーみたいに使いたいというご要望を頂く事があり、どんなアプリがあるのだろうかと思って調べてみました（手元にあるのはSurface。。。）

また見つけたら追記します。

-   [popowa: AWSのS3をWindowsで使う -
    2014年版 ](http://blog.popowa.com/2014/10/awss3windows-2014.html)

アプリ
------

### [S3 Browser](http://s3browser.com/)

-   個人で使う場合は無償版
-   商用、企業で使う場合は[有償版](http://s3browser.com/buypro.php)。大体30ドル〜50ドル程度
-   メモ：S3
    BrowserポータブルというUSBにアプリを入れて使える製品も売っている
-   アプリを開いてファイルを操作するイメージ
-   2014年もまだ健在

### [[CloudBerry Explorer](http://www.cloudberrylab.com/products.aspx)]



色々なクラウドストレージに対応した製品を出している

無償版あり

有償版では、暗号化、圧縮、5TBまでのファイルコピー、HTTPヘッダーの事前設定が可能。IAMもサポートしている

アプリを開いてファイルを操作するイメージ

2014年もまだ健在

参考URL

-   [Windows用S3クライアント，CloudBerry
    Proは同期ができる。](http://debiancdn.wordpress.com/2011/10/17/windows%E7%94%A8s3%E3%82%AF%E3%83%A9%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%88%EF%BC%8Ccloudberry-pro%E3%81%AF%E5%90%8C%E6%9C%9F%E3%81%8C%E3%81%A7%E3%81%8D%E3%82%8B%E3%80%82/)

### [DragonDisk](http://www.dragondisk.com/)





無償版のみ

Windows以外のプラットフォーム対応アプリもある

アプリを開いてファイルを操作するイメージ

2014年時点: 開発は停止している？

-   [Amazon S3 + Glacier + DragonDisk
    による低価格＆高信頼性バックアップ環境の構築 (1) - Smart-PDA.net
    管理者のブログ ](http://blog.smart-pda.net/2013/02/amazon-s3-glacier-dragondisk-1.html)

### [TntDrive](http://tntdrive.com/)



-   30日間無料、その後個人利用は40ドルぐらい、商用利用は６０ドルぐらい
-   ネットワークドライブにマッピングして操作するイメージ





### [Gladinet](http://www.gladinet.com/)



-   トライアルありの有償版。月額プランにて、ストレージアカウントはGladinet側にある模様（個人のアカウントで操作するものではなさげ）SaaS形式
-   ネットワークドライブにマッピングして操作するイメージ



### [Jungle Disk](https://www.jungledisk.com/)



-   月額2ドル〜、ストレージアカウントはサービス側負担。SaaS形式
-   バックアップ、同期、ファイル操作などが可能

### [CrossFTP](http://www.crossftp.com/)

-   30日間無料、その後25ドルぐらい 
-   2014年も健在



### [S3 Browser for Windows Live Writer](http://s3browser.codeplex.com/)



-   無償
-   あまり多機能ではなさげ 



### [WebDrive](http://www.webdrive.com/products/webdrive/index.html)



-   20日無料、その後70ドルぐらい
-   ネットワークドライブとしてマッピングが可能
-   \[追記\]
    日本語ページがあるそうです！　<http://webdrive.add-soft.jp/>　



### [GoodSync](http://www.goodsync.com/platforms/windows-desktop)



-   Goodsync for Mac for Windows的な感じでややこしいw
-   30日無料、その後30ドルぐらい
-   有料/一定期間のお試し有り
-   ファイルの自動同期
-   GoodSync for Windows
    Desktopから名前が変わってGoodSyncに変わったみたい



### [ExpanDrive 3](http://www.expandrive.com/expandrive)



-   ネットワークドライブとしてマッピングが可能
-   ３０日間無償、その後３０ドルぐらい
-   [Strongspace](https://www.strongspace.com/)というバックアップに特化した製品もあり



### [CA ARCserve Backup](http://www.arcserve.com/jp/backup.aspx)

エンタープライズ向け。元々はバックアップファイルのアーカイブをS3に持って行くという感じの機能 

参考URL: 

-   [Amazon S3 クラウド
    ストレージへのデータのアーカイブ](https://support.ca.com/cadocs/0/CA%20ARCserve%20%20Backup%20r16-JPN/Bookshelf_Files/HTML/relsumry/index.htm?toc.htm?1579393.html)

初期15万ぐらい。高い。。

### [SyncBack](http://www.2brightsparks.com/syncback/syncback-hub.html)



-   無償版、有償版と機能別に分かれている
-   SyncBack proしかS3に対応してない模様
    -\> [比較表](http://www.2brightsparks.com/syncback/compare.html)



### [Bucket Explorer](http://www.bucketexplorer.com/)



-   15日、もしくは30日の無償版、その後有償版で７０ドル程度
-   コマンドラインも提供されている

### [TyphoonBackup](http://www.typhoonbackup.com/)





-   制限付きの無償版、機能別有償版あり
-   ストレージは先方負担（容量が必要であればアップグレードが必要）

### [ElephantDrive](http://home.elephantdrive.com/)

-   昔からある製品
-   無償版、容量が増えるにつれて金額が増える有償版
-   ストレージは先方負担

### [S3Safe](http://www.lumensystems.com/s3safe.aspx)





-   無料









コマンドライン



-   [Standalone Windows .EXE command line utility for Amazon S3 &
    EC2](http://s3.codeplex.com/)
-   [s3sync, s3cmd](http://s3tools.org/s3tools)

### ドキュメント

-   [Using the AWS Tools for Windows
    PowerShell](http://docs.aws.amazon.com/powershell/latest/userguide/pstools-using.html)
-   [.NET 用 AWS SDK](http://aws.amazon.com/jp/sdkfornet/)
