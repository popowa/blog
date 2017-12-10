Title: 今日のalias
Date: 2013-04-12 00:44
Authors: ayakomuro
Tags:  Mac
Slug:2013/04/alias
Status: published

Macのローカルで時々作業する時、MySQLの起動コマンドがどこだったか毎回忘れてhistoryでgrepしている自分に嫌気が指したので、aliasに入れてみた。


> \$ vi \~/.bashrc  
> alias startdb=\'/usr/local/bin/mysql.server start\'  
> :wc  
> \$ source \~/.bashrc  
> \$ startdb  
> Starting MySQL  
> .. SUCCESS!

なかなかMacの環境には慣れませんね。。
