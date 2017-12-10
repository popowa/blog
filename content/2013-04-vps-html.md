Title: VPS的なサービスを探している
Date: 2013-04-27 00:22
Authors: ayakomuro
Tags:  help, VPS
Slug:2013/04/vps
Status: published

放置していたので全く気付かなかったんだけど、dotCloudがsandboxを停止するという通知を出していたみたいで、コードも全部削除になってしまった。


-   [April 25thAll Sandbox applications will be
    destroyed.](http://blog.dotcloud.com/new-sandbox#sunset)
-   [お金を(なるべく)かけずにサーバー運用出来るか試してみた](http://blog.popowa.com/2012/03/less-money-more-options.html)

元々のコード自体は[github](https://github.com/popowa/ATND)に置いていたのでよかったんだけど、またホスティングする場所探さないとなーという事で自分の中でのVPS
要件定義を書いてみる

小室的VPS要件定義

安い、もしくは無料

-   年払いだと安くなる、というのでもOK

サブドメインにて操作出来る

-   NSを移譲しないと使えない、というのはNG

SaaSでもいい

-   以下のようにアクセス出来るAPIもしくは何かしらのデプロイ方法があれば。

SSHが出来る、もしくは外部からの自分のコードがデプロイ方法がある

-   指定アプリのデプロイはあまり嬉しくない。
-   ex. wordpressをワンクリックでデプロイ、とか

IPv4なくてもいい

-   root domainを使わないので。

性能にはそんなにこだわらない

-   料金に比例する事を理解している

サポートもそんなに必要ない

-   helpページがあればいい



という訳で、ゴールデンウィークかけてVPS探してみたいと思います。









早速教えてもらったVPSサービス





> @[ayakomuro](https://twitter.com/ayakomuro)
> [epw.jp](http://t.co/pV2njG4cdS "http://www.epw.jp/")
> 日本のホスティングで、3150円/年です。 ExpressWeb  
> --- Naoki Satoさん (@nksato)
> [2013年4月26日](https://twitter.com/nksato/status/327933690489470976)

> @[ayakomuro](https://twitter.com/ayakomuro) では
> [digitalocean.com](https://t.co/3eenXewADc "https://www.digitalocean.com/")
> でもどうぞー。出来た当初問題でたけど、ここ2ヶ月ノントラブルですよ。  
> --- d6rkaizさん (@d6rkaiz)
> [2013年4月26日](https://twitter.com/d6rkaiz/status/327933811818119168)

> @[ayakomuro](https://twitter.com/ayakomuro) ゲヒルンとか  
> --- あやぴー@なんちゃってLisperさん (@ayato\_p)
> [2013年4月26日](https://twitter.com/ayato_p/status/327934496357883904)










