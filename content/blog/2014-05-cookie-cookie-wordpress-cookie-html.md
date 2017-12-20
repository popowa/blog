Title: 
Date: 2014-05-12 06:28
Authors: ayakomuro
Tags:  rss-image-feed, wordpress
Slug:2014/05/cookie-cookie-wordpress-cookie
Status: published


に対応していません。WordPress を使うには Cookie
を有効にする必要があります。+表題のエラーが出てログイン出来ないよ！！と言われてなんだろうと思って調べて、対処した話。

[![](http://3.bp.blogspot.com/-QEhK3v7qM2c/U3BogYvYzzI/AAAAAAAAar4/HV8Cfs4ncMw/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-05-12+10.43.11.png)](http://3.bp.blogspot.com/-QEhK3v7qM2c/U3BogYvYzzI/AAAAAAAAar4/HV8Cfs4ncMw/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-05-12+10.43.11.png)


取りあえずhttp://www.example.com/wp-adminにアクセスすると真っ白ページに表示される。それからphp\_errors.logに以下のように出力されていた。

> ``` 
> [12-May-2014 01:44:32 UTC] PHP Warning:  Cannot modify header information - headers already sent in /var/www/wordpress/wp-login.php on line 427
> ```

で、結局



1.  Wordpress入れ替え
2.  wp-config.phpだけを新しい方に置き換え
3.  ここでDBの更新が走る
4.  ログイン出来る事を確認
5.  themesを新しい方にコピー
6.  pluginsを新しい方にコピー　-\> エラー再現
7.  pluginsフォルダーを元に戻す
8.  pluginsフォルダー内にある個々のプラグインを一つずつ新しい方にコピー＆エラーが出来るかどうか調べる
9.  結果、[rss-image-feed](http://wordpress.org/plugins/rss-image-feed/)というプラグインがエラーを出していました



上記プラグインを使っていてエラーになったら上記方法を試してみてください。




