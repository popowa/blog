Title: 
Date: 2014-01-29 21:56
Authors: ayakomuro
Tags:  blogger
Slug:2014/01/bloggermobile-template
Status: published


templateを自分で編集する方法+ちょっと知り合いに聞かれて調べてみたら、分かったのでブログにも書いておく

当ブログはBloggerを使っているんだけど、携帯向けのテンプレートもあってそれをアクセスした端末によって出し分けている  
PC関連  
<http://blog.popowa.com/>  
モバイル関連  
<http://blog.popowa.com/?m=1>

基本あまりテンプレートとか触らないんだけど、このモバイル向けCSSを触りたい時は以下の方にするといい。

1.  テンプレート \> モバイルで、モバイル
    テンプレートを選択で、カスタムを選択して保存。
2.  その後「ブログで使用中」アイコンの下にあるカスタマイズアイコンをクリック
3.  その後上級者向け \>
    CSSを追加、に好きなCSSを追加すればモバイル関連のみに反映される。

モバイル関連だとbodyタグにclass=mobileと入るので、基本はmobileクラスに入れ子にすれば間違いないと思う。

例  

> .mobile .title 

一つ勉強になった
