Title: ロリポップのレンタルサーバのメールだけを使えないか調べてみた
Date: 2013-02-13 03:37
Authors: ayakomuro
Tags:  lolipop
Slug:2013/02/blog-post
Status: published

ロリポップのレンタルサーバのメール機能だけを使えないかどうか調べた見た。


例えばexample.comというドメインがあった時

-   example.comのドメイン取得はお名前.com
-   example.comのネームサーバーはAWS Route53
-   http://example.com、http://www.example.comのウェブサーバはさくらVPS
-   メールアカウント@example.comをロリポップのレンタルサーバのメール機能

という風にしたかった。

[]  
ロリポップのサービスを契約したりサポートに問い合わせてみたりしたけど、どうやらドップレベルの独自ドメインでしか利用出来ない模様。。  
つまり

-   ルートドメイン（example.com）のネームサーバーがロリポップ側にある



以外はレンタルサーバがうまく利用出来ないという事のようです。



それならばサブドメインで出来るかな、と思って調べてみた結果のメモです（ルートドメインて自分で書いておきながら少し矛盾もある気がするが。。）

-   example.comのドメイン取得はお名前.com
-   example.comのネームサーバーはAWS Route53
-   http://example.com、http://www.example.comのウェブサーバはさくらVPS
-   メールアカウント@[mail.]example.comをロリポップのレンタルサーバのメール機能  
   ↑mail.example.comをロリポップ側に委譲する事で利用出来るのではないか！？と思った次第。

最初以下のネームサーバーをサブドメインのNSとして登録すればよいのかと思い設定してみた。

-    <http://lolipop.jp/manual/user/chg-plan/>

[![](http://4.bp.blogspot.com/-uxlv7jinxDk/URsFbFhrZcI/AAAAAAAAWvw/tp30MW3TvmM/s1600/1.png)](http://4.bp.blogspot.com/-uxlv7jinxDk/URsFbFhrZcI/AAAAAAAAWvw/tp30MW3TvmM/s1600/1.png)


その後対象ドメインの設定内で、サブドメインにてNSを作成した

[![](http://1.bp.blogspot.com/-HZ91zFaz9wo/URsFbDoIyJI/AAAAAAAAWvs/oYOP3RGT1vA/s1600/2.png)](http://1.bp.blogspot.com/-HZ91zFaz9wo/URsFbDoIyJI/AAAAAAAAWvs/oYOP3RGT1vA/s1600/2.png)


これでmail.popowa.comをロリポップ側の独自ドメイン設定扱いとすればロリポップサーバが使えるはず！！╰(\*´︶\`\*)╯♡


。。


エラーが。。。


[![](http://4.bp.blogspot.com/-beqE-6mXMi8/URsGejRRNPI/AAAAAAAAWwA/ccRLOh-Bm3o/s1600/3.png)](http://4.bp.blogspot.com/-beqE-6mXMi8/URsGejRRNPI/AAAAAAAAWwA/ccRLOh-Bm3o/s1600/3.png)


(´；ω；｀)ﾌﾞﾜｯ


という訳で、検証の結果サブドメイン委譲でのロリポップレンタルサーバ利用は難しそうです。

もしかしたらウェブ側のvalidation問題でやろうと思えば出来るかもしれない。


-   <http://ya7a.se/2011/05/15/using-se-domains-at-lolipop-server-jp/>


もしロリポップ側で機能追加があれば、メールサーバーだけ使えるような機能があるといいなと思いました！お願いします！！
