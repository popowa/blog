Title: FQDNが変わった時にWordpressでどう対処出来るか
Date: 2013-01-05 01:49
Authors: ayakomuro
Tags:  Uncategorized
Slug:2013/01/fqdnwordpress
Status: published

よくAWSのハンズオンや学校の授業などでEC2にWordPressを入れて試してみよう！というのをやるのですが、毎回困るのが次の授業でAMIからEC2を立ち上げると、FQDNが変わっていて、Wordpressがちゃんと表示されない、という事です。


[![](http://4.bp.blogspot.com/-dxwPvGthFbU/UOeP3uUABwI/AAAAAAAAV-g/4dkOnnxEXCg/s320/wordpress-logo-stacked-rgb.png){width="320"
height="196"}](http://4.bp.blogspot.com/-dxwPvGthFbU/UOeP3uUABwI/AAAAAAAAV-g/4dkOnnxEXCg/s1600/wordpress-logo-stacked-rgb.png)

[]  
今まで起こっていた流れとしては

1.  EC2インスタンスで[**WordPress立ち上げ成功**]！（この時はEC2のFQDNを利用）
2.  EC2インスタンスを**AMI化**[、もしくは]**[停止]**にして**[数日]**寝かしておく
3.  AMIからまたWordPressをインストールしたEC2を起動する(先日とは違うFQDNになる)
4.  ブラウザーから新しいWordPressにアクセスをする（HTTPDはリクエストを受け付ける）
5.  **CSSが表示されず、管理画面にもログイン出来ない**
6.  ＼(\^o\^)／ｵﾜﾀ

という感じでした。  
これを解決する方法を調べてみたので、記載します。  
[もちろんEC2のハンズオンの前にDNSのRoute53か固定IPのEIPをやればいんでしょうけど、どうしてもサイドディッシュというか後回しになっちゃうですよねー（白目]

### 1. DB内の値を変える

    $ mysql -u アカウント名 -p #MySQLにログイン
    mysql > use wordpress;
    mysql> UPDATE wp_options 
     SET option_value = replace(option_value, 
     'http://old.example.jp',  'http://new.example.jp') 
     WHERE option_name = 'home' OR option_name = 'siteurl';

最初はこのやり方しか知らなかったのだけど、ハンズオンや授業では非常に面倒で、このやり方以外にないのかなぁと思っていた。

### 2. wp-config.phpで\"予め\"設定しておく

    $ vi /var/www/wordpress/wp-config.php
    define('WP_HOME','http://new.example.com/');
    define('WP_SITEURL','http://new.example.com/');

この方法だと、管理画面から設定が出来なくなるが、FQDNが変わってしまって管理画面にログイン出来なくなって(1)をする事になるよりはマシだと思う。

### 3. functions.phpに書いて、(1)を行なう

    $ vi /var/www/wordpress/wp-content/themes/twentytwelve/functions.php
    update_option('siteurl','http://new.example.com/');
    update_option('home','http://new.example.com/');

利用しているテンプレートにあるfunctions.phpが呼ばれた時に(1)を行なってくれる機能があるそうです。  
これを書いて実行するのは一回だけで、上書きが終わったら、上記のupdate\_optionの行を削除する必要があるそうです。二度手間ですね。

functions.phpがなければ、以下のように新規作成すればよいようです。

    <?php
    update_option('siteurl','http://new.example.com/');
    update_option('home','http://new.example.com/');
    ?>

### 4. 一時的に管理画面にログインする際のURLを違うものでも良しとする設定をtrueにする

    $ vi /var/www/wordpress/wp-config.php
    define('RELOCATE',true);

wp-config.phpに上記を追加する事で、違うFQDNでアクセスしている際に管理画面に一時的にログインを許可する設定が出来るそうです。  
上記を追加する事でhttp://new.example.jp/wordpress/wp-login.phpにアクセスする事でDB内のsiteurlが上書きされて、管理画面にログインが可能になります。  
管理画面ログイン後、設定ページでhomeの部分を新しいURLに書き換えれば終了！  
書き換えが終わったらRELOCATEは削除しておかないと別ドメインでアクセスして来た人にsiteurlを上書きされるので気をつけましょう。

### 参考URL

-   [Changing The Site
    URL](http://codex.wordpress.org/Changing_The_Site_URL)
