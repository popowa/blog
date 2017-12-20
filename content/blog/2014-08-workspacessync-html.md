Title: WorkSpacesにSyncを使う
Date: 2014-08-05 21:29
Authors: ayakomuro
Tags:  sync, workspaces
Slug:2014/08/workspacessync
Status: published

最近WorkSpacesを使う事がやたら多くなった小室です。  

今日はSync入れたログ書いておきます。

[事前準備]

まずこちらのドキュメントに目を通しておきます。  
<http://docs.aws.amazon.com/workspaces/latest/adminguide/sync_client_help.html>

必要な物

WorkSpace

PC(以下のどれかのOSであること）

-   Windows 7
-   Windows 8 以降〜
-   Windows Server 2008
-   Mac 製品でOSがMax OS X 10.7かそれ以降〜

[アプリのダウンロード]

以下のサイトにアクセスをしてSyncアプリをダウンロードします。

<https://sync.amazonworkspaces.com/>

[![](http://1.bp.blogspot.com/-zjfcr5HaAq0/U-CSPh0acCI/AAAAAAAAcPo/6NUSKV3K2S4/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+17.13.24.png){width="640"
height="350"}](http://1.bp.blogspot.com/-zjfcr5HaAq0/U-CSPh0acCI/AAAAAAAAcPo/6NUSKV3K2S4/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+17.13.24.png)

インストール時のエラーは末尾に載せてます。

[インストール]

さてダウンロードした後、Syncをインストールします。Macの場合はAmazonWorkSpacesSync.dmgというのがダウンロードされるので、クリックしたらこのようなよく見るアイコンをApplicationsフォルダーに入れろ、というのが出てきます。このフォルダーの背景よく見たら色々オフィス系のガジェットとかサービスのアイコンが載っていて可愛いですね。

[![](http://1.bp.blogspot.com/-xWm9ATihVSk/U-CWm1S5MpI/AAAAAAAAcQA/SEy04KnPoho/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+17.30.55.png)](http://1.bp.blogspot.com/-xWm9ATihVSk/U-CWm1S5MpI/AAAAAAAAcQA/SEy04KnPoho/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+17.30.55.png)

[設定]

設定する事はローカル、およびWorkSpaces側でSyncアプリを入れて設定する必要があります。なので以下の作業は二回行います。

Syncのアイコンをダブルクリックします。

+-----------------------------------+-----------------------------------+
| （Applicationフォルダーにあります）\ | gn: center;"}                  |
| ![](https://images-blogger-openso |                                   |
| s/proxy?url=http%3A%2F%2F2.bp.blo | gn: left;"}                       |
| gspot.com%2F-XK7LAwXzmGE%2FU-CW_t | WorkSpaces側にあるアイコン        |
| %2Fs1600%2F%25E3%2582%25B9%25E3%2 |                                   |
| 582%25AF%25E3%2583%25AA%25E3%2583 | （デスクトップにあります）        |
| %25BC%25E3%2583%25B3%25E3%2582%25 |                                   |
| 25E3%2583%2588%2B2014-08-05%2B17. | gn: center;"}                     |
| 33.26.png&container=blogger&gadge | [![](http://4.bp.blogspot.com/-gU |
| t=a&rewriteMime=image%2F*)        | vNcRJhohk/U-FE9DS_6eI/AAAAAAAAcRM |
|                                   | /2k72wqiEVZY/s1600/%E3%82%B9%E3%8 |
|                                   | 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E |
|                                   | 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 |
|                                   | 8+2014-08-05+18.14.11.png)](http: |
|                                   | //4.bp.blogspot.com/-gUvNcRJhohk/ |
|                                   | U-FE9DS_6eI/AAAAAAAAcRM/2k72wqiEV |
|                                   | ZY/s1600/%E3%82%B9%E3%82%AF%E3%83 |
|                                   | %AA%E3%83%BC%E3%83%B3%E3%82%B7%E3 |
|                                   | %83%A7%E3%83%83%E3%83%88+2014-08- |
|                                   | 05+18.14.11.png)                  |
+-----------------------------------+-----------------------------------+
| スクショ忘れましたが、インターネットからダウンロードしたアプリだけ | 実行するか聞かれるかもしれません。 |
| ど実行する？と聞かれます。        |                                   |
|                                   |                                   |
|                                   | gn: center;"}                     |
|                                   | [\                                |
|                                   | ]     |
|                                   |                                   |
|                                   | gn: center;"}                     |
|                                   | [![](http://4.bp.blogspot.com/-3Y |
|                                   | PceYSVg8U/U-FGCkLn2SI/AAAAAAAAcRU |
|                                   | /cxKoNALW0fA/s1600/%E3%82%B9%E3%8 |
|                                   | 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E |
|                                   | 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 |
|                                   | 8+2014-08-05+18.14.21.png){width= |
|                                   | "320"                             |
|                                   | height="237"}](http://4.bp.blogsp |
|                                   | ot.com/-3YPceYSVg8U/U-FGCkLn2SI/A |
|                                   | AAAAAAAcRU/cxKoNALW0fA/s1600/%E3% |
|                                   | 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% |
|                                   | E3%83%B3%E3%82%B7%E3%83%A7%E3%83% |
|                                   | 83%E3%83%88+2014-08-05+18.14.21.p |
|                                   | ng)                               |
+-----------------------------------+-----------------------------------+
|                                   | このような感じでファイルのダウンロードが\... |
|                                   |                                   |
|                                   |                                   |
|                                   | gn: center;"}                     |
|                                   | [![](http://2.bp.blogspot.com/-n3 |
|                                   | PZL6Adih4/U-FGebEyUQI/AAAAAAAAcRc |
|                                   | /5LU9Y2wki5s/s1600/%E3%82%B9%E3%8 |
|                                   | 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E |
|                                   | 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 |
|                                   | 8+2014-08-05+18.14.36.png){width= |
|                                   | "320"                             |
|                                   | height="184"}](http://2.bp.blogsp |
|                                   | ot.com/-n3PZL6Adih4/U-FGebEyUQI/A |
|                                   | AAAAAAAcRc/5LU9Y2wki5s/s1600/%E3% |
|                                   | 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% |
|                                   | E3%83%B3%E3%82%B7%E3%83%A7%E3%83% |
|                                   | 83%E3%83%88+2014-08-05+18.14.36.p |
|                                   | ng)                               |
+-----------------------------------+-----------------------------------+
| するとWorkSpaces Sync             | インストール画面は同じですね。    |
| accountはすでに準備済みだ！と出てきます。どういう事でしょう |         |
| しょうか。。？\                   | gn: center;"}                     |
| juCfAgMWU/U-CXW6r58wI/AAAAAAAAcQQ |                                   |
| 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E | gn: center;"}                     |
| 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 | [![](http://4.bp.blogspot.com/-iq |
| 8+2014-08-05+17.34.11.png){width= | CnsHIc1ww/U-FG1e0Gs4I/AAAAAAAAcRs |
| "320"                             | /KvzIp2Xlp_Q/s1600/%E3%82%B9%E3%8 |
| height="243"}](http://4.bp.blogsp | 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E |
| ot.com/-dzjuCfAgMWU/U-CXW6r58wI/A | 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 |
| AAAAAAAcQQ/Mgh3PewnkOE/s1600/%E3% | 8+2014-08-05+18.16.09.png){width= |
| 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% | "320"                             |
| E3%83%B3%E3%82%B7%E3%83%A7%E3%83% | height="222"}](http://4.bp.blogsp |
| 83%E3%83%88+2014-08-05+17.34.11.p | ot.com/-iqCnsHIc1ww/U-FG1e0Gs4I/A |
| ng)                               | AAAAAAAcRs/KvzIp2Xlp_Q/s1600/%E3% |
|                                   | 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% |
|                                   | E3%83%B3%E3%82%B7%E3%83%A7%E3%83% |
|                                   | 83%E3%83%88+2014-08-05+18.16.09.p |
|                                   | ng)                               |
+-----------------------------------+-----------------------------------+
| レジストレーションコードを登録します。\ | レジストレーションコードを登録します。 |
|                                   |                                   |
| （右に同じ）                      |                                   |
|                                   | gn: center;"}                     |
|                                   | [![](http://2.bp.blogspot.com/-M1 |
|                                   | kqCIc3Thg/U-FHCJX9dvI/AAAAAAAAcR0 |
|                                   | /m9gWPoYkiks/s1600/%E3%82%B9%E3%8 |
|                                   | 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E |
|                                   | 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 |
|                                   | 8+2014-08-05+18.17.20.png){width= |
|                                   | "320"                             |
|                                   | height="223"}](http://2.bp.blogsp |
|                                   | ot.com/-M1kqCIc3Thg/U-FHCJX9dvI/A |
|                                   | AAAAAAAcR0/m9gWPoYkiks/s1600/%E3% |
|                                   | 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% |
|                                   | E3%83%B3%E3%82%B7%E3%83%A7%E3%83% |
|                                   | 83%E3%83%88+2014-08-05+18.17.20.p |
|                                   | ng)                               |
+-----------------------------------+-----------------------------------+
| WorkSpacesのユーザー名とパスワードを設定します。\ | WorkSpacesのユーザー名とパスワードを設定します（自身がW |
|                                   | orkSpaces内にいるのに？と不思議でした。ここら辺のからくり |
| （右に同じ）                      | はもう少し調べたい）。            |
|                                   |                                   |
|                                   | gn: center;"}                     |
|                                   | [![](http://3.bp.blogspot.com/-X0 |
|                                   | i5gL4_9oQ/U-FIq1KvmDI/AAAAAAAAcSc |
|                                   | /SJj-Rx1VqQY/s1600/%E3%82%B9%E3%8 |
|                                   | 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E |
|                                   | 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 |
|                                   | 8+2014-08-05+18.25.15.png){width= |
|                                   | "320"                             |
|                                   | height="176"}](http://3.bp.blogsp |
|                                   | ot.com/-X0i5gL4_9oQ/U-FIq1KvmDI/A |
|                                   | AAAAAAAcSc/SJj-Rx1VqQY/s1600/%E3% |
|                                   | 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% |
|                                   | E3%83%B3%E3%82%B7%E3%83%A7%E3%83% |
|                                   | 83%E3%83%88+2014-08-05+18.25.15.p |
|                                   | ng)                               |
+-----------------------------------+-----------------------------------+
| するとどのフォルダーと同期をとるか聞かれるので、好きな場所に変更し | WorkSpaces内のどのフォルダーと共有するか設定します。 |
| ましょう。Changeからフォルダー指定が出来ます。 |                      |
|                                   |                                   |
| [![](http://1.bp.blogspot.com/-Yb | gn: center;"}                     |
| zhS53rL2E/U-CdoFq9BRI/AAAAAAAAcQg | [![](http://3.bp.blogspot.com/-l_ |
| /VF2J9tUtmLo/s1600/%E3%82%B9%E3%8 | M1fwsQSS8/U-FJEHhfeaI/AAAAAAAAcSk |
| 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E | /9qy2jOE4IOs/s1600/%E3%82%B9%E3%8 |
| 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 | 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E |
| 8+2014-08-05+17.50.59.png){width= | 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 |
| "320"                             | 8+2014-08-05+18.26.03.png){width= |
| height="245"}](http://1.bp.blogsp | "320"                             |
| ot.com/-YbzhS53rL2E/U-CdoFq9BRI/A | height="120"}](http://3.bp.blogsp |
| AAAAAAAcQg/VF2J9tUtmLo/s1600/%E3% | ot.com/-l_M1fwsQSS8/U-FJEHhfeaI/A |
| 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% | AAAAAAAcSk/9qy2jOE4IOs/s1600/%E3% |
| E3%83%B3%E3%82%B7%E3%83%A7%E3%83% | 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% |
| 83%E3%83%88+2014-08-05+17.50.59.p | E3%83%B3%E3%82%B7%E3%83%A7%E3%83% |
| ng)                               | 83%E3%83%88+2014-08-05+18.26.03.p |
|                                   | ng)                               |
+-----------------------------------+-----------------------------------+
|                                   | gn: center;"}                     |
| [![](http://2.bp.blogspot.com/-dC | [![](http://3.bp.blogspot.com/-Xm |
| JZHJfnxxs/U-CdoRGHlfI/AAAAAAAAcQk | JQ_Iqsdsw/U-FJMmTfQFI/AAAAAAAAcSs |
| /v4y1rryxT6o/s1600/%E3%82%B9%E3%8 | /rxSJIS7IMuA/s1600/%E3%82%B9%E3%8 |
| 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E | 2%AF%E3%83%AA%E3%83%BC%E3%83%B3%E |
| 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 | 3%82%B7%E3%83%A7%E3%83%83%E3%83%8 |
| 8+2014-08-05+17.51.50.png){width= | 8+2014-08-05+18.26.45.png)](http: |
| "320"                             | //3.bp.blogspot.com/-XmJQ_Iqsdsw/ |
| height="168"}](http://2.bp.blogsp | U-FJMmTfQFI/AAAAAAAAcSs/rxSJIS7IM |
| ot.com/-dCJZHJfnxxs/U-CdoRGHlfI/A | uA/s1600/%E3%82%B9%E3%82%AF%E3%83 |
| AAAAAAAcQk/v4y1rryxT6o/s1600/%E3% | %AA%E3%83%BC%E3%83%B3%E3%82%B7%E3 |
| 82%B9%E3%82%AF%E3%83%AA%E3%83%BC% | %83%A7%E3%83%83%E3%83%88+2014-08- |
| E3%83%B3%E3%82%B7%E3%83%A7%E3%83% | 05+18.26.45.png)                  |
| ng)                               |                                   |
+-----------------------------------+-----------------------------------+



