Title: 
Date: 2011-05-29 05:46
Authors: ayakomuro
Tags:  AWS, Rackspace, RightScale, RightScale解体新書
Slug:2011/05/rightscale_29
Status: published


〜連携させるクラウドアカウントを作ってみよう〜+それでは実践に入っていきたいと思います。RightScaleは管理ツールなので、管理するクラウド（パブリック、プライベート）のアカウントを作る必要があります。  
  
[]  
  
RightScale上で個々のクラウドに自動でアカウント作成が行われる訳ではありません。  
  
流れとしては  

1.  クラウド契約する
2.  クラウドでのAPI情報を取得
3.  RightScaleにログインして、クラウド追加
4.  有効化されて、RightScaleでも扱えるようになる

  
となっています。  
  
まずは定番のAmazon Web Servicesにアカウントを作ってみましょう。  
  
AWSのアカウント作成方法については沢山のブログや記事が出ているのでろのリンク集を載せたいと思います。  

-   【参考資料】 AWS アカウント登録方法[Amazon EC2
    を利用する際のアカウント登録方法](http://jaws-ug.jp/documents/j5f69c)
-   AWS: [はじめてのアマゾンクラウド①\[Amazon Web
    Services(AWS)のアカウントを開設する\]](http://www.slideshare.net/kentamagawa/3aws)
-   incharge.jp [利用方法（AWSアカウント作成からEC2登録まで）](http://www.incharge.jp/howtiuse)
-   [AWS ことはじめ
    ーアカウント作成編ー](http://circular-image.com/archives/1)
-   [はじめてのアマゾンクラウド①\[Amazon Web
    Services(AWS)のアカウントを開設する\]](http://www.slideshare.net/kentamagawa/3aws)

  
※AWSに関しては最初クレジットカードを入れなくてもアカウントが出来ますが、一番最初にサービスを使う時にカード入力を求められるので、それも済ましておきましょう。  
  
AWSと並んで人気なのはRackspaceです。Rackspaceのアカウントの作り方は【[RackspaceでのAccount
Activation](http://d.hatena.ne.jp/popowa/20110121/1295641485)】をご覧ください。  
  
クラウドのアカウントが出来たらクラウドが提供しているAPI情報を取得しておきます。  
  

AWSの場合
---------

  
  

### マネージメントコンソール以外で作成する場合

  
※以下の方法で【アクセスキーを作成する】というリンクが出なければ、【IAMから作る】をご確認ください。  

1.  [http://aws.amazon.com/jp/](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws1.png)の右端にある【Account　もしくは
    アカウント】をクリックします[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws1.png "aws1"){.alignnone
    .size-full .wp-image-928 width="150"
    height="53"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws1.png)
2.  するとアカウントに関するメニューが出てくるので、【セキュリティ証明書　】をクリックします  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws2-300x111.png "aws2"){.alignnone
    .size-medium .wp-image-929 width="300"
    height="111"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws2.png)
3.  セキュリティ証明書のページに遷移したら右上に載っている【口座番号】をメモしておきます。こんな感じです(数字です)-\>
    XXXX-XXXX-XXXX  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws3.png "aws3"){.alignnone
    .size-full .wp-image-930 width="216"
    height="57"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws3.png)
4.  次はページ真ん中あたりで【アクセス証明書】を探します。  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws4-300x252.png "aws4"){.alignnone
    .size-medium .wp-image-931 width="300"
    height="252"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws4.png)
5.  （上記の図には表示されていませんが）【アクセスキーを作成する】というリンクが出ていたら、クリックする事でアクセスキーを作る事が出来ます。
6.  アクセスキーIDとシークレットアクセスキーというのが出てくるので、それをメモしておきます。

  
  

### IAMからアクセスキーを作成する方法

  

1.  AWSのマネージメントコンソールにログインしタブの一番右端にある【IAM】<https://console.aws.amazon.com/iam/home>
    にアクセスします。  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws5.png "aws5"){.alignnone
    .size-full .wp-image-932 width="119"
    height="57"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws5.png)
2.  ナビゲーションにある【Users】をクリックします。  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws6.png "aws6"){.alignnone
    .size-full .wp-image-937 width="168"
    height="148"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws6.png)
3.  IAMのユーザーダッシュボードが表示されます。【Create New
    Users】をクリックします。  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws7.png "aws7"){.alignnone
    .size-full .wp-image-936 width="157"
    height="86"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws7.png)
4.  ポップアップが出てくるので、ユーザー名を入力します。[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws8-300x118.png "aws8"){.alignnone
    .size-medium .wp-image-935 width="300"
    height="118"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws8.png)
5.  最初は１アカウントしかないと思うので【Generate an access key for
    each User】にチェックをいれておきます[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws9-300x29.png "aws9"){.alignnone
    .size-medium .wp-image-934 width="300"
    height="29"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws9.png)
6.  ユーザー作成と共に、アクセスキーが出来ました。【アクセスキー】と【シークレットアクセスキー】が表示されるので、メモしておきます。【Download
    Credential】をクリックする事で【credentials.csv】という形式でダウンロードする事も可能です。[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws10-300x143.png "aws10"){.alignnone
    .size-medium .wp-image-933 width="300"
    height="143"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws10.png)
7.  ユーザーが出来たら次は【ナビゲーション】から【Groups】を選択します。  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws11.png "aws11"){.alignnone
    .size-full .wp-image-948 width="160"
    height="106"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws11.png)
