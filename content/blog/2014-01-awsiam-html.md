Title: 昔からAWSを使っている人はセキュリティ証明書をIAM側に移行させよう
Date: 2014-01-30 08:29
Authors: ayakomuro
Tags:  AWS
Slug:2014/01/awsiam
Status: published

IAMが出来る前は、AWSマネージメントコンソールではなくアカウントサイトにてセキュリティ証明書を発行出来るページがあって（今もある）、X509証明書や今で言うアクセスキーの発行を行っていたのですが、どうやら今後そのセキュリティ証明書のページが閲覧出来なくなるらしいので、IAMに移行しましょう。


<https://portal.aws.amazon.com/gp/aws/securityCredentials>  
ここにアクセスするとこんな警告が出る（理解しました、をチェックいれても毎回出る）

[![](http://4.bp.blogspot.com/-YabHPwqrobk/UuoKAme1VvI/AAAAAAAAZHs/II3oUObHo_s/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.09.33.png)](http://4.bp.blogspot.com/-YabHPwqrobk/UuoKAme1VvI/AAAAAAAAZHs/II3oUObHo_s/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.09.33.png)

IAM出来てからはセキュリティ証明書は無効にしてIAM側でまとめている人がほとんどだと思うけど、もしまだフルアクセス権のアクセスキー、X.509証明書、キーペア(EC2/Cloudfront用）を保持している人は、IAMや所定の箇所に移行するといいんじゃないかな。

[![](http://1.bp.blogspot.com/-yJoMrzwWq8Y/UuoKK3LeKxI/AAAAAAAAZH0/nuLq4I1Eq2A/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.13.15.png)](http://1.bp.blogspot.com/-yJoMrzwWq8Y/UuoKK3LeKxI/AAAAAAAAZH0/nuLq4I1Eq2A/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.13.15.png)

このページも無くなるかもしれないので、記念にスクリーンショット載せておく（魚拓するまではないw)

ここで証明書を発行していた時が遥か昔のような気持ちになる。  
なんか時代を感じるね。

[![](http://3.bp.blogspot.com/-LY1S_3tr11E/UuoLCLqhJqI/AAAAAAAAZH8/00SwmPED02Q/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.16.11.png)](http://3.bp.blogspot.com/-LY1S_3tr11E/UuoLCLqhJqI/AAAAAAAAZH8/00SwmPED02Q/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.16.11.png)

[![](http://2.bp.blogspot.com/-ybBgzjNp8Nc/UuoLCIqofgI/AAAAAAAAZIA/HQuMaQr5etg/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.16.19.png)](http://2.bp.blogspot.com/-ybBgzjNp8Nc/UuoLCIqofgI/AAAAAAAAZIA/HQuMaQr5etg/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.16.19.png)

[![](http://2.bp.blogspot.com/-L5P9vt20T1U/UuoLCEkpvoI/AAAAAAAAZIE/7qBmGbu5MJY/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.16.25.png)](http://2.bp.blogspot.com/-L5P9vt20T1U/UuoLCEkpvoI/AAAAAAAAZIE/7qBmGbu5MJY/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.16.25.png)

[![](http://2.bp.blogspot.com/-X8p0kw9Gdjo/UuoLC8hY1pI/AAAAAAAAZIM/UvmC_Wv4_Yc/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.16.41.png)](http://2.bp.blogspot.com/-X8p0kw9Gdjo/UuoLC8hY1pI/AAAAAAAAZIM/UvmC_Wv4_Yc/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-01-30+17.16.41.png)
