Title: サブドメインへのリクエストを、（別サブドメインの）サブディレクトリに仕向けたい時
Date: 2012-04-22 03:05
Authors: ayakomuro
Tags:  S3
Slug:2012/04/blog-post
Status: published






若さの過ちで、サブドメインを大量に作ってアプリを展開したのはいいものの、時が過ぎ閉じたいけどなかなか閉じれない時があると思います[（みんな賛同してくれると信じてる）]



例えば  
http://my-cool-app.popowa.com  
というのがあったとします。

サブドメインが動いているサーバーは落としたいけど、どこかにこのサブドメインとコンテンツを残しておきたい。  
しかしその為にサーバを立てて、Virtual
Host設定で別のサイトに転送するのは賢いやり方ではありません。そもそもサーバーを引っ越しする度に、そのVirtual
Hostが何だったのかを思い出して適切な移行をしDNS設定も変更する必要があるからです。

[]

**[No 面倒！ ]**

そんな時にS3のウェブサイト機能を使います。

http://my-cool-app.popowa.com  
に来たリクエストを  
http://www.popowa.com/my-cool-app/index.html  
というサブドメインからサブディレクトリに転送するのをサーバを立てずにします。

まずS3で my-cool-app.popowa.comというバケットを作ります。

[![](http://4.bp.blogspot.com/-xojwSnyxH_o/T5Nub2hy7fI/AAAAAAAAQoI/n4KqFjegAOQ/s400/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-04-22+11.27.50%EF%BC%89.png){width="400"
height="230"}](http://4.bp.blogspot.com/-xojwSnyxH_o/T5Nub2hy7fI/AAAAAAAAQoI/n4KqFjegAOQ/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-04-22+11.27.50%EF%BC%89.png)

バケットを作成後、権限設定で誰でもアクセス可能にします。  

> Grantee: Everyone : List を許可します。

[![](http://2.bp.blogspot.com/-O2W4cXkPy7I/T5NuyaYzmHI/AAAAAAAAQoQ/UX99liJHkcA/s400/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-04-22+11.29.56%EF%BC%89.png){width="400"
height="101"} ](http://2.bp.blogspot.com/-O2W4cXkPy7I/T5NuyaYzmHI/AAAAAAAAQoQ/UX99liJHkcA/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-04-22+11.29.56%EF%BC%89.png)

その後Websiteタブをクリックし、

> Enabled: クリック
>
> Index Document: index.html
>
> Error Document: index.html
>
> Endpoint: 自動で生成されるのでコピーしておきます。


[![](http://3.bp.blogspot.com/-g9F8ZxSGB1U/T5NuzFxMkeI/AAAAAAAAQoU/K6SPhmxU57s/s400/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-04-22+11.30.24%EF%BC%89.png){width="400"
height="112"} ](http://3.bp.blogspot.com/-g9F8ZxSGB1U/T5NuzFxMkeI/AAAAAAAAQoU/K6SPhmxU57s/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-04-22+11.30.24%EF%BC%89.png)


popowa.comのDNSはRoute 53を使っているので、Route
53でレコードを編集します。  
（ここはドメインが使っているDNSを変更します。）  
先ほどコピーしたEndPointをCNAMEにします。

> my-cool-app.popowa.com CNAME
> my-cool-app.popowa.com.s3-website-ap-northeast-1.amazonaws.com

[![](http://3.bp.blogspot.com/-xximfnARLuw/T5NuzpmQ5FI/AAAAAAAAQoc/p45y38zRhEY/s400/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-04-22+11.31.28%EF%BC%89.png){width="345"
height="400"}](http://3.bp.blogspot.com/-xximfnARLuw/T5NuzpmQ5FI/AAAAAAAAQoc/p45y38zRhEY/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-04-22+11.31.28%EF%BC%89.png)

その後以下のHTMLをindex.htmlとしてコピーして作成したバケットにアップロードします。S3には.htaccessは使えません。なので以下のようなHTML自体が転送をする処理を追加しておく必要があります。  
もし分岐させたい場合は、リクエストのURLを見てそこから別のドメインに付け足して。。という事も出来ます。  

> \<html xmlns=\"http://www.w3.org/1999/xhtml\"
> xmlns:og=\"http://ogp.me/ns\#\" xml:lang=\"ja\" lang=\"ja\"\>  
>     \<head\>  
>         \<meta http-equiv=\"Content-Type\" content=\"text/html;
> charset=utf-8\" /\>  
>         \<meta http-equiv=\"Content-Script-Type\"
> content=\"text/javascript\" /\>  
>         \<title\>Redirect to
> http://www.popowa.com/my-cool-app/index.html\</title\>  
>         \<script type=\"text/javascript\" language=\"javascript\"\>  
>         \<!\--  
>        
> location.href=\'http://www.popowa.com/my-cool-app/index.html\';  
>         // \--\>  
>         \</script\>  
>     \</head\>  
>     \<body\>  
>     See you Later!  
>     \</body\>  
> \</html\>

これじゃなくても  

> \<meta http-equiv=\"Refresh\"
> content=\"0;URL=http://www.popowa.com/my-cool-app/index.html\" /\>

でもいいかもしれません。

それではアクセスしてみましょう！  
[http://my-cool-app.popowa.com](http://my-cool-app.popowa.com/)  
あっという間に  
<http://www.popowa.com/my-cool-app/index.html>  
に転送されていると思います。

これで転送用のサーバを立てずして過去の遺産を新しいドメインに移す事が出来ましたね！

という訳で過去よ永遠に、S3を使ったサブドメインからサブディレクトリへの転送でしたー