8.  Groupsのダッシュボードで【Create New Group　】をクリックします[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws12.png "aws12"){.alignnone
    .size-full .wp-image-947 width="142"
    height="59"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws12.png)
9.  ポップアップが出てくるので【Group Name】の所の任意の名前を入れます[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws13-300x141.png "aws13"){.alignnone
    .size-medium .wp-image-946 width="300"
    height="141"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws13.png)
10. 次のページで権限を選択する箇所が出るので、【Power User
    Access】をクリックします[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws14-300x30.png "aws14"){.alignnone
    .size-medium .wp-image-945 width="300"
    height="30"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws14.png)
11. 追加の権限設定のフィールドが出てきますが、そのまま次へ進みます。[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws15-300x235.png "aws15"){.alignnone
    .size-medium .wp-image-944 width="300"
    height="235"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws15.png)
12. 確認します[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws16-300x83.png "aws16"){.alignnone
    .size-medium .wp-image-943 width="300"
    height="83"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws16.png)
13. Groupのダッシュボードに戻った後、先ほど作ったGroupのチェックボックスを入れます。右下の枠に詳細が表示されるので、【Add
    users to Group】を選択します[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws17-300x171.png "aws17"){.alignnone
    .size-medium .wp-image-942 width="300"
    height="171"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws17.png)
14. またポップアップが出るので、そこで【Users】で追加したユーザーを選択します。[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws18-300x116.png "aws18"){.alignnone
    .size-medium .wp-image-941 width="300"
    height="116"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws18.png)
15. 【Group】のダッシュボードに遷移し、GroupにUserが紐づいた情報が表示されます。[  
   ![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws19-300x100.png "aws19"){.alignnone
    .size-medium .wp-image-940 width="300"
    height="100"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/aws19.png)

  
   
  

Rackspaceの場合
---------------

  

1.  右上にある【Customer Login】から【 Cloud Control
    Panel】をクリックします。  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs1.png "rs1"){.alignnone
    .size-full .wp-image-957 width="217"
    height="76"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs1.png)
2.  ログイン画面に遷移するので、ログインします。  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs2-300x225.png "rs2"){.alignnone
    .size-medium .wp-image-956 width="300"
    height="225"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs2.png)
3.  左側にあるナビゲーションから【 Your
    Account　】をクリックすると、アカウント関連のメニューが表示されるので【
    API Access 】をクリックします。  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs3-120x300.png "rs3"){.alignnone
    .size-medium .wp-image-955 width="120"
    height="300"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs3.png)
4.  右側に詳細が表示されるので、　APIキーが作成されていなかったら【
    Generate API key 】をクリックする  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs4.png "rs4"){.alignnone
    .size-full .wp-image-954 width="176"
    height="52"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs4.png)
5.  id/pwが表示されるのでメモしておく  
   [![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs5-300x47.png "rs5"){.alignnone
    .size-medium .wp-image-953 width="300"
    height="47"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/05/rs5.png)
