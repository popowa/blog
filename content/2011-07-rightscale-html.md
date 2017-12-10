Title: RightScaleを解き明かす\~クラウド登録、諸設定をしよう\~
Date: 2011-07-22 05:44
Authors: ayakomuro
Tags:  AWS, RightScale, RightScale解体新書
Slug:2011/07/rightscale
Status: published

時間が経ってしまいましたが、RightScale解体新書の続きを書きたいと思います！前回はRightScale登録でしたので、ログイン後のクラウド登録、諸設定を説明します。  

  
[]  

-   ダッシュボード日本語化
-   クラウド追加(AWS)
-   セキュリティグループ設定
-   credentialsの設定

  
  

### ◆ダッシュボード日本語化

  
アカウント作成後、ログインをするとダッシュボードに遷移します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/login1-300x106.png "login1"){.alignnone
.size-medium .wp-image-1168 width="300"
height="106"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/login1.png)  
  
最初は英語表示なので、左下にある言語選択プルダウンから日本語を選びます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/login2.png "login2"){.alignnone
.size-full .wp-image-1169 width="170"
height="97"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/login2.png)  
  
選択をすると、自動でリロードし、ダッシュボードが日本語化します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/login3-300x85.png "login3"){.alignnone
.size-medium .wp-image-1170 width="300"
height="85"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/login3.png)  
  

◆クラウドを紐付ける
-------------------

  
ダッシュボードにある「Add one or more clouds to your
account」をクリックするか  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/addcloud1.png "addcloud1"){.alignnone
.size-full .wp-image-1172 width="266"
height="46"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/addcloud1.png)  
  
[](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/addcloud1.png)メニューにある「クラウド」-\>
「クラウドを追加する」 をクリックするか  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/addcloud2.png "addcloud2"){.alignnone
.size-full .wp-image-1173 width="110"
height="83"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/addcloud2.png)  
  
「設定」-\> 「アカウントの設定」-\> 「クラウド」をクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/addcloud3.png "addcloud3"){.alignnone
.size-full .wp-image-1174 width="271"
height="195"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/addcloud3.png)  
  
AWSのアイコン、もしくはRackspaceのアイコン、プライベートクラウドの選択が出てくるので、そこでAWSアイコンを押します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/enteraws-300x153.png "enteraws"){.alignnone
.size-medium .wp-image-1181 width="300"
height="153"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/enteraws.png)  
  
AWSのIAMでRightScale用のアカウントを作成しておきます。  
=\>IAMでのアカウント作成方法はこちらをご覧ください。「[RightScaleを解き明かす\~RightScale用のAWS
アカウントをIAMを使って作ろう\~](http://www.popowa.com/archives/1183 "RightScaleを解き明かす~RightScale用のAWS アカウントをIAMを使って作ろう~")」  
  
手元に  
  

> "User Name","Access Key Id","Secret Access
> Key"\"RightScale\_Aya","AKxxxxxxxx","\$MxSkxxxxxxxxxxxxxx"

  
があると思うので、上記枠に追加します。AWS Account
Numberはアカウントページの右上に表示される番号です。  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_account_num.png "aws_account_num"){.alignnone
.size-full .wp-image-1196 width="209"
height="42"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_account_num.png)  
  
情報を追加後、RightScaleがAPI経由で設定を取得しに行きます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_adding_aws-300x114.png "rs_adding_aws"){.alignnone
.size-medium .wp-image-1197 width="300"
height="114"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_adding_aws.png)  
  
RightScaleはSSHの公開鍵、秘密鍵両方を保持します（過去にAWSで作ったSSHに関しては、RightScaleは秘密鍵を持っていないので、実質新しく作り直した方がいいと思います。それか後ほど秘密鍵をRightScale側に寄せる、が出来ると思います。）  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_adding_aws_ssh-300x134.png "rs_adding_aws_ssh"){.alignnone
.size-medium .wp-image-1200 width="300"
height="134"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_adding_aws_ssh.png)  
  
Security Group
Setupで、AWSのセキュリティグループの設定の変更が行われます。これはディフォルトのセキュリティグループに22(ssh)と80(http)のポートを開ける設定を行います。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_adding_aws_port-300x128.png "rs_adding_aws_port"){.alignnone
.size-medium .wp-image-1199 width="300"
height="128"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_adding_aws_port.png)  
  
クラウドが追加されました！  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_adding_aws_done-300x154.png "rs_adding_aws_done"){.alignnone
.size-medium .wp-image-1198 width="300"
height="154"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_adding_aws_done.png)  
  
   
  

◆セキュリティグループ設定
-------------------------

  
先ほど22/80ポートを開けましたが、もし開くのを忘れたら、「クラウド」-\>
使いたいリージョンの「EC2 セキュリティグループ」を選択します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_setting_1-300x147.png "rs_setting_1"){.alignnone
.size-medium .wp-image-1202 width="300"
height="147"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_setting_1.png)  
  
ディフォルトのセキュリティグループはこんな感じになっていると思います（22/80ポートも開いているでしょう）。最初は22/25/53/80が開いていればいいと思います。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_setting_2-300x81.png "rs_setting_2"){.alignnone
.size-medium .wp-image-1203 width="300"
height="81"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_setting_2.png)  
  
もしポートが開いていなかったら以下の方法で設定します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_setting_4-300x125.png "rs_setting_4"){.alignnone
.size-medium .wp-image-1205 width="300"
height="125"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_setting_4.png)  
  
Add IPs: tcp Ports: \[開始ポート番号\] .. \[ 終了ポート番号\] IPs:
\[0.0.0.0/0\]とするとすべてのリクエストに対して指定したポートを開く事になります。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_open_port-300x22.png "rs_open_port"){.alignnone
.size-medium .wp-image-1201 width="300"
height="22"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_open_port.png)  
  
   
  

◆credentialsの設定
------------------

  
credentialsとはAWSなどで利用するIAMアカウントの番号や秘密鍵、などを保存しておく場所です。  
  
イメージとしてはある案件でS3にバックアップを取りたいので、S3のみアクセスが可能な権限を持ったアカウントをIAMで作成し、このcredentialsにS3\_ONLY\_USER/S3\_ONLY\_PASSという変数名で保存しておく事で、案件（デプロイメント）で再利用出来ますし、複数のサーバで利用していたとしても、credentialsで変更を行う事で、利用サーバで設定が反映されます。  
  
「デザイン」-\> 「証明書」をクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_credentials.png "rs_credentials"){.alignnone
.size-full .wp-image-1208 width="239"
height="206"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_credentials.png)  
  
「New credentials」をクリックします。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_cerdentials_add.png "rs_cerdentials_add"){.alignnone
.size-full .wp-image-1207 width="139"
height="77"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_cerdentials_add.png)  
  
Access Key IdやSecret Key をいれます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_credentials_example-300x151.png "rs_credentials_example"){.alignnone
.size-medium .wp-image-1209 width="300"
height="151"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/rs_credentials_example.png)  
  
 
