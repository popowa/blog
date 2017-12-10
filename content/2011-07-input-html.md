Title: 
Date: 2011-07-30 16:59
Authors: ayakomuro
Tags:  RightScale, RightScale解体新書
Slug:2011/07/input
Status: published


\~+つい先日サーバテンプレートで立ち上げたサーバテンプレートでInputに入力の漏れがあって、その変数がOperational
Scriptで使うものだったので、困ったな、という事で中の人に聞いてみたら、サーバで直せ、という事だったので、図を描いてみました。  
  
[]サーバテンプレートでは、設定を変数化して、入力出来るのが特徴的ですが、サーバを立ち上げた後は、あまり変更しないと思います（特にBootscriptで使われるInputは見逃していたり、抜けていたりすると、そもそもbootしない場合が多いと思います）  
  
見逃し易いのはOperational ScriptやDecommission
scriptで使うInputで、これは使う時にはって初めて抜けていた、という事に気がつきます。  
  
そういう場合は、サーバテンプレートに入れても実稼働中のサーバには反映されません。なので、実稼働をしているサーバをInputに対して設定をする事で、デプロイメントでのスクリプト実行が出来るようになります。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/640x480.jpg "640x480"){.alignnone
.size-full .wp-image-1316 width="448"
height="280"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/640x480.jpg)  
  
変更したいデプロイメントを選択し、サーバテンプレートではなく、サーバを選択します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input.jpg "input"){.alignnone
.size-full .wp-image-1317 width="453"
height="84"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/input.jpg)  
  
そして個々のサーバページのInputで抜けていた内容を入力します。  
  
[![](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/server_input.png "server_input"){.alignnone
.size-full .wp-image-1318 width="233"
height="179"}](http://cloudstockimg.s3.amazonaws.com/wp-content/uploads/2011/07/server_input.png)  
  
ここで入力する事で、Operational
Scriptなど実行する事が出来ますが、サーバを立てる前にサーバテンプレートに入力しておく事が一番です♫  
  
   
  
   
  
 
