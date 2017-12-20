Title: 
Date: 2012-05-03 21:28
Authors: ayakomuro
Tags:  Apache
Slug:2012/05/apache-software-foundation-hosted
Status: published


Foundationがホストしているインキュベーション状態のソフトウェア一覧+前回[福岡インフラ勉強会](https://www.facebook.com/groups/100825430047874/)で開催した、[Webサーバ勉強会＠福岡](http://atnd.org/events/26885)で発表したので、資料と追記情報をアップしたいと思います。  
[]  
Apache Software
Foundation(以下ASF)は、ホストしているソフトウェアに対して組織化サポート、法的サポート、金銭的サポート（ホストサーバを提供するなど）を提供しています。

多くのソフトウェアがASFに受け入れられ、有志によって継続的な開発が行われ、ある程度の開発をし尽くしたら、リタイアという形で開発が中止されたりもしています（例えばCMS系はある程度で尽くした感がありリタイアしている物も多し）。

その時の資料はこちら

**[恐るべきApache,
Web勉強会＠福岡](http://www.slideshare.net/popowa/apache-web "恐るべきApache, Web勉強会＠福岡")**

View more [presentations](http://www.slideshare.net/) from [Aya
Komuro](http://www.slideshare.net/popowa)

最後まで調べきれなかったインキュベーション状態（正式リリースされていない）のアプリについて調べましたのでご紹介します。  
全体的に見ると、今までのASFがホストしてきたソフト（[カテゴリ一覧](http://projects.apache.org/indexes/category.html)）は、CMS周りやRDBMSなデータベースが多かったのですが、[インキュベーション状態のソフト](http://incubator.apache.org/)の多くはクラウドを操るものだったり、(Hadoop関係の)BigData周りなどのソフトが多く、時代の移り変わりを感じさせます。

### [Airvata](http://incubator.apache.org/airavata/)

-    [![](http://4.bp.blogspot.com/-mvsxBsgYRtk/T6Ij3gm-1yI/AAAAAAAAQ_w/XXdYtmVc4oQ/s200/airavata-logo.png){width="200"
    height="137"}](http://4.bp.blogspot.com/-mvsxBsgYRtk/T6Ij3gm-1yI/AAAAAAAAQ_w/XXdYtmVc4oQ/s1600/airavata-logo.png)
-   ローカルなクラスタからナショナルグリッドやクラウドなどのリソースを構成、管理、実行、監視する管理とワークフローフレームワーク

### [Ambari](http://incubator.apache.org/ambari/)

-    [![](http://3.bp.blogspot.com/-4-cbOA1Dx5k/T6IkCDXekfI/AAAAAAAAQ_4/JWA3-ULoR00/s320/apache-ambari-project.png){width="320"
    height="29"}](http://3.bp.blogspot.com/-4-cbOA1Dx5k/T6IkCDXekfI/AAAAAAAAQ_4/JWA3-ULoR00/s1600/apache-ambari-project.png)
-   Hadoopクラスタを監視、管理、ライフサイクル管理する

### [Amber](https://cwiki.apache.org/confluence/display/AMBER/Index)

-   Java開発でのOAuth構築用フレームワーク

### [Ayn23（Anything To Triples）](http://incubator.apache.org/any23/)

-    [![](http://3.bp.blogspot.com/-IqccJI1MIqk/T6IlrQXhdbI/AAAAAAAARAA/-5nGRvfvHo8/s200/logo-any23.png){width="200"
    height="124"}](http://3.bp.blogspot.com/-IqccJI1MIqk/T6IlrQXhdbI/AAAAAAAARAA/-5nGRvfvHo8/s1600/logo-any23.png)
-   多様な形式のウェブコンテンツからRDF形式に出力するライブラリ

### [AWF](http://incubator.apache.org/awf/)

-    [![](http://2.bp.blogspot.com/-FDz_902jUMM/T6ImQhS1X5I/AAAAAAAARAI/WFjr4Q8OgYg/s1600/awf-logo.png)](http://2.bp.blogspot.com/-FDz_902jUMM/T6ImQhS1X5I/AAAAAAAARAI/WFjr4Q8OgYg/s1600/awf-logo.png)
-   JVM上で動くノンブロッキング、非同期、イベント駆動の高パフォーマンスウェブフレームワーク

### [BigTop](http://incubator.apache.org/bigtop/)

-    [![](http://1.bp.blogspot.com/-F1dTGa7pJsw/T6ImbFg5e-I/AAAAAAAARAQ/yWKkkzMj580/s1600/bigtop-logo.png)](http://1.bp.blogspot.com/-F1dTGa7pJsw/T6ImbFg5e-I/AAAAAAAARAQ/yWKkkzMj580/s1600/bigtop-logo.png)
-   Hadoopをパッケージしテストするツール

### [Bloodhound](http://incubator.apache.org/bloodhound/)

-    [![](http://4.bp.blogspot.com/-PnaTQJI1Ajo/T6ImoVCMPjI/AAAAAAAARAY/XWxDfhlHWII/s1600/logo_houndOnly.png)](http://4.bp.blogspot.com/-PnaTQJI1Ajo/T6ImoVCMPjI/AAAAAAAARAY/XWxDfhlHWII/s1600/logo_houndOnly.png)
-   Tracの派生版

### [Celix](http://incubator.apache.org/celix/)

-    [![](http://3.bp.blogspot.com/-GLX85dkmi4A/T6InRz7911I/AAAAAAAARAg/Iew1ck5szds/s200/celix.png){width="200"
    height="72"}](http://3.bp.blogspot.com/-GLX85dkmi4A/T6InRz7911I/AAAAAAAARAg/Iew1ck5szds/s1600/celix.png)
-   (JavaとCが相互間で動くように注力されてCに移植された)OSGi

### [Chukwa](http://incubator.apache.org/chukwa/)

-    [![](http://3.bp.blogspot.com/-HUqGhHRvBQc/T6InrV9aAUI/AAAAAAAARAo/kmPaW-4Jr7U/s1600/chukwa_logo_small.jpg)](http://3.bp.blogspot.com/-HUqGhHRvBQc/T6InrV9aAUI/AAAAAAAARAo/kmPaW-4Jr7U/s1600/chukwa_logo_small.jpg)
-   データコレクション用の監視システム

### [Clerezza](http://incubator.apache.org/clerezza/)

-    [![](http://1.bp.blogspot.com/-lPnqoaa_r4Y/T6IoeETH-oI/AAAAAAAARAw/HUtL1htmXOE/s1600/logo.png)](http://1.bp.blogspot.com/-lPnqoaa_r4Y/T6IoeETH-oI/AAAAAAAARAw/HUtL1htmXOE/s1600/logo.png)
-   RESTFulなウェブアプリケーションやサービスを開発出来るOSGiベースのモジュール群

### [CloudStack](http://www.cloudstack.org/)

-    [![](http://1.bp.blogspot.com/-EH4BElCa310/T6IotV79AZI/AAAAAAAARA4/4JmHTp_5VII/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+15.41.47%EF%BC%89.png)](http://1.bp.blogspot.com/-EH4BElCa310/T6IotV79AZI/AAAAAAAARA4/4JmHTp_5VII/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+15.41.47%EF%BC%89.png)
-   IaaS仮想化管理システム

###  

### [Cordova（旧Callback）](http://incubator.apache.org/callback/)

-    [![](http://1.bp.blogspot.com/-okVMBR9JkTQ/T6Io6tQOm3I/AAAAAAAARBA/7OPWdlkaPbg/s200/cordova-st-sign-a-300x130.png){width="200"
    height="86"}](http://1.bp.blogspot.com/-okVMBR9JkTQ/T6Io6tQOm3I/AAAAAAAARBA/7OPWdlkaPbg/s1600/cordova-st-sign-a-300x130.png)
-   HTML/CSS/Javascriptを使ってネイティブモバイルアプリを構築出来るプラットフォーム

### [DeltaSpike](https://cwiki.apache.org/confluence/display/DeltaSpike/Index)

-    Java SEとEEプラットフォームで開発を行う為のJSR-299 (CDI)拡張群

### [DeviceMap](http://incubator.apache.org/devicemap/)

-    [![](http://4.bp.blogspot.com/-RlAJi4vQAl8/T6IpoA6J0XI/AAAAAAAARBI/NxURlnRS3X8/s200/devicemap-logo-300-98.png){width="200"
    height="65"}](http://4.bp.blogspot.com/-RlAJi4vQAl8/T6IpoA6J0XI/AAAAAAAARBI/NxURlnRS3X8/s1600/devicemap-logo-300-98.png)
-   端末情報、画像など端末に関する情報のレポジトリを作る事が出来るツール

### [DirectMemory](http://incubator.apache.org/directmemory/)

-    [![](http://2.bp.blogspot.com/-Us-NKZ1fr_8/T6Iqk5dFa1I/AAAAAAAARBU/1ysjNMGpWH0/s1600/Apache-DirectMemory-logo-flat-small.png)](http://2.bp.blogspot.com/-Us-NKZ1fr_8/T6Iqk5dFa1I/AAAAAAAARBU/1ysjNMGpWH0/s1600/Apache-DirectMemory-logo-flat-small.png)
-   JVMのGCパフォーマンスに影響を与えずに大量のJavaオブジェクトを扱えるようにしたオフヒープメモリ管理（別名ビックメモリ）機能を含める複数レイヤーのキャッシュシステム

### [Droid](http://incubator.apache.org/droids/)

-    [![](http://4.bp.blogspot.com/-SeUbDqHhlbw/T6Iq7LPAWLI/AAAAAAAARBg/TCXkCGZKOgU/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+15.51.10%EF%BC%89.png)](http://4.bp.blogspot.com/-SeUbDqHhlbw/T6Iq7LPAWLI/AAAAAAAARBg/TCXkCGZKOgU/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+15.51.10%EF%BC%89.png)
-   スタンドアロンのロボットフレームワーク

###  [Easyant](http://incubator.apache.org/easyant/)

-    [![](http://1.bp.blogspot.com/-P4hbTtdKPME/T6IreJ3bA2I/AAAAAAAARBo/9wJRheSuIvA/s200/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+15.53.29%EF%BC%89.png){width="200"
    height="76"}](http://1.bp.blogspot.com/-P4hbTtdKPME/T6IreJ3bA2I/AAAAAAAARBo/9wJRheSuIvA/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+15.53.29%EF%BC%89.png)
-   AntとIvyをベースにしたビルドシステム

### [Etch](http://incubator.apache.org/etch/)

-    [![](http://1.bp.blogspot.com/-EAQQPaP5N3E/T6Ir_p12gGI/AAAAAAAARBw/UQATs0xvYYE/s1600/etch-logo.png)](http://1.bp.blogspot.com/-EAQQPaP5N3E/T6Ir_p12gGI/AAAAAAAARBw/UQATs0xvYYE/s1600/etch-logo.png)
-   ネットワークサービスの開発、使用を行うクロスプラットフォームで言語と経路フリーのフレームワーク

### [Flex](http://incubator.apache.org/flex/)

-    [![](http://3.bp.blogspot.com/-_6NfIOPnSFc/T6IsKy5R_7I/AAAAAAAARB8/TPWvg5pLfjs/s1600/flex.png)](http://3.bp.blogspot.com/-_6NfIOPnSFc/T6IsKy5R_7I/AAAAAAAARB8/TPWvg5pLfjs/s1600/flex.png)
-   Flashベースで携帯・ブラウザ/デスクトップ用のアプリを作るフレームワーク

### [Flume](http://incubator.apache.org/flume/)

-    [![](http://3.bp.blogspot.com/-dgfLqaQVj2Q/T6I4-wWyoKI/AAAAAAAARCI/OPp0yslk_K4/s1600/flume-logo.jpeg)](http://3.bp.blogspot.com/-dgfLqaQVj2Q/T6I4-wWyoKI/AAAAAAAARCI/OPp0yslk_K4/s1600/flume-logo.jpeg)
-   複数のソースからの(ログ)データ収集管理
-   似ているアプリ: scribe, fluent

### [Giraph](http://incubator.apache.org/giraph/)

-    大規模で耐障害性の大量同時並行グラフ処理フレームワーク

### [Hama](http://incubator.apache.org/hama/)

-    [![](http://3.bp.blogspot.com/-WmYdmRFPfFE/T6I59_9y8JI/AAAAAAAARCQ/61Wgoq3-CbU/s200/hama_art_arthur_300x220.png){width="200"
    height="146"}](http://3.bp.blogspot.com/-WmYdmRFPfFE/T6I59_9y8JI/AAAAAAAARCQ/61Wgoq3-CbU/s1600/hama_art_arthur_300x220.png)
-   Hadoop向け大量同時並行配信ファイルシステム用フレームワーク

### [HCatalog](http://incubator.apache.org/hcatalog/)

-    Hadoopを使ったデータ作成用テーブルとストレージ管理サービス

### [Isis](http://incubator.apache.org/isis/)

-    [![](http://2.bp.blogspot.com/-yHq62N1TO0A/T6Hfsbc_HKI/AAAAAAAAQ9E/xsI0lDlf970/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%25EF%25BC%25882012-05-03+10.02.30%25EF%25BC%2589.png)](http://2.bp.blogspot.com/-yHq62N1TO0A/T6Hfsbc_HKI/AAAAAAAAQ9E/xsI0lDlf970/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%25EF%25BC%25882012-05-03+10.02.30%25EF%25BC%2589.png)
-   ドメイン駆動アプリの開発を高速に行える

### [JSPWiki](http://incubator.apache.org/jspwiki/)

-    [![](http://2.bp.blogspot.com/-TJVz4JEQvNQ/T6HhWFu59LI/AAAAAAAAQ9M/Ou_SSsIMKXY/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+10.35.12%EF%BC%89.png)](http://2.bp.blogspot.com/-TJVz4JEQvNQ/T6HhWFu59LI/AAAAAAAAQ9M/Ou_SSsIMKXY/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+10.35.12%EF%BC%89.png)
-   JSPWikiソフトウェアをベースとしたモジュール型、ユーザー主導の拡張型Wikiエンジンシステム
-   2008年からやっている。サイト上もリンク切れなど多く、不明な点が多い



### [Kafka](http://incubator.apache.org/kafka/)

-   高いスループットでの配信、購読メッセージ提供システム
-   Hadoopにデータを並行投入させる等
-   似ているアプリ：FacebookのScribeやApache Flume 等

### [Kalumet](https://cwiki.apache.org/confluence/display/KALUMET/Index)

-   J2EEを含む環境構築管理
-   あまり情報がないのでどのくらい進んでいるのか不明

### [Kato](http://incubator.apache.org/kato/site/index.html)

-   JVMによる後継診断用Java API群（JSR 326)

### [Kitty](http://incubator.apache.org/kitty/)

-   軽量、プロダクト中心のJavaベースのアプリケーションサーバーのパフォーマンス診断と管理ユーティリティツール
-   Tomcatなどと一緒に使う













###  [Lucene.Net](http://incubator.apache.org/lucene.net/)





-    [![](http://4.bp.blogspot.com/-xpLJMwGvokk/T6IMRPTMnjI/AAAAAAAAQ9k/a1l3kTvQAas/s320/lucene-medium.png){width="320"
    height="59"}](http://4.bp.blogspot.com/-xpLJMwGvokk/T6IMRPTMnjI/AAAAAAAAQ9k/a1l3kTvQAas/s1600/lucene-medium.png)
-   Lucene検索エンジンをC\#と.NETプラットフォーム向けに移植
-   利用者や、商業プロダクト化している所が多い模様









### [ManifoldCF (MCF)](http://incubator.apache.org/connectors/ja_JP/index.html)





-    [![](http://1.bp.blogspot.com/-tpStJgxvHOw/T6INhBSzqdI/AAAAAAAAQ9s/aLyfmSMIhnU/s1600/ManifoldCF-logo.PNG)](http://1.bp.blogspot.com/-tpStJgxvHOw/T6INhBSzqdI/AAAAAAAAQ9s/aLyfmSMIhnU/s1600/ManifoldCF-logo.PNG)
-   Microsoft SharepointやEMC
    Documentumなどが抱えているコンテンツに単一APIでアクセス出来るようになるフレームワーク
-   ドキュメントが日本語化されている





### [Mesos](http://incubator.apache.org/mesos/)





-   クラスター間での動的リソース共有と有効的なリソース占有を行える管理ツール

### [MRUnit](http://incubator.apache.org/mrunit/)

-    [![](http://2.bp.blogspot.com/-vbOZwe1dgh0/T6IPEYHz5sI/AAAAAAAAQ90/ZvVPPtI2BGU/s200/mrunit_logo.png){width="200"
    height="69"}](http://2.bp.blogspot.com/-vbOZwe1dgh0/T6IPEYHz5sI/AAAAAAAAQ90/ZvVPPtI2BGU/s1600/mrunit_logo.png)
-   Hadoop MapReduceのジョブのユニットテストをサポートするライブラリ

### [NPanday](http://incubator.apache.org/npanday/)

-   [![](http://1.bp.blogspot.com/-WG6B4EdJWDw/T6IQkMoF9PI/AAAAAAAAQ98/9WxVztVvcRk/s320/NPanday.png){width="320"
    height="83"}](http://1.bp.blogspot.com/-WG6B4EdJWDw/T6IQkMoF9PI/AAAAAAAAQ98/9WxVztVvcRk/s1600/NPanday.png)
-   .NETフレームワークを作ってMaven用にプロジェクトを作れる、またはMavenプロジェクトに変換出来る

### [Nuvem](http://incubator.apache.org/nuvem/)

-   一般的なクラウドプラットフォームを横断的に利用出来るプログラムインターフェイスを提供
-   似た他のサービス: cloudkick?

### [ODF Toolkit](http://incubator.apache.org/odftoolkit/)

-   オープンドキュメントフォーマット (ISO/IEC 26300 ==
    ODF)のドキュメントをプログラマ的に作成、スキャン、複製出来るJavaモジュールセット

### [ Oozie](http://incubator.apache.org/oozie/)

-   Hadoopのデータプロセスのジョブをスケジュール管理とコーディネート管理出来るサーバーサイドのワークフローシステム

### [Openmeetings ](http://incubator.apache.org/openmeetings/)

-    [![](http://2.bp.blogspot.com/-tiGLxSS17NY/T6IVu3SfvLI/AAAAAAAAQ-I/0jZ7iG4AR7o/s320/logo-2.jpg){width="320"
    height="64"}](http://2.bp.blogspot.com/-tiGLxSS17NY/T6IVu3SfvLI/AAAAAAAAQ-I/0jZ7iG4AR7o/s1600/logo-2.jpg)
-   ビデオカンファレンス、チャット機能、ホワイトボード、同時ドキュメント編集、Red5ストリーミングサーバーのAPI機能を使ったグループウェアツールなどを提供



### [OpenOffice.org](http://incubator.apache.org/openofficeorg/)





-   [![](http://3.bp.blogspot.com/-H5O-62mPxQ0/T6IWuGoBchI/AAAAAAAAQ-Q/Z9OCndTAZsQ/s1600/300x100_dj_trans.png)](http://3.bp.blogspot.com/-H5O-62mPxQ0/T6IWuGoBchI/AAAAAAAAQ-Q/Z9OCndTAZsQ/s1600/300x100_dj_trans.png)
-   ワード、スプレッドシート、プレゼンテーション、お絵描き、方式計算、データベースを提供するオフィスアプリケーション群。110言語をサポートしており、Windows,
    Solaris, Linux, Macなどで利用可能

### [PhotArk](http://incubator.apache.org/photark/)

-    [![](http://2.bp.blogspot.com/-WcLpkztM85s/T6IXHryzmSI/AAAAAAAAQ-Y/o0009DmM_iQ/s1600/photark_logo_small_transparent.gif)](http://2.bp.blogspot.com/-WcLpkztM85s/T6IXHryzmSI/AAAAAAAAQ-Y/o0009DmM_iQ/s1600/photark_logo_small_transparent.gif)
-   ウェブでの写真閲覧アプリケーション

### [Release Audit Tool (RAT)](http://incubator.apache.org/rat/)

-   リリース時の監視ツール
-   Antと一緒にタスク管理を行う事も可能

### [S4 (Simple Scalable Streaming System)](http://incubator.apache.org/s4/)

-    [![](http://1.bp.blogspot.com/-VAsPtf1UkUw/T6IY5a1aFZI/AAAAAAAAQ-g/EwDalex_Bho/s1600/s4_test.png)](http://1.bp.blogspot.com/-VAsPtf1UkUw/T6IY5a1aFZI/AAAAAAAAQ-g/EwDalex_Bho/s1600/s4_test.png)
-   一般的なスケーラブルで耐障害性を兼ね備えたプラグイン形式の配信システム

### 

### [Spatial Information System (SIS)](http://incubator.apache.org/sis/)

-    [![](http://3.bp.blogspot.com/-uDk_JQ3KgJQ/T6IaK0h2H1I/AAAAAAAAQ-o/8BBykSHxKWI/s320/sis_logo_small.png){width="320"
    height="132"}](http://3.bp.blogspot.com/-uDk_JQ3KgJQ/T6IaK0h2H1I/AAAAAAAAQ-o/8BBykSHxKWI/s1600/sis_logo_small.png)
-   検索や、データクラスタリング、アーカイブ向けの分布フレームワーク

### [Stanbol](http://incubator.apache.org/stanbol/)

-    [![](http://3.bp.blogspot.com/-uPQrBsFTV4s/T6IamdN0gXI/AAAAAAAAQ-4/u-j8NSNFc9E/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+14.41.28%EF%BC%89.png)](http://3.bp.blogspot.com/-uPQrBsFTV4s/T6IamdN0gXI/AAAAAAAAQ-4/u-j8NSNFc9E/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+14.41.28%EF%BC%89.png)
-   CMS本体と再利用可能なモジュール群

### [Syncope](http://incubator.apache.org/syncope/)

-    [![](http://3.bp.blogspot.com/-Y8GjLNHtp5U/T6IbexkSOWI/AAAAAAAAQ_A/b_tMhZMaLdU/s1600/apache-syncope-logo-small.jpg)](http://3.bp.blogspot.com/-Y8GjLNHtp5U/T6IbexkSOWI/AAAAAAAAQ_A/b_tMhZMaLdU/s1600/apache-syncope-logo-small.jpg)
-   J2EE技術を取り入れたエンタープライズ環境の認証管理システム

### [ Tashi](http://incubator.apache.org/tashi/)

-   [![](http://1.bp.blogspot.com/-nA17ly0feC0/T6IcV4KAxUI/AAAAAAAAQ_I/g2q2I7INAlU/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+14.48.40%EF%BC%89.png)](http://1.bp.blogspot.com/-nA17ly0feC0/T6IcV4KAxUI/AAAAAAAAQ_I/g2q2I7INAlU/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+14.48.40%EF%BC%89.png)
-   ビッグデータを利用したクラウド向けのインフラソフト開発支援ツール

### [VCL(Virtual Computing Lab)](http://incubator.apache.org/vcl/)

-   実マシン上や、仮想マシンの上で、仮想マシンイメージを開発、調整、管理を行うフレームワーク

### [VXQuery (Versatile XQuery)](http://incubator.apache.org/vxquery/)

-   Javaに移植されたXMLクエリ処理

### [Wave](http://incubator.apache.org/wave/)

-   [![](http://3.bp.blogspot.com/-6e-itHwFbZg/T6Iea4V0A0I/AAAAAAAAQ_Q/pw2_mRJTXeg/s320/customLogo.gif){width="320"
    height="62"}](http://3.bp.blogspot.com/-6e-itHwFbZg/T6Iea4V0A0I/AAAAAAAAQ_Q/pw2_mRJTXeg/s1600/customLogo.gif)
-   Google WaveがOSSになった版。共同ドキュメント編集など共同作業ツール

### [ Wink](http://incubator.apache.org/wink/)

-    [![](http://2.bp.blogspot.com/-90zYo_1OS9w/T6Ifi3VYo1I/AAAAAAAAQ_Y/VFf52sRBMFE/s1600/wink2-s.png)](http://2.bp.blogspot.com/-90zYo_1OS9w/T6Ifi3VYo1I/AAAAAAAAQ_Y/VFf52sRBMFE/s1600/wink2-s.png)
-   RESTfulなウェブサービスを構築出来るフレームワーク（サーバーとクライアントを提供）

### [Wookie](http://incubator.apache.org/wookie/)

-    [![](http://3.bp.blogspot.com/-Hgya9tgUMUE/T6IhU_nK1BI/AAAAAAAAQ_g/krONS_1Az3A/s320/logo.png){width="320"
    height="91"}](http://3.bp.blogspot.com/-Hgya9tgUMUE/T6IhU_nK1BI/AAAAAAAAQ_g/krONS_1Az3A/s1600/logo.png)
-   自前アプリケーションにウィジェットをアップロード＆展開を行えるようにするJavaサーバーアプリケーション

### [Zeta Components](http://incubator.apache.org/zetacomponents/)

-    [![](http://3.bp.blogspot.com/-Dvg3w9UZd9k/T6Iih7VVLeI/AAAAAAAAQ_o/zXoNvSlrWTg/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+15.15.21%EF%BC%89.png)](http://3.bp.blogspot.com/-Dvg3w9UZd9k/T6Iih7VVLeI/AAAAAAAAQ_o/zXoNvSlrWTg/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-05-03+15.15.21%EF%BC%89.png)
-   高品質な疎結合されたPHP5コンポーネントライブラリ群

何か役に立ちそうなソフトや開発を手伝いたいのはありましたでしょうか！？







**No 車輪の再開発!**







新しい発見があるといいですね♪








