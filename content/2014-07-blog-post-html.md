Title: スポットインスタンスの利用上限数が変更していた件
Date: 2014-07-28 03:02
Authors: ayakomuro
Tags:  AWS, spot
Slug:2014/07/blog-post
Status: published

経口補水液って意外と美味しいなと思った小室です。  

ちょっと前ですがEC2関連の上限数がマネージメントコンソールで見える様になりましたね。

-   [Amazon EC2 Service Limits Report Now
    Available](http://aws.amazon.com/jp/about-aws/whats-new/2014/06/19/amazon-ec2-service-limits-report-now-available/)

おや、これはそう言えば前Trusted
A（げふんげふn　でしたが、ついに気軽に確認出来る様になったので良かったなーと思ってみていたら、別の、まさに表題の件について知ったのでブログ書きます。

Amazon マネージメントコンソール \> EC2 \> Limitsにあります。  
こんな感じでした。

[![](http://3.bp.blogspot.com/--2yXQbe0OVg/U9W63xuzbdI/AAAAAAAAcKw/KgS3enNpWwM/s1600/list.png){width="400"
height="293"}](http://3.bp.blogspot.com/--2yXQbe0OVg/U9W63xuzbdI/AAAAAAAAcKw/KgS3enNpWwM/s1600/list.png)

Spot
インスタンスの一覧にあるdefaultの箇所をクリックすると[こちら](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html)のページに遷移するのですが\....おや\...?  

> By default, you are limited to a total of 5 Spot Instance requests in
> a region. New AWS accounts might have lower limits. Currently, the
> instance types T2, I2, and HS1 are not available on Spot. Also, some
> instance types are not offered in all regions. (For information about
> instance types, see [Instance
> Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html "Instance Types").)

抄訳すると、  

> 各リージョンでのスポットインスタンスは[**5**]スポットインスタンスで、新しいAWSアカウントはもしかしたらそれよりも少ないかもしれません。現在
> T2, I2,
> HS1インスタンスはスポット対応していません。また特定のインスタンスタイプのスポットは全てのリージョンで提供していないかもしれません。

今まではオンデマンドインスタンス数の5倍の数を使える設定だったのですが、やはり皆さん、[スポットインスタンスの良さ]に気付いたのでしょうね。嬉しいやら悲しいやら。。

昔こんな記事を書いたのですがもうクローズしないとですね。。。

-   [知らないと損をする!? スポットインスタンス上限数と起動方法 «
    サーバーワークス
    エンジニアブログ ](http://blog.serverworks.co.jp/tech/2013/03/11/you-should-know-about-spot-instance/)

 
