Title: Spotインスタンスで、継続的にインスタンスを起動し続ける方法
Date: 2013-06-17 20:11
Authors: ayakomuro
Tags:  spot
Slug:2013/06/spot
Status: published

スポットインスタンスについて、毎回金額を状況に合わせなくても、継続的にスポットを使い続ける方法があります。


[![](http://3.bp.blogspot.com/-LzasiAgONQw/Ub9pz6DJHWI/AAAAAAAAXnA/t4lFVyF8ATE/s640/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2013-06-18+4.53.30.png){width="640"
height="217"}](http://3.bp.blogspot.com/-LzasiAgONQw/Ub9pz6DJHWI/AAAAAAAAXnA/t4lFVyF8ATE/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2013-06-18+4.53.30.png)

起動時にPersistent Requestにチェックを入れておくと、

-   上記Max price以上に入札金額がなってインスタンスが終了しても、
-   再度入札金額がMax priceより下になった場合
-   再度インスタンスを起動させる



という事が可能です。









詳細URLはこちら



###  

-   [[【AWS発表】
    EC2のスポットインスタンスがアベイラビリティゾーンを指定できるように](http://aws.typepad.com/aws_japan/2011/07/ec2-spot-pricing-now-specific-to-each-availability-zone.html)]
-   [[An Introduction to Spot
    Instances](http://aws.amazon.com/articles/3260?_encoding=UTF8)]
-   <http://aws.amazon.com/jp/ec2/spot-instances/>
