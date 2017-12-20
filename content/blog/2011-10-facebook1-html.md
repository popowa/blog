Title: Facebookのいいね！を変えたいだけどなー/その1
Date: 2011-10-08 14:10
Authors: ayakomuro
Tags:  Chrome, extension
Slug:2011/10/facebook1
Status: published

Facebookのいいね！ボタンが日本のポータルサイトに始まり、ブログ、企業サイト、至る所に出没するようになったのは、ほんの最近のように思います。  

でもあるのが当たり前な毎日になって無い方が不思議なくらいに、日本でのFacebookは普及しました。  
でもなんでいつも青色バックのいいね！なんだろう？と思った事はありませんか。  
いいね！じゃなくて、カワイイ！とか日本人向けなんじゃないのとか、tdiaryのプラグインでもあるへー！ボタンとかでもいいんじゃないのかな、と思って調べてみました  
[]  
それをChromeのExtentionで実装出来ないだろうか？調査とその結果にいたるまでの内容です、というかまだ終わってません。orz  
やりたい事としてはFacebook Like
Buttonを実装するサイト側じゃなくて、そのButtonを見ている側がそれを自分のブラウザーだけでカスタマイズ出来ないかなーと思ったのです。greasemonkeyとかで出来そうな気もするんだけど。

まずChrome のextentionの作り方についてはこのページが参考になりました。  
[\>\> Tutorial: Getting Started (Hello,
World!)](http://code.google.com/chrome/extensions/getstarted.html)

よくある echo
\'hello\'とかじゃなくて、とても実践的なチュートリアルです。

上記を一通りやってみてから、Facebookのいいね！ボタンについて調べてみます。  
[\>\> Facebook Like
Box](http://developers.facebook.com/docs/reference/plugins/like/)  
例えばblog.popowa.comに対していいね！ボタンを付ける場合、コードとしては






になります。  
（上記のソース内でJSが動いてしまっているけど）その後実際にウェブ経由で見た際にどのように展開されているかというと



divの中にspanを入れて、その中にiframeをappendして表示させているようです。

iframe内にあるsrcのURLをブラウザーで叩くとになって以下のようになっていました。

[![](http://3.bp.blogspot.com/-2vvfpwCHxxw/TpBFVgFKgLI/AAAAAAAANuo/W9ejYleQyVw/s320/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%25EF%25BC%25882011-10-08+20.22.02%25EF%25BC%2589.png){width="320"
height="37"}](http://3.bp.blogspot.com/-2vvfpwCHxxw/TpBFVgFKgLI/AAAAAAAANuo/W9ejYleQyVw/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%25EF%25BC%25882011-10-08+20.22.02%25EF%25BC%2589.png)

このiframe内のHTMLを見るとページ末尾参照のようになっています（長いです）。
その中でLikeとかいいね！になっている部分は

    いいね！

そもそもあるページからiframe内に読み込まれるデータを変更出来るんだろうか？  
これは調べてみたら出来るようですが、iframeのid/nameは、reloadする度に変わる事が判明。  
ここはid/nameが固定じゃないと var likeText =
.document.getElementByClassName(\'liketext\').value;
で出来ない。  
何度かreloadして分かった事は、最初の文字が小文字英語の\"f\"である事ぐらいで、その後はランダムであまり規則性がなさそう。

[![](http://1.bp.blogspot.com/-DRoBXLLdEEE/TpBFWRaub_I/AAAAAAAANuw/PFzolWrmfWE/s320/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%25EF%25BC%25882011-10-08+21.37.14%25EF%25BC%2589.png){width="320"
height="20"}](http://1.bp.blogspot.com/-DRoBXLLdEEE/TpBFWRaub_I/AAAAAAAANuw/PFzolWrmfWE/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%25EF%25BC%25882011-10-08+21.37.14%25EF%25BC%2589.png)

[![](http://2.bp.blogspot.com/-JccnW4lAuQk/TpBFV03QklI/AAAAAAAANus/Zjy8UUZtmUE/s320/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%25EF%25BC%25882011-10-08+21.37.01%25EF%25BC%2589.png){width="320"
height="21"}](http://2.bp.blogspot.com/-JccnW4lAuQk/TpBFV03QklI/AAAAAAAANus/Zjy8UUZtmUE/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%25EF%25BC%25882011-10-08+21.37.01%25EF%25BC%2589.png)

結構大変そうな事が分かったので、この時点でjQueryを導入しようと決意。  
そして検索しているうちにこんなページを発見  
[\>\>
Facebookの「いいね！」ボタンのガイドライン ](http://www.facebook.com/brandpermissions/logos.php)  
用途  
「いいね！」ボタンの大きさは必要に応じて調節していただいて構いませんが、その他の変更は一切認められません(デザイン変更など)。  
 という事なので、出来ない模様。この用途を良く読むと\[F\]がないといけない、と書いてあるのにはすこし驚きを感じました。結構適当にいいね！を\[F\]なしで使っている広告代理店とか、見る気がします。まぁ、それはいつかFacebookが本腰を入れたら直るかと思いますが。

さて個人のブラウザー単位でいいね！を違う文字に変えられるか、という話に戻ると、
まだ出来てなくてjQueryのAPIを現在調べ居ている所。  
動的にjQueryをappendした時、確かそれ専用にreload的に使える関数があった気がするんだけど、まだ見つけれてない。  
こんな感じで書いてみたんだけど、jQueryが読み込まれてないようで、\$って何？とエラーが出る。  
manifest.json

    {
      "name": "Customize FB Like!",
      "version": "1.0",
      "description": "This extension can allow you customize Facebook 'like' to 'Cute'",
      "content_scripts": [
           {
           "matches": ["http://*/*"],
            "js": ["myscript.js"]
           }
       ],
      "permissions": [
      ]
    }

myscript.js

    var script = document.createElement('script'); 
    script.type = 'text/javascript'; 
    script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js'; 
    document.getElementsByTagName('head')[0].appendChild(script);

     $(document).ready(function(){
       $('iframe').contents().find('span[@class="liketext"]').html('Cute');
     });

もうちょっと調べないとです(´・ω・\`)。

つづく！

FacebookのLike ButtonのiframeのsrcのHTML詳細

    Like










    いいね！

[承認](http://www.blogger.com/blogger.g?blogID=2677338708669705892)



  



  
あなたが「いいね！」と言っています。[](http://www.blogger.com/blogger.g?blogID=2677338708669705892) · [管理用ページ](http://www.blogger.com/blogger.g?blogID=2677338708669705892) · [インサイト](http://www.blogger.com/blogger.g?blogID=2677338708669705892) · [エラー](http://www.blogger.com/blogger.g?blogID=2677338708669705892)[小室
文](http://www.facebook.com/ayakomuro)さんが「いいね！」と言っています。「いいね！」と言っている友達はまだいません。[](http://www.blogger.com/blogger.g?blogID=2677338708669705892) · [管理用ページ](http://www.blogger.com/blogger.g?blogID=2677338708669705892) · [インサイト](http://www.blogger.com/blogger.g?blogID=2677338708669705892) · [エラー](http://www.blogger.com/blogger.g?blogID=2677338708669705892)



  



  

  

  



  



  



  
[![](http://profile.ak.fbcdn.net/hprofile-ak-snc4/23094_681849640_6919_q.jpg){.connect_widget_image
.img}小室 文](http://www.facebook.com/ayakomuro)



  



  



  

  

  
  
  
