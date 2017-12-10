Title: 
Date: 2012-12-05 07:17
Authors: ayakomuro
Tags:  xenapp
Slug:2012/12/xenapp-on-cloud
Status: published


Cloud+XenApp(<http://www.citrix.co.jp/products/xenapp/index.html>)て便利ですよね。

XenApp on
AWSもいけるのかしら？と調べてみたら、XenApp内でMSのOfficeは使えないそうです。MSのAzureでも使えないとの回答を頂きました。

また確認すべきライセンスが沢山あるようです。

[Citrix
XenApp製品のよくあるご質問（FAQ)](http://jp.fujitsu.com/platform/server/primergy/software/citrix/answer.html)  
[アプリケーション仮想化「Citrix
XenApp」で実現するシンクライアントシステムご紹介](http://www.kip.co.jp/products/net/XenApp/Citrix_XenApp_2.html)

> ライセンスの考え方  
> 例として、利用者総数500名、同時接続（同時利用する人数）100名の場合のライセンスの考え方をご紹介いたします。

> 1.  [Citrix XenApp
>     ライセンス　100本（Edition別）][ ]
> 2.  [Windows Server
>     CAL　500本（ユーザCAL、デバイスCALのどちらか）] 
> 3.  [Windows Server Terminal Service CAL
>     500本]

> このほかに、XenAppを稼働させる
> WindowsServer自体のライセンスやインストールに必要なメディアなどが必要になります。また、公開するアプリケーションに関しては、アプリケーションを提供するメーカ毎に規定がありますのでご注意ください。また、VM
> Hosted App利用時には、別途Microsoft VECDライセンスが必要となります。



技術的な所ではなくライセンスの問題なので、早く解決するといいなと思います。


