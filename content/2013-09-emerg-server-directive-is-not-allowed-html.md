Title: [emerg] "server" directive is not allowed hereて言われたら
Date: 2013-09-28 21:56
Authors: ayakomuro
Tags:  nginx
Slug:2013/09/emerg-server-directive-is-not-allowed
Status: published


hereて言われたら+Nginxでauth\_basicを追加して設定ファイルの確認しようとしたら  

```sh
[root@dev-site conf.d]# /usr/sbin/nginx -t -c /etc/nginx/conf.d/default.conf
nginx: [emerg] "server" directive is not allowed here in /etc/nginx/conf.d/default.conf:1
nginx: configuration file /etc/nginx/conf.d/default.conf test failed
[root@dev-site conf.d]# /usr/sbin/nginx -v
nginx version: nginx/1.4.2
```

が出て、調べてみた。ちなにみNginxはあまり使った事がない。  
どうやら設定上http外にserverが出ていてはいけないという投稿 (
<http://forum.owncloud.org/viewtopic.php?f=3&t=3426> ) をみて、

```sh
[root@dev-site conf.d]# cat default.conf >> ../nginx.conf
```

コード上  

```sh
http{
略
include /etc/nginx/conf.d/*.conf; #←これをコメント
}
```

をコメントし  
最後に}を追加  

```sh
[root@dev-site nginx]# diff nginx.conf nginx.conf.komurobk
95,172c95
< #    include /etc/nginx/conf.d/*.conf;
< #}
< server {
<     listen      80 default;
<     server_name _;
<     root        /var/www/vhosts/cms;
<     index       index.html index.htm;
<     charset     utf-8;
〜略〜
<     }
---
>     include /etc/nginx/conf.d/*.conf;
174,175d96
<
< } #close http

```
構図としてはこんな感じ
```sh
http{
  ~略~
 #include /etc/nginx/conf.d/*.conf; #server設定が入っていたファイル
  server {}
}
```


確認  

```sh
```

反映された。最近仕様が変わったのかな？
