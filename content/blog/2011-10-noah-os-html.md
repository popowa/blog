Title: 
Date: 2011-10-03 21:23
Authors: ayakomuro
Tags:  Noah cloud
Slug:2011/10/noah-os
Status: published


提供OS一覧と仮想マシン起動フロー+Noahクラウドに登録したら、早速インスタンスを立ち上げてみよう！という事で、どんなOS（テンプレートと言うらしいです）が提供されているのか見てみました。

[]ホームのクイックスタート、か

[![](http://1.bp.blogspot.com/-JQTq68zY0r8/TooW0pRYNKI/AAAAAAAANkE/6E9dz8ibS3k/s1600/quickstart.png)](http://1.bp.blogspot.com/-JQTq68zY0r8/TooW0pRYNKI/AAAAAAAANkE/6E9dz8ibS3k/s1600/quickstart.png)

サービス \>\>
仮想マシン、をクリックするとテンプレート一覧ページに遷移します。

[![](http://3.bp.blogspot.com/-M4y0vqfZVWc/TooW9VwcbKI/AAAAAAAANkI/aeSpVJsYJlk/s400/template.png){width="400"
height="93"}](http://3.bp.blogspot.com/-M4y0vqfZVWc/TooW9VwcbKI/AAAAAAAANkI/aeSpVJsYJlk/s1600/template.png)

 現在のテンプレートには

-   NOAHテンプレート
-   マイテンプレート
-   コミュニティテンプレート
-   ISO

があるようで、コミュニティテンプレートはまだオープンしてないようです。今後色々カスタマイズされたテンプレートが出てくるんでしょうね。期待したい所です♩ISOはISOファイルをアップすればいいのかな。ちょっと使い方が分かりませんでした。要調査。

NOAHテンプレートには現在2011/10/4時点で以下のOSがありました。

CentOS 5.6 32-bit

-   Root Disk: 15 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0)

CentOS 5.6 64-bit

-   Root Disk: 15 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0)

CentOS 6.0 64-bit

-   Root Disk: 15 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0) 

Ubuntu Server 10.04.03 LTS 64-bit

-   Root Disk: 15 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0)

Microsoft Windows Server 2003 R2 Enterprise with SP2 32-bit

-   Root Disk: 40 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0)

Microsoft Windows Server 2008 R2 Enterprise with SP1

-   Root Disk: 40 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0)

Red Hat Enterprise Linux 5.7 32-bit

-   Root Disk: 15 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0)

Red Hat Enterprise Linux 5.7 64-bit

-   Root Disk: 15 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0)

Red Hat Enterprise Linux 6.1 64-bit

-   Root Disk: 15 GB, (NOAHv1.0)
-   Dedicated Hardware, Root Disk: 200 GB, (NOAHv1.0)

NOAHテンプレート概要は上記な感じですが、並び順がバラバラなので、ソート出来たらいいなと思いました。  
Ubuntuを選択すると、サイズを選択する画面に遷移します。サイズはXS\~DL32まであるようです（[基本サービス](http://www.idcf.jp/noah/service/)）

[![](http://1.bp.blogspot.com/-FFbQ131mErU/Took8XdqM7I/AAAAAAAANkM/pDVLNUEgtrA/s400/size.png){width="400"
height="168"}](http://1.bp.blogspot.com/-FFbQ131mErU/Took8XdqM7I/AAAAAAAANkM/pDVLNUEgtrA/s1600/size.png)

希望のサイズを選択すると追加ディスクを選択出来ます。

[![](http://3.bp.blogspot.com/-4KtAEAA-SG0/ToolOiVp6xI/AAAAAAAANkQ/nl-LP4m_Tck/s400/disk.png){width="400"
height="70"}](http://3.bp.blogspot.com/-4KtAEAA-SG0/ToolOiVp6xI/AAAAAAAANkQ/nl-LP4m_Tck/s1600/disk.png)

 詳細情報入力画面では、仮想マシンの名前、所属するグループ、そしてSSHの紐付けを行う事が出来ます。  
仮想マシン名に入力すると１仮想マシン名にも自動で入るのですが、この二つの違いはよく分かりませんでした。多分複数台作成の時にhoge1,
hoge2という感じで簡単に作れる機能なんだろうと思います。

[![](http://1.bp.blogspot.com/--rEBUNtDIHw/ToomN6Cv-nI/AAAAAAAANkU/1EKHmalTHcM/s400/numofserver.png){width="400"
height="101"} ](http://1.bp.blogspot.com/--rEBUNtDIHw/ToomN6Cv-nI/AAAAAAAANkU/1EKHmalTHcM/s1600/numofserver.png)

SSH鍵は無ければ新規生成、既存の物をアップロード、が出来ます。

[![](http://4.bp.blogspot.com/-xVz4dc29PgE/ToomyYvZNWI/AAAAAAAANkg/UteqaSsZ0L4/s320/selectssh.png){width="320"
height="171"}](http://4.bp.blogspot.com/-xVz4dc29PgE/ToomyYvZNWI/AAAAAAAANkg/UteqaSsZ0L4/s1600/selectssh.png)

SSH鍵生成を選択すると、以下の画像の様にprivate
keyがテキストエリアに表示されるので、コピペして、テキストファイルに張り付け-\>
hoge.pemなどの名前で保存します。


[![](http://4.bp.blogspot.com/-nTaAnNPoFeA/ToonVEVPr5I/AAAAAAAANkk/R7LzpOySD9M/s400/ssh.jpg){width="400"
height="80"}](http://4.bp.blogspot.com/-nTaAnNPoFeA/ToonVEVPr5I/AAAAAAAANkk/R7LzpOySD9M/s1600/ssh.jpg)


 今まで選択して来た項目の一覧が表示され、重要項目ならびに契約約款に同意した後、仮想サーバを立てる事が出来ます。

[![](http://2.bp.blogspot.com/-JUOfotDcj9U/ToosmTxbj1I/AAAAAAAANko/bLd15A_KDYk/s320/done.jpg){width="320"
height="44"}](http://2.bp.blogspot.com/-JUOfotDcj9U/ToosmTxbj1I/AAAAAAAANko/bLd15A_KDYk/s1600/done.jpg)

 出来ました！
