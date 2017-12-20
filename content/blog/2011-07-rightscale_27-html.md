Title: RightScaleを解き明かす\~サーバーテンプレートのページの見方\~
Date: 2011-07-26 15:49
Authors: ayakomuro
Tags:  RightScale解体新書
Slug:2011/07/rightscale_27
Status: published

RightScaleの醍醐味であるサーバーテンプレートですが、そのダッシュボード（マルチクラウド・マーケットプレイス・サーバーテンプレート）は最初どう使っていいのか迷う場合があります。そこでサーバーテンプレートのマーケットプレイスの使い方を説明します。  

  
[]「デザイン」-\> 「MultiCloud
Marketplace」の配下にある「サーバーテンプレート」をクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_2-300x117.png "ss_2"){.alignnone
.size-medium .wp-image-1223 width="300"
height="117"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_2.png)  
  
左側にあるメニューから説明します。  
  

Browse
------

  
   
  
現在選択してるものが太文字になって表示されます。「サーバテンプレート」を選択しているので「ServerTemplates」が太文字になって表示されています。右側のコンテンツにはサーバテンプレートが表示されていると思います。  

-   ServerTemplates (サーバテンプレート)
-   RightScripts　（ライトスクリプト）
-   MultiCloud Images　（マルチクラウドイメージ）
-   Macros　（マクロ）

  
![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/browse.png "browse"){.size-full
.wp-image-1226 .alignnone width="205" height="149"}  
  

Search
------

  
上記Browseで選択したスクリプトの種類の中を様々な条件で検索します。  
  
ディフォルト  

-   Keyword(s) : キーワード
-   Search in (Title / Title & Description / Publisher) :
    キーワードをどこで検索するか（タイトル/タイトル＆説明文/作成者名）

  
「Show advanced options」をクリックすると、オプションが表示されます。  
  
オプション  

-   Price (Any / Free / Paid) : プライス（なんでも/無償/有償）
-   Category：カテゴリ（以下を参照）
-   Cloud (AWS, Rackspace, Eucalyptus,CloudStack,OpenStack) :
    使えるクラウド
-   Sort by (Newest First / Oldest First / Title / Rating) :
    ソート順（新しい、古い、タイトル、レート）

  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/search-146x300.png "search"){.alignnone
.size-medium .wp-image-1227 width="146"
height="300"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/search.png)  
  

Categories
----------

  
選択したカテゴリーのスクリプトを表示します。全部使った事が無いので、今度個々のカテゴリを調べてどのようなサーバテンプレートがあるか記事を書きたいと思います。一つのサーバテンプレートには何個かカテゴリーを登録する事が出来るので、例えばAll-In-Oneと、11H1
Compatibleと、Application Server,
Blogに引っかかるサーバテンプレートもあります。  

-   All　：　全部のサーバテンプレート
-   Shared
     ：シェアは、他のRightScaleユーザーが自分にシェアしてくれたサーバテンプレートが表示されます。これはSharing
    Groups（シェアリンググループ）を使って共有されたものになります。この機能はプレミアムとエンタープライズエディションを使っているユーザーのみ利用出来ます
    X(
-   11H1 Compatible :  これは2011年のHalf
    1（上半期）のRightScaleが提供するイメージに対応しているサーバテンプレート、という意味です。11H2だと2011年下半期、12H1は2012年上半期\...になります。
-   All-In-One　：　オールインワン。文字のごとく、すべてが1つのインスタンスに入る設定になっているサーバテンプレート
-   Application Server
-   Blog
-   Business Intelligence
-   Cache Server
-   Chef
-   Content Management
-   Database
-   Distributed Processing
-   Filesystem
-   Load Balancer
-   Monitoring
-   Security
-   Testing and Development
-   Toolbox
-   Tutorial
-   VM Image Tools
-   Web Server
-   Windows

  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/categories.png "categories"){.alignnone
.size-full .wp-image-1230 width="209"
height="131"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/categories.png)  
  

- 右側のメインコンテンツ -
--------------------------

  
  

Featured ServerTemplate
-----------------------

  
RightScaleお勧めのサーバテンプレートが表示されます。ここに表示するには多分RightScaleにお金を出さないといけないのかな？と個人的には思っていますが、真相はいかに。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/featuredserver-300x116.png "featuredserver"){.alignnone
.size-medium .wp-image-1233 width="300"
height="116"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/featuredserver.png)  
  

Highest Rated / Recently Added / Featured \-- View All
------------------------------------------------------

  
レートが高いもの、最近追加された物、特集、すべて見るというタブで簡単にサーバテンプレートを表示させる事が出来ます。レーティングに関してはまだあまり投票が行われていないので、これから、になると思います。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/hrfa-300x19.png "hrfa"){.alignnone
.size-medium .wp-image-1234 width="300"
height="19"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/hrfa.png)  
  

選択したサーバテンプレート
--------------------------

  
以下のサーバテンプレートはログがないですが、ロゴ、タイトル、作成者、対応しているクラウドのアイコン、（あれば）有償のアイコンが表示されています。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_ja-300x58.png "ss_ja"){.alignnone
.size-medium .wp-image-1235 width="300"
height="58"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_ja.png)  
  
アイコンの説明  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_aws.png "ss_aws"){.alignnone
.size-full .wp-image-1236 width="24"
height="23"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_aws.png)
：AWS対応している  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_rs.png "ss_rs"){.alignnone
.size-full .wp-image-1239 width="21"
height="23"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_rs.png)；Rackspace対応している  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_cc.png "ss_cc"){.alignnone
.size-full .wp-image-1237 width="24"
height="22"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_cc.png)：Eucalyptusもしくは、CloudStack対応、OpenStack対応している  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_price.png "ss_price"){.alignnone
.size-full .wp-image-1238 width="16"
height="23"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_price.png)：有償（無償であればアイコンは出ない）  
  
 
