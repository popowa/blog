Title: 
Date: 2013-11-09 09:48
Authors: ayakomuro
Tags:  Uncategorized
Slug:2013/11/phpchmod-operation-not-permitted
Status: published


permittedって出たら+多分ファイルの所有者と、それを実行しようとするプロセスユーザーが一致していないのだと思う。  
なので

> \$ chown apache hoge.txt

みたいにしてあげればいいと思う。  
http://php.net/manual/ja/function.chmod.php
