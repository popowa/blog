Title: 
Date: 2014-08-02 02:19
Authors: ayakomuro
Tags:  Windows Server
Slug:2014/08/windows-ec2
Status: published


EC2で速度を計測するまでの設定+Windowsとか全然分からないのですが、機会があったのでWindows
EC2でiperfを使って速度計測してみました。

このブログは、本当にWindowsとかWIndows
Server触った事ない、MSの製品の設計思考を知らない人が操作したログなので知っている人からすればそんなの（ryという感じです。

[ローカルのMacにipefを入れる]  

> brew install iperf

なんて簡単！

[Windows EC2を起動する]

まずWindows EC2を起動します。起動するAMIはMicrosoft Windows Server 2012
R2 Base で良いでしょう。  
起動方法はこちらにあるのでここは省略します。Security
Groupで5001を開けておいてください。

-   [AWS 初級トレーニング （Windows Server 2012編） \#aws
    \#ec2](http://www.slideshare.net/AmazonWebServicesJapan/aws-windows-14943091) 

[Windows EC2に接続する]

Mac OS からログインするときはRemote Desktop
Connectionだとエラーで何故かログイン出来ないので、[CoRD](http://cord.sourceforge.net/)をダウンロードします。ホスト名とUsername,
passwordを設定すればログインが可能です。  
Mac OS 10.9.4だとこのアプリでWindows OSにログイン出来なかった  
（参考記事: [http://ameblo.jp/nekocat2/entry-11494736515.html](http://ameblo.jp/nekocat2/entry-11494736515.html))

[![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-Oo-wRg9tF0M%2FU9w09iUU7hI%2FAAAAAAAAcMQ%2F98UlH4aaTFQ%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B9.45.50.png&container=blogger&gadget=a&rewriteMime=image%2F*)](http://2.bp.blogspot.com/-Oo-wRg9tF0M/U9w09iUU7hI/AAAAAAAAcMQ/98UlH4aaTFQ/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-02+9.45.50.png)　←この人だとエラーでRDP出来ない

[Windows EC2の設定をする]  
ログイン後、まずiperfをダウンロードしたいので、IEの設定を変更します。左側の四角いアイコン（多分スタートボタンだと思います）をクリックします。

[![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-E7a9R9o3lGA%2FU9w2zO-5ZnI%2FAAAAAAAAcMc%2Fza76YTbscOo%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B9.53.55.png&container=blogger&gadget=a&rewriteMime=image%2F*)](http://1.bp.blogspot.com/-E7a9R9o3lGA/U9w2zO-5ZnI/AAAAAAAAcMc/za76YTbscOo/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-02+9.53.55.png)

クリックすると、このようなタイルみたいなのが出てくるので、Internet
Explorerをクリックします。ちなにこのページから最初のデスクトップ画面に戻りたいときは右上にあるDesktopをクリックすれば戻れました。

[![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F3.bp.blogspot.com%2F-lYC0iLVu6RM%2FU9w3vWZ0K4I%2FAAAAAAAAcMk%2FOQFgBHNwH00%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B9.57.07.png&container=blogger&gadget=a&rewriteMime=image%2F*)](http://3.bp.blogspot.com/-lYC0iLVu6RM/U9w3vWZ0K4I/AAAAAAAAcMk/OQFgBHNwH00/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-02+9.57.07.png)

クリックすると、IEが立ち上がるので、右上にある車輪マーク？をクリックします。

[![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-bWuXYNmQ054%2FU9w4CnC9awI%2FAAAAAAAAcMs%2FpTa165yGyJ8%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B9.59.17.png&container=blogger&gadget=a&rewriteMime=image%2F*)](http://1.bp.blogspot.com/-bWuXYNmQ054/U9w4CnC9awI/AAAAAAAAcMs/pTa165yGyJ8/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-02+9.59.17.png)

クリックするとメニューが出てくるのでInternet Optionsを選択します。

[![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-VJD2GgS9s7g%2FU9w4R89IAvI%2FAAAAAAAAcM0%2FethssahlZRc%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.00.06.png&container=blogger&gadget=a&rewriteMime=image%2F*)](http://2.bp.blogspot.com/-VJD2GgS9s7g/U9w4R89IAvI/AAAAAAAAcM0/ethssahlZRc/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-02+10.00.06.png)

ポップアップが出てくるので、Securityタブを選択し、Internetアイコンを選択した後、Custom
Levelをクリックします。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-9_sB3oQ4WjE%2FU9w6bivNELI%2FAAAAAAAAcNA%2FY6bAnpeuBls%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.01.26.png&container=blogger&gadget=a&rewriteMime=image%2F*)  
Settingsの所で、Downloads \> File Download をDisable から
Enableにします。その後OKをクリックします。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-63k1akGzg_M%2FU9w6tdiU7ZI%2FAAAAAAAAcNI%2Fsh2JjyNKX4c%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.03.19.png&container=blogger&gadget=a&rewriteMime=image%2F*)  
Warningのポップアップが出てくるので、Yesをクリックした後、Internet
Optionsの画面に戻るので、Applyをクリックした後、OKをクリックします。

その後Windows EC2内のファイヤーウォールの設定をします。  
まず最初のスタートページに戻り、今度はControl
Panelをクリックします。その後に設定項目が出るので、System and Security
\> Windows
Firewallを選択します（もし見つからなかったら、WF.mscというキーワードで検索してみてください）。



その後Advanced Settingsをクリックして設定画面を開きます。







![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F4.bp.blogspot.com%2F-x7FbDpy1gYU%2FU9w9WqMs9_I%2FAAAAAAAAcNU%2F65K4pZzuQU8%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.21.34.png&container=blogger&gadget=a&rewriteMime=image%2F*)  
Windows Firewall with Advanced
Securityという画面が出てくるので、左側メニューにあるInbound
Rulesを選択し、上のメニューバーからAction \> New
Rules\....をクリックします。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F4.bp.blogspot.com%2F-RUxe_9vM2ck%2FU9w-VEkROXI%2FAAAAAAAAcNg%2Fj7Jk9Kfj9GI%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.24.30.png&container=blogger&gadget=a&rewriteMime=image%2F*)


New Inbound Rule Wizardが出てくるので、Portを選択後、Next
を押して、TCPを選択し、Specific local ports; にて5001を入力します。

![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F3.bp.blogspot.com%2F-qpnOg81z9Ic%2FU9w-VC7VCjI%2FAAAAAAAAcNc%2FU4YOmJPu6lk%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.26.21.png&container=blogger&gadget=a&rewriteMime=image%2F*)  
次の画面で、Allow the connectionを選択します。  
その後、適応する箇所について聞かれるので、Doamin/Private/Public
全部を選びます。全部じゃなくてPublicだけでもいいのですが、何となく。  
最後は設定に名前を付けてFinish, 保存します。  
追加されました。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-o7AE5-OJALk%2FU9xBE0FnLDI%2FAAAAAAAAcNw%2FE1mS81vwd_k%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.37.56.png&container=blogger&gadget=a&rewriteMime=image%2F*)

[Windows EC2にアプリ設定をする]

次はiperfのダウンロードと、Javaのダウロードをして設定します。

[iperf]  
スタートページからIEに戻ってこちらのリンクにアクセスします。  
<https://code.google.com/p/xjperf/>  
このページのDownloads からFeatured jperf
iperfをダウンロードします（2014/8/2時点ではjperf-2.0.2.zipでした。  
<https://code.google.com/p/xjperf/downloads/list>  
ダウンロード後、zip解凍します。

[Java]  
次にJavaをダウンロードします。  
<http://www.java.com/ja/>  
上記ページにアクセスして、**あなたとJava**という文言に何とも言えない気持ちになりました。

ダウンロードするとThis PC \>
Downloadsに、JavaSetup7u65というファイルがダウンロードされるので、ダブルクリックしてインストールします。ウィザードが立ちあがりますが、基本はディフォルトでよいでしょう。

Javaインストール後、Pathの設定をする必要があります。これをしないとiperfを起動してもjavawがないと怒られます（ちなみにjavawを見た時、w-\>ﾜﾗの方がと思ってしまいました。javaﾜﾗ）  
参考リンク: <http://wp2.trojanbear.net/708.html>

スタートページからControl Panelに移動し、System and Security \> System
からbasic information about your computerの画面に遷移します。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-OFqZVAOC_6E%2FU9xDQtE-IjI%2FAAAAAAAAcN8%2FKb5KrdwLYTQ%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.45.49.png&container=blogger&gadget=a&rewriteMime=image%2F*)



↓  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F3.bp.blogspot.com%2F-VxAF15djZa0%2FU9xDQlhlH-I%2FAAAAAAAAcOE%2F4gCQmoig-9M%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.45.58.png&container=blogger&gadget=a&rewriteMime=image%2F*)





↓  
以下のChange
settingsをクリックします（随分分かり辛い場所にあると思いません？？）  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-3Fn2Ia0o7x0%2FU9xDQtstlfI%2FAAAAAAAAcOA%2F9D2D_2Rn798%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.46.09.png&container=blogger&gadget=a&rewriteMime=image%2F*)

System Properties画面が立ちがあるので、AdvancedタブにあるEnvironment
Variablesをクリックします。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F4.bp.blogspot.com%2F-ZFYX79DnTgc%2FU9xEL5W26eI%2FAAAAAAAAcOU%2F0jmgIaJO2cM%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.49.31.png&container=blogger&gadget=a&rewriteMime=image%2F*)  
Environment
Variables画面が出てくるので、TEMPをハイライトし、その下に出てくるSystem
variablesにあるPathを選択し、Editします。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-mBjHK7-Vu3Y%2FU9xF4mwr_3I%2FAAAAAAAAcOg%2F_ia3u4Tf5Ak%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B10.58.08.png&container=blogger&gadget=a&rewriteMime=image%2F*)