[使ってみる]

WorkSpacesにログインします。Workspaces \<\-\--\>
ローカルPCで同期が取られるはずです。

また同期が取られないファイルは以下の通りです。

ピリオド(\".\")で始まるファイル（例：\".lock\", \".\~doctor.ppt\")

ティルダ(\"\~\")で始まる/終わるファイル（例：\"hello.txt\~\",
\"\~WRD0000.tmp\")

\".tmp\"という拡張子で終わるファイル（例：\"pptC407.tmp\",
\"\~WRD0000.tmp\")

以下の予約語と同じ名前で作られたファイル（完全一致です）

-   Microsoft User Data
-   Outlook Files

128文字数よりも長いファイル、もしくはフォルダー（以下例）

-   Documents/file name longer than 128 characters.txt
-   Documents/folder name longer than 128 characters/file.txt

以下の文字を含むファイルもしくはフォルダー

-   \*/:\<\>?\|\"
-   character code 202Eh

\".\"か\"..\"に一致するファイル、もしくはフォルダー

まだローカルにも入っていません。

[![](http://3.bp.blogspot.com/-21lyu4r1hww/U-CfzuIgVMI/AAAAAAAAcQ8/03lkm9NWNzo/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.11.00.png)](http://3.bp.blogspot.com/-21lyu4r1hww/U-CfzuIgVMI/AAAAAAAAcQ8/03lkm9NWNzo/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.11.00.png)

WorkSpaces \-\--\>
ローカルにファイルを置いてみたら5秒もしないうちにデータが落ちてきました。

[![](http://2.bp.blogspot.com/-w4LQf4bgGRQ/U-FJchN7zNI/AAAAAAAAcS0/MH4NXHugeKQ/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.29.08.png){width="640"
height="201"}](http://2.bp.blogspot.com/-w4LQf4bgGRQ/U-FJchN7zNI/AAAAAAAAcS0/MH4NXHugeKQ/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.29.08.png)

ローカル \--\>  WorkSpacesにファイルを置いたみたら大体10秒ぐらいでした。

[![](http://3.bp.blogspot.com/-DiOhrfR8wMQ/U-FKfw9yn_I/AAAAAAAAcS8/1rKczrC40VU/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-06+6.19.22.png){width="640"
height="200"}](http://3.bp.blogspot.com/-DiOhrfR8wMQ/U-FKfw9yn_I/AAAAAAAAcS8/1rKczrC40VU/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-06+6.19.22.png)

そこでローカル\<\-\--\>
WorkSpacesで同じファイルを操作した場合、どちらが勝つのかをやってみたら、同じファイルの更新日が先の方が上書きされていました。なのでDropboxみたいに、コンフリクト時に別のファイルとして生成する仕組みはないようです。

後どうでも良い事ですがSyncを動かしているとこのようなアイコンが表示されます。

[![](http://3.bp.blogspot.com/-UfBsGtMTNgk/U-FMIFJ6DkI/AAAAAAAAcTI/_hDwQpOd7PA/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-06+6.26.18.png)](http://3.bp.blogspot.com/-UfBsGtMTNgk/U-FMIFJ6DkI/AAAAAAAAcTI/_hDwQpOd7PA/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-06+6.26.18.png)

それからWorkSpacesに接続している時のSession
Laggyというのは見ている限り、WorkSpacesの転送速度を測るにはよいアイコンに見えますがもうちょっと分かり易いアイコンの方がよいと思いました。緑だといい感じで、黄色？になると遅い事を意味する様です。

[![](http://1.bp.blogspot.com/-t8cbhRiDddY/U-FMWb6WZBI/AAAAAAAAcTQ/qckTymHu-7I/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.23.38.png)](http://1.bp.blogspot.com/-t8cbhRiDddY/U-FMWb6WZBI/AAAAAAAAcTQ/qckTymHu-7I/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.23.38.png)

以下はエラー対応についてです。

[アプリダウンロード時にエラー]

この時もし利用しているネットワークがプロキシー認証をしている場合はエラーになります。このような感じです。

[![](http://2.bp.blogspot.com/-yovnG52IGDQ/U-CUCy7zy-I/AAAAAAAAcP0/kLdB_Z8YEms/s1600/%E3%82%A8%E3%83%A9%E3%83%BC%EF%BC%92.png)](http://2.bp.blogspot.com/-yovnG52IGDQ/U-CUCy7zy-I/AAAAAAAAcP0/kLdB_Z8YEms/s1600/%E3%82%A8%E3%83%A9%E3%83%BC%EF%BC%92.png)

エラーログもこんな感じ（だそうです  

> The following properties have been set:  
> Property: \[AdminUser\] = true   
> Property: \[InstallMode\] = HomeSite   
> Property: \[NTProductType\] = 1   
> Property: \[ProcessorArchitecture\] = Intel   
> Property: \[VersionNT\] = 6.1.1   
> Running checks for package \'Microsoft .NET Framework 4.5 (x86 and
> x64)\', phase BuildList  
> Reading value \'Version\' of registry key \'HKLMSoftwareMicrosoftNET
> Framework SetupNDPv4Full\'  
> Read string value \'4.5.50709\'  
> Setting value \'4.5.50709 \' for property
> \'DotNet45Full\_TargetVersion\'  
> The following properties have been set for package \'Microsoft .NET
> Framework 4.5 (x86 and x64)\':  
> Property: \[DotNet45Full\_TargetVersion\] = 4.5.50709   
> Running checks for command
> \'DotNetFX45dotNetFx45\_Full\_x86\_x64.exe\'  
> Result of running operator \'ValueEqualTo\' on property
> \'InstallMode\' and value \'HomeSite\': true  
> Result of checks for command
> \'DotNetFX45dotNetFx45\_Full\_x86\_x64.exe\' is \'Bypass\'  
> Running checks for command \'DotNetFX45dotNetFx45\_Full\_setup.exe\'  
> Result of running operator \'ValueNotEqualTo\' on property
> \'InstallMode\' and value \'HomeSite\': false  
> Result of running operator \'VersionGreaterThanOrEqualTo\' on property
> \'DotNet45Full\_TargetVersion\' and value \'4.5.50709\': true  
> Result of checks for command \'DotNetFX45dotNetFx45\_Full\_setup.exe\'
> is \'Bypass\'  
> \'Microsoft .NET Framework 4.5 (x86 and x64)\' RunCheck result: No
> Install Needed  
> Launching Application.  
> URLDownloadToCacheFile failed with HRESULT \'-2147024891\'  
> Error: An error occurred trying to download
> \'http://s3.amazonaws.com/ws-sync/win/1\_0\_83\_0/AmazonWorkSpacesSync.application\'.

このようなエラーが出た場合は、プロキシー認証がないネットワークにいく以外方法はないそうです。それかWorkSpaces,
Syncがそれに対応するのを待つか、こちらの方法もあるようです（未検証：<http://www.0x00.to/post/2012/12/31/How-to-use-ClickOnce-with-proxy-authentication>）

[インストール時にエラーの場合]



裏で利用するブラウザーの設定によっては途中でエラーが出るかもしれません。てか最初は必ず出ると思います。（WorkSpacesの事前の設定でしてくれてたらいいのに。。。）

[![](http://2.bp.blogspot.com/-HmHdZrIQaWQ/U-FHURM9EnI/AAAAAAAAcR8/TbPSq3ivDOE/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.18.03.png)](http://2.bp.blogspot.com/-HmHdZrIQaWQ/U-FHURM9EnI/AAAAAAAAcR8/TbPSq3ivDOE/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.18.03.png)

\"Your web browser must have JavaScript enabled in order for this
application to display correctly\"  
そういう場合はWorkSpacesの場合、IEを立ち上げ歯車アイコンをクリックし、Internet
Optionsを選びます。

[![](http://2.bp.blogspot.com/-_bQzP6pLhxI/U-FHrbLjA1I/AAAAAAAAcSE/vupb3y79OAE/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.18.26.png)](http://2.bp.blogspot.com/-_bQzP6pLhxI/U-FHrbLjA1I/AAAAAAAAcSE/vupb3y79OAE/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.18.26.png)

その後Security \> Internet \> Custom level を選択します。

[![](http://1.bp.blogspot.com/-G4Hd2tYv4Zk/U-FIA7hE-7I/AAAAAAAAcSM/8WNRx9a40Yo/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.18.47.png)](http://1.bp.blogspot.com/-G4Hd2tYv4Zk/U-FIA7hE-7I/AAAAAAAAcSM/8WNRx9a40Yo/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.18.47.png)

設定でScripting \> Active scripting \> Enable を選択し、OKにします。

[![](http://1.bp.blogspot.com/-vzql92SfefE/U-FIRQLGj4I/AAAAAAAAcSU/BgUBCc-2kQY/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.20.08.png)](http://1.bp.blogspot.com/-vzql92SfefE/U-FIRQLGj4I/AAAAAAAAcSU/BgUBCc-2kQY/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2014-08-05+18.20.08.png)


