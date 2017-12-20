Title: 
Date: 2011-07-27 11:00
Authors: ayakomuro
Tags:  AWS, RightScale, RightScale解体新書
Slug:2011/07/rightscale_4942
Status: published


げてみよう\~+クラウドの追加、諸設定が終わったので、サーバーテンプレートを取り込んで、サーバを立ち上げます。このページでは、サーバーテンプレートの動き、とどのようにサーバーを立ち上げるスクリプトが機能するかを見て行きたいと思います。  
  
[]  

-   デプロイメントを作成する
-   サーバーテンプレートを持ってくる
-   サーバーテンプレートの諸設定する
-   サーバーテンプレートで使うバケット、ファイルの用意をする
-   サーバーテンプレートをデプロイメントに追加する
-   サーバーを立てる

  
  

◆デプロイメントを作成する
-------------------------

  
まず、「管理」-\>
「デプロイメント」の横にある「新規追加」をクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/depoyment_1.png "depoyment_1"){.alignnone
.size-full .wp-image-1219 width="205"
height="86"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/depoyment_1.png)  
  
Nickname:  デプロイメントの名前です（後で変えられます）  
Description:　説明文  
Default Availability
Zone:　ディフォルトのアベイラビリティゾーン（これはサーバーレベルで上書きする事が出来ます。）  
Default Placement Group:
 こちらは通常利用しないと思います（多分何も出てないかと）  
これはCCI (クラスターコンピューティングインスタンス）をHPC(AWS High
Performance Computing)として利用時に使う場所です。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/depoyment_2-300x186.png "depoyment_2"){.alignnone
.size-medium .wp-image-1220 width="300"
height="186"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/depoyment_2.png)  
  
「Save」をすると作成したデプロイメントのページに遷移します。先ほど入力した内容を変えたい場合は、「edit」をクリックして編集します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/deployment_3-300x288.png "deployment_3"){.alignnone
.size-medium .wp-image-1221 width="300"
height="288"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/deployment_3.png)  
  
デプロイメントのページには  
  
**インフォメーション、サーバ、入力、監視、スクリプト、ボリューム、アラート、監視エントリ、履歴、変更**  
  
というタブがあります。これは後ほど説明したいと思います。  
  

◆サーバーテンプレートを持ってくる
---------------------------------

  
メニューバーの「デザイン」-\> 「MultiCloud
Maketplace」の下にある「サーバテンプレート」を選択します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_1-300x68.png "ss_1"){.alignnone
.size-medium .wp-image-1222 width="300"
height="68"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_1.png)  
  
サーバーテンプレートのページへ遷移します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_2-300x117.png "ss_2"){.alignnone
.size-medium .wp-image-1223 width="300"
height="117"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ss_2.png)  
  
サーバーテンプレートのページの見方については  
\>\> [RightScaleを解き明かす\~　サーバーテンプレートのページの見方\~](http://www.popowa.com/archives/1225 "RightScaleを解き明かす~サーバーテンプレートのページの見方~")  
をご覧ください。  
  
今回は@[pinkguinness](http://twitter.com/pinkguinness)さんが作られた  
\>\> [LAMP All-In-One with wordpress JP- 11H1  
](http://www.rightscale.com/library/server_templates/LAMP-All-In-One-with-wordpress/20568)を取り込みたいと思います。  
  
対象サーバテンプレートのページを開いた後、右側にある「Import」をクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/import-300x57.png "import"){.alignnone
.size-medium .wp-image-1244 width="300"
height="57"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/import.png)  
  
するとマルチクラウド・マーケットプレイスからサーバテンプレートを取り込みます。  
イメージ的に説明すると、本屋にある雑誌を１部、自分の本棚に入れる感じです（無償、有償関わらず）  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/imported-300x108.png "imported"){.alignnone
.size-medium .wp-image-1245 width="300"
height="108"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/imported.png)  
  
[](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/imported.png)そしてその後「Clone」で、複製を作成します。  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/clone.png "clone"){.alignnone
.size-full .wp-image-1246 width="62"
height="28"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/clone.png)  
これはなぜ複製を作るかというと、今後自分なりにカスタマイズすると思うのですが、
その時に元のサーバテンプレートに戻りたいときがあるかもしれません。その時に戻れなくもないですが、今まで作業した内容も保持していたい場合、複製を作っておくと両方見る事が出来る為、便利です。しなくてもいいですが、した方がいいと思います。  
  