Pathの値の末尾に、Javaがインストールされたパスを書きます。多分こんな感じになるでしょう。  

> ;C:Program Files (x86)Javajre7bin

これで設定は終わりです。

[計測]

iperfを立ち上げます。クリックするとSecurity
Warningが出ますがRunさせます。  
起動させたら、Serverを選択し、Run iperfします。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-C31Cy285Cn4%2FU9xIYjXNFUI%2FAAAAAAAAcOs%2F_mu84NN2sWk%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B11.08.04.png&container=blogger&gadget=a&rewriteMime=image%2F*)  
手元にあるPCから接続をします。  
コマンドは  

> iperf -c Windows EC2の固定IP

です。このような感じになると思います。  
![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F3.bp.blogspot.com%2F-3Fth4RtNh50%2FU9xJojDRowI%2FAAAAAAAAcO4%2FBugMt4ziVqo%2Fs1600%2F%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2014-08-02%2B11.11.49.png&container=blogger&gadget=a&rewriteMime=image%2F*)

> aya-2:\~ komuro\$ iperf -c 54.210.217.54  
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  
> Client connecting to 54.210.217.54, TCP port 5001  
> TCP window size:  129 KByte (default)  
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  
> \[  4\] local 192.168.11.3 port 51824 connected with 54.210.217.54
> port 5001  
> \[ ID\] Interval       Transfer     Bandwidth  
> \[  4\]  0.0-14.3 sec  **15.2 MBytes  8.93 Mbits/sec**



