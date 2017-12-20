Title: ELBのドメインの扱い方
Date: 2012-10-30 22:07
Authors: ayakomuro
Tags:  ELB
Slug:2012/10/elb
Status: published

ELBで扱えるドメイン






### Zone Apex



ELB(example.com)





\_EC2





\_EC2





\_EC2\....









=\> Zone ApexをRoute53を利用してのみ可能







### サブドメイン



ELB(www.example.com)







\_EC2





\_EC2





\_EC2\....











=\> NSはどこでもよい



### サブディレクトリ



ELB(www.example.com)







\_EC2(Apache/Varnish/Nginx等のProxyサーバ)





      \_EC2(www.example.com/dir)





      \_EC2(www.example.com/dir2)







      \_EC2\....









=\> ELBの下にProxyサーバを置く事で可能









ELBがサブディレクトリの処理をするのは違うとは思うが、機能としては欲しいなぁと思う今日この頃