> Your cloned ServerTemplate will have its usage reported to
> RightScale.  
> ライトスケールに複製したサーバテンプレート情報を通知しました。  
> ServerTemplate successfully cloned and shown below. Click \'Edit\' to
> change it.  
> サーバテンプレートは以下の通り複製に成功しました。「Edit」をクリックして変更してください。

  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/cloned-300x46.png "cloned"){.alignnone
.size-medium .wp-image-1247 width="300"
height="46"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/cloned.png)  
  
この複製を取ったのは先ほどのイメージで言うと自分の本棚に、同じ本をもう一つ作った事になります。  
タイトルも、「LAMP All-In-One with wordpress JP- 11H1
v1 」と「v1」が付いています。  
  

◆サーバーテンプレートの諸設定する
---------------------------------

  
サーバテンプレートの設定に関しては  
\>\>
[RightScaleを解き明かす\~サーバテンプレートの諸設定をしよう\~](http://www.popowa.com/archives/1258 "RightScaleを解き明かす~サーバテンプレートの諸設定をしよう~")  
をご覧ください。  
  

◆サーバーテンプレートで使うバケット、ファイルの用意をする
---------------------------------------------------------

  
例えば\>\> [LAMP All-In-One with wordpress JP-
11H1](http://www.rightscale.com/library/server_templates/LAMP-All-In-One-with-wordpress/20568)
ではwordpressのファイルをzipファイルにしてS3に置いてあり、サーバを起動させる時に、S3から持って来て、展開するようになっています（これはRightScaleでは一般的なデプロイの仕方です）。  
  
なので、まずS3のバケットを作りましょう。デスクトップアプリで簡単なのはCyberduckとかが使い易いと思います。  
\>\>
[CyberduckでAWSのS3を使う方法(英語）](http://trac.cyberduck.ch/wiki/help/en/howto/s3)  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/s3.png "s3"){.alignnone
.size-full .wp-image-1288 width="463"
height="67"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/s3.png)  
  
   
  

◆サーバーテンプレートをデプロイメントに追加する
-----------------------------------------------

  
諸設定をしたサーバテンプレートをデプロイメントに取り込みます。自分の本棚にあった設定済みの本を取り出して、実際に実行させる、というイメージでしょうか。  
  
対象のサーバテンプレートのページで、「Add to
Deployment」をクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/add2deployment.png "add2deployment"){.alignnone
.size-full .wp-image-1279 width="140"
height="30"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/add2deployment.png)  
  
クリックすると、どのリージョンに立てるか、選択する事が出来ます。今回はシンガポールで立てたいと思います。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/add_cloud.png "add_cloud"){.alignnone
.size-full .wp-image-1278 width="426"
height="145"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/add_cloud.png)  
  
   
  
リージョンを設定した後、詳細の設定を行います。  

-   Deployment: 展開をするデプロイメントを選択します
-   ServerTemplate:
    利用するサーバテンプレートのリビジョンを選択します（通常はHEADになります。
-   Cloud: 先ほど選択したリージョン
-   Multicloud Image: 利用するサーバイメージ  
   Inherit from ServerTemplate -\>
    サーバテンプレートでディフォルトで設定されているサーバを利用。それ以外は指定のサーバイメージを選択する
-   Nickname: サーバ構成の名前（後で変えられます）
-   Instance Type:
    インスタンスのタイプを選択出来ます。時々マイクロインスタンスが使える、と出ていますが、使えない場合があります。確実に使えるのはスモール以上の場合が多いです。
-   SSH Key: 利用するSSHの鍵
-   Security Group(s) ：利用するセキュリティグループ
-   Availability Zone: 利用するゾーン
-   Elastic IP : 固定IPを使うか
-   Associate IP at Launch ? :
    固定IPを利用する場合、構成に紐付けるかどうかを選択出来ます。Elastic
    IPを利用しない、にしていたならばチェックをいれていても何も起こりません。

  
   
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/add_deployment.png "add_deployment"){.alignnone
.size-full .wp-image-1289 width="385"
height="376"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/add_deployment.png)  
  