今回Windows
EC2をUS-East-1に立てたので、東京リージョンよりは1/3ぐらいの速度かなぁと思いました。





後この検証している時、子どもが横でYoutube見ていたのでそれも影響しそうです。





朝3時に家族が寝ている時に同じ環境で検証したときは以下のような結果でした。



> aya-2:\~ komuro\$ iperf -c 54.210.217.54  
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  
> Client connecting to 54.210.217.54, TCP port 5001  
> TCP window size: 129 KByte (default)  
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  
> \[ 4\] local 192.168.11.3 port 61719 connected with 54.210.217.54 port
> 5001  
> \[ ID\] Interval Transfer Bandwidth  
> \[ 4\] 0.0-10.1 sec **20.6 MBytes 17.2 Mbits/sec**



ここまでやって思った事は毎度ですけど、サーバにGUIはどうしても慣れないなぁという事でした。サーバと思わないで全く違うものだと思って使えばいいのかもしれません。









何はともあれWindows Serverの勉強になりました！









今回参考になったページ



-   <http://onlineconsultant.jp/pukiwiki/?%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%AE%E9%80%9A%E4%BF%A1%E9%80%9F%E5%BA%A6%E3%82%92%E6%B8%AC%E5%AE%9A%E3%81%99%E3%82%8B>
-   <http://ameblo.jp/mac-begin3/entry-10768602467.html>
-   <http://wp2.trojanbear.net/708.html>
-   <http://inokara.hateblo.jp/entry/2014/01/03/105023>


