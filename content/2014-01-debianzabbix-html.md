Title: DebianでのZabbixの入れ方
Date: 2014-01-01 05:00
Authors: ayakomuro
Tags:  zabbiz
Slug:2014/01/debianzabbix
Status: published

ドキュメント読んでいたら.debパッケージをwgetして入れろ、みたいな事を書いてあるんだけど、wheey-backportにもあって、どっちがどっちなんだ！？となったので調べてみたよ。


-   <https://www.zabbix.com/documentation/2.2/manual/installation/install_from_packages>
-   <http://packages.debian.org/wheezy-backports/zabbix-server-mysql>







Zabbixソースパッケージ（<http://packages.debian.org/source/wheezy-backports/misc/zabbix>）からzabbix-server-mysqlのパッケージがビルドされているので、Debianで使う場合は  
source.listsでwheey-backportの設定をしてから

1.  mysql-server(2番目の依存パッケージであるので、明示的に指名する必要は無い）
2.  zabbix-server-mysql
3.  zabbix-frontend-php





を入れれば使えるようになる。