デプロイメントに追加出来ました！しかしまだ起動してません。CPUの所が赤になっているのは、停止している（もしくは起動してない）という意味です。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/added.png "added"){.alignnone
.size-full .wp-image-1283 width="565"
height="64"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/added.png)  
  

◆サーバーを立てる
-----------------

  
サーバを立てます。青いボタンをクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/start.png "start"){.alignnone
.size-full .wp-image-1284 width="29"
height="28"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/start.png)  
  
入力で足りない分は赤い色で表示されます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/start_line.png "start_line"){.alignnone
.size-full .wp-image-1285 width="471"
height="59"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/start_line.png)  
  
WEBSITE\_DNSが未入力でした。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/missing.png "missing"){.alignnone
.size-full .wp-image-1286 width="341"
height="70"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/missing.png)  
  
[](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/missing.png)未入力部分を入力して、「Launch」、もしくは「Save
and Lauch」します。  
  
起動が開始するとCPUの部分が黄色の↑に変わり、状態がpendingに変わります。またサーバ構成の上に想定金額が表示されます。  
  
CPU  

-   Stop　：赤い■
-   Pending：黄色い↑
-   Booting：緑の↑
-   operational: 緑の■

  
IPを取得したらパブリックIPの所に、IPアドレスが表示されます。  
  
アクションの部分には  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ssh.png "ssh"){.alignnone
.size-full .wp-image-1292 width="24"
height="23"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ssh.png)：ssh  
  
SSHアイコンをクリックすると、SSHコンソールをブラウザー越しに起動してくれてデスクトップに入っているコンソールでSSHにログインした状態にしてくれます。  
  
RightScaleからのアクセスを許可します。  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ssh_access-300x114.png "ssh_access"){.alignnone
.size-medium .wp-image-1294 width="300" height="114"}  
](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ssh_access.png)  
  
ウィンドウが1つ立ち上がり、どのコンソールを立ち上げるか聞いてきます（midtermかopenssh)　Mac
OS Xについているコンソールに慣れているので、OpenSSHをクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ssh_which-300x100.png "ssh_which"){.alignnone
.size-medium .wp-image-1295 width="300"
height="100"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/ssh_which.png)  
  
そうするとコンソールが立ち上がって（初めての場合はyesと入れる必要があるかもしれません）、サーバにはいる事が出来ます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/console-300x256.jpg "console"){.alignnone
.size-medium .wp-image-1296 width="300"
height="256"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/console.jpg)  
  
   
  
起動/設定には時間がかかるので、AWS側のマネージメントコンソールを見て、実際に起動しているかどうか見ると良いかもしれません。  
  
↓Runningになってますね。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws-300x10.jpg "aws"){.alignnone
.size-medium .wp-image-1291 width="300"
height="10"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws.jpg)  
  
RightScaleのコンソールに戻り、パブリックIPをコピペして、ブラウザーのアドレスバーに貼付けます。  
  
Wordpressが立ち上がっていました！　もしサーバテンプレートで指定した「APPLICATION\_CODE\_PACKAGE」で指定したzipファイルが、インストール前にパッケージだったら、インストール画面が出てインストールを行う必要があります（3ページぐらいです）  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/wordpress.png "wordpress"){.alignnone
.size-full .wp-image-1298 width="269"
height="174"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/wordpress.png)  
  
   
  
 
