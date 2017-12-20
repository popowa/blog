Title: 
Date: 2013-02-13 01:36
Authors: ayakomuro
Tags:  AWS, Route53
Slug:2013/02/route53hosted-zone-delete-hosted-zone
Status: published


Route53+既知な事かもしれないけど、Hosted Zone(ドメイン）を消す時はRecord
Setを消す必要があるんだけど、NSとSOAは消せない。  
You might already know this, but I didn\'t.  
Before deleting hosted zone, you need to delete record sets first. But
you can\'t with NS and SOA.

[![](http://4.bp.blogspot.com/-A7tZ7VW6txI/URrrDZ8pBgI/AAAAAAAAWu8/zsO2DQdkKA8/s1600/1.png)](http://4.bp.blogspot.com/-A7tZ7VW6txI/URrrDZ8pBgI/AAAAAAAAWu8/zsO2DQdkKA8/s1600/1.png)


[]

例えばNS/SOA/CNAMEがあった場合、全部を選択したら、Delete Record
Setはクリック出来る状態。

eg. there are 3 record sets, NS/SOA/CNAME. Select all and click \'Delete
Record Set\'.


[![](http://2.bp.blogspot.com/-QAuYuUwgvKI/URrrDWLvDcI/AAAAAAAAWu4/FGe0v0p5wtY/s1600/2.png)](http://2.bp.blogspot.com/-QAuYuUwgvKI/URrrDWLvDcI/AAAAAAAAWu4/FGe0v0p5wtY/s1600/2.png)

クリックしたらちゃんと削除対象として認識してくれる。でも削除出来ない。

Popup confirmed to delete 3 record sets, but you can\'t delete NS/SOA.

[![](http://3.bp.blogspot.com/-LI4ioneJR94/URrrDSEZuoI/AAAAAAAAWvA/L0rTeT5PuK8/s1600/3.png)](http://3.bp.blogspot.com/-LI4ioneJR94/URrrDSEZuoI/AAAAAAAAWvA/L0rTeT5PuK8/s1600/3.png)

NS/SOAだけ残った状態だと、選択してもDelete Record
Setはクリック出来る状態にはならない  
You can\'t select \'Delete Record Set\' when selected record sets are
either NS or SOA or both.

[![](http://3.bp.blogspot.com/-QXWJCIYZxws/URrrDvhCF2I/AAAAAAAAWvI/yqF4PY9kO1Q/s1600/4.png)](http://3.bp.blogspot.com/-QXWJCIYZxws/URrrDvhCF2I/AAAAAAAAWvI/yqF4PY9kO1Q/s1600/4.png)

削除するには一つ上のレベルにあがってDelete Hosted
Zoneをする事でNS/SOAを削除する。

You have to go to Hosted Zone leve to delete NS/SOA related to target
domain.


まぁ考えてみたら、Hosted
Zoneを追加すると自動で最初に追加されるのがNS/SOAなので当たり前の機能ですよね。ちょっと明確には知らなかったのでメモした次第でした。

When you make new hosted zone, it will come with NS/SOA, so there is no
wonder in reverse way. But I just didn\'t know exact validation :)

