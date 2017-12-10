Title: 
Date: 2011-07-22 04:59
Authors: ayakomuro
Tags:  AWS, RightScale, RightScale解体新書
Slug:2011/07/rightscalerightscaleaws-iam
Status: published


アカウントをIAMを使って作ろう\~+RightScaleはAWSのAPIを使ってクラウドを操作するのですが、IAMが出来たため、通常の方法でAPI用のアカウントを作れなくなりました。IAMからRightScale用のアカウントを作成する方法を記述します。  
  
[][AWSのマネージメントコンソール](https://console.aws.amazon.com/iam/home)にログインします。IAMのタブをクリックします。  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_iam.png "aws_iam"){.alignnone
.size-full .wp-image-1184 width="207"
height="71"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_iam.png)  
  
[](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_iam.png)ユーザーを作成します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_1.png "aws_1"){.alignnone
.size-full .wp-image-1178 width="132"
height="57"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_1.png)  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_user_2-300x192.png "aws_create_user_2"){.alignnone
.size-medium .wp-image-1185 width="300"
height="192"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_user_2.png)  
  
名前を入力する所が出てくるので、分かり易い名前にします。「Generate an
access key for each
User」にチェックをつけておきます（これはチェックがなくてもいいですが、面倒でも個別管理しておいた方が後々ユーザー管理をきちんとする上ではいいと思います）。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_2-300x87.png "aws_2"){.alignnone
.size-medium .wp-image-1179 width="300"
height="87"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_2.png)  
  
作成すると公開鍵と、秘密鍵の値をcsvとしてダウンロード出来るようになります。ファイルの中身はこんな風になっています。  
  

> \"User Name\",\"Access Key Id\",\"Secret Access
> Key\"\"RightScale\_Aya\",\"AKxxxxxxxx\",\"\$MxSkxxxxxxxxxxxxxx\"

  
※
次はオプションです。しなくてもいいです。グループを作らない場合は、ユーザーに対して権限を設定する必要があります。※  
グループを作成します。  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group.png "aws_create_group"){.alignnone
.size-full .wp-image-1186 width="139"
height="58"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group.png)  
  
グループ名を入力します。  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_2-300x119.png "aws_create_group_2"){.alignnone
.size-medium .wp-image-1187 width="300"
height="119"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_2.png)  
  
[](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_2.png)権限一覧が出ます。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_3-300x246.png "aws_create_group_3"){.alignnone
.size-medium .wp-image-1188 width="300"
height="246"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_3.png)  
  
[](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_3.png)その中で「Power
User Access」を選択します。  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_4-300x28.png "aws_create_group_4"){.alignnone
.size-medium .wp-image-1189 width="300"
height="28"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_4.png)  
  
確認します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_group_permit-300x208.png "aws_group_permit"){.alignnone
.size-medium .wp-image-1192 width="300"
height="208"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_group_permit.png)  
  
[](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_create_group_4.png)グループが出来ました。次はグループにユーザーを紐付けます。対象グループを選択し、上部にある「Group
Actions」のクリックすると選択肢が出てくるので「Add Users to
Group」を選択します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_add_user_group-300x109.png "aws_add_user_group"){.alignnone
.size-medium .wp-image-1191 width="300"
height="109"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_add_user_group.png)  
  
ユーザー一覧が出るので、追加したいユーザーにチェックボックスを入れてグループに追加します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_add_user_group_confirm-300x105.png "aws_add_user_group_confirm"){.alignnone
.size-medium .wp-image-1193 width="300"
height="105"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/aws_add_user_group_confirm.png)
