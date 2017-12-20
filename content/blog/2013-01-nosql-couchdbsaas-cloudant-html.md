Title: 
Date: 2013-01-04 23:21
Authors: ayakomuro
Tags:  CouchDB, NoSQL
Slug:2013/01/nosql-couchdbsaas-cloudant
Status: published


Cloudant+Cloudantという製品について調べてみた。

-   製品名: Cloudant
-   URL: <https://cloudant.com/>

[![](http://4.bp.blogspot.com/-IcijgudRNIs/UOdkhR19IQI/AAAAAAAAV-E/vkOt1dK9S6w/s1600/cloudant_logo.jpg)](http://4.bp.blogspot.com/-IcijgudRNIs/UOdkhR19IQI/AAAAAAAAV-E/vkOt1dK9S6w/s1600/cloudant_logo.jpg)







### 要約



> **CouchDBをサービスとして色んなクラウド上で展開出来るSaaS  
> 自分でCouchDBをインストール＆設定、冗長化をしたく無い人にはぴったりのサービス。** 

> **CouchDBのコミッターも多いらしいので、ほぼCouchDBと同じ機能だと考えてOK** 





[]



### 概要



-   

    Cloudantは [Apache
    CouchDB](http://couchdb.apache.org/)で構築されている

    

    

    CouchDB: JSON形式のドキュメントでデータ保存、返却をするNoSQL

    

    

    

-   Data Layer as a Service(DLAAS?)
-   

### 機能について

-   より深い解析: MapReduce機能
-   全文検索:
    [Lucene](http://lucene.apache.org/core/)互換のインデックス機能
-   データ・レプリケーション: 非同期な処理や接続が断たれた場合も対応可能
-   各CloudantドキュメントにはユニークなID(\"\_id\")が付いてい
-   ドキュメントの値は、数字、文字列、Boolans、オブジェクト、配列、添付(ビデオ、イメージ、それ以外も）
-   ドキュメントのサイズに制限はない
-   HTTP経由でRESTfulなAPIでアクセスが可能
-   データベースのインデックスはMapReduce機能を使って構築されているので、クエリー処理や解析が素早く行なえる



### 冗長性・インフラについて





[![](http://4.bp.blogspot.com/-Rd2IQpplD8w/UOdjEbcDvUI/AAAAAAAAV9o/-_p0xVJ7F7s/s320/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2013-01-02+19.44.20.png){width="320"
height="89"}](http://4.bp.blogspot.com/-Rd2IQpplD8w/UOdjEbcDvUI/AAAAAAAAV9o/-_p0xVJ7F7s/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2013-01-02+19.44.20.png)

-   Cloudantではメインのクラウドをどの物理プラットフォームを使うか、どのリージョンで使うかを選択する
-   選べるクラウド（リージョン）：SoftLayer/Windows
    Azure/AWS/Rackspace/Joyent
-   Cloudantは自動で全世界でレプリケーションを行なう（エンドユーザーから見るとレイテンシーが低い）
-   Cloudantはクラスターサーバ（ノード）間で分割して保存する。データ分散がされている





### サービス特有の内容



-   マルチテナントが嫌な場合は専有テナントもあり
-   平行クラスター・フレームワークをErlangで開発
-   ノードサーバにデータを増やす機能、なので作った（CouchDBに無いらしい？？）

[![](http://4.bp.blogspot.com/-9s78y4WZjV8/UOQMD1w4-eI/AAAAAAAAV74/stEW20vem3U/s1600/cloudant.png)](http://4.bp.blogspot.com/-9s78y4WZjV8/UOQMD1w4-eI/AAAAAAAAV74/stEW20vem3U/s1600/cloudant.png)











Cloudantスケール機能の勘所





-   読み込みのロード時間 vs 書き込みのロード時間
-   単純なドキュメントがどのぐらいクエリーが発生するのか
    vs複雑なMapReduceなクエリーが全ノード間で発生するのか
-   ディスク浸達性
-   キャッシュ利用
-   CPUコア利用









コマンドラインで操作

-   [\[Cloudant\]コマンドラインで操作 ](http://d.hatena.ne.jp/popowa/20130103#1357197178)
-   [\[Cloudant\]プライマリ・インデックス](http://d.hatena.ne.jp/popowa/20130104#1357256329)
-   [\[Cloudant\]セカンダリー・インデックス](http://d.hatena.ne.jp/popowa/20130105#1357334012)





ここまで調べておいて、CouchDBを調べた方がよく分かると思ったのは内緒だ。


