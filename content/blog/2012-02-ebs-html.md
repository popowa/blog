Title: EBSのスナップショットについて
Date: 2012-02-12 00:55
Authors: ayakomuro
Tags:  Amazon, EBS
Slug:2012/02/ebs
Status: published

先日の \#jawsug 福岡の会で、  

[https://twitter.com/\#!/kaz\_goto/status/167571575296634881](https://twitter.com/#%21/kaz_goto/status/167571575296634881)

[![](http://2.bp.blogspot.com/-69900MMDsjE/TzXgL2bibrI/AAAAAAAAPMU/7bRhxxUO8UE/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-02-11+12.27.14%EF%BC%89.png)](http://2.bp.blogspot.com/-69900MMDsjE/TzXgL2bibrI/AAAAAAAAPMU/7bRhxxUO8UE/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%EF%BC%882012-02-11+12.27.14%EF%BC%89.png)

へーほーふー、知らなかったわーと思ってEBSのスナップショットだけにフォーカスして見ました。

記事

-   [Amazon Elastic Block Store (EBS)-\>日本語 by
    AWS](http://aws.amazon.com/jp/ebs/)
-   [Feature Guide: Elastic Block Store -\>英語 by
    AWS](http://aws.amazon.com/articles/1667)
-   [Amazon's Elastic Block Store explained -\>英語 by
    RightScale](http://blog.rightscale.com/2008/08/20/amazon-ebs-explained/)
-   [About Elastic Block Store (EBS) -\>英語 by
    RightScale](http://support.rightscale.com/12-Guides/Dashboard_Users_Guide/Clouds/AWS_Region/EBS_Volumes/Concepts/About_EBS_Volumes)

今更感なEBSの機能おさらい☆

-   外付け出来るブロックストレージ
-   1Gから1Tまでのストレージ領域を作成出来る
-   同じアベーラビリティゾーン内のインスタンスにマウント出来る
-   マウントしたインスタンスが落ちたら（障害なども含む）、勝手にアンマウントされる（はず）
-   好きなファイルフォーマット形式でフォーマットが出来る
-   作成したアベーラビリティゾーン内であれば、別のインスタンスにマウント出来る（EBSとインスタンスは絶対的な関係性が永続的にある訳ではない）
-   1EBSは1インスタンスにしかマウント出来ないが、1インスタンスは複数のEBSをマウント出来る
-   スナップショットをS3に取れる　\<== 気になる点！

EBSのスナップショットがS3に入るというのはどういう事なのでしょうか？

> Amazon EBS
> スナップショットは、最後にスナップショットを撮った時点から変更のあるブロックのみを保存する差分バックアップです。

 ん？Git的な感じなのかしら？と思って@kaz\_gotoさんが教えてくれたリンク、また検索などをして調べました。

簡単ですけど、こういう事らしいです。

☆初めてのわくわくドキドキのスナップショット ☆

1.  EBSを10Gで作ったとします。
2.  色々置いて4Gになりました☆(・ω\<)
3.  初めてのスナップショットでは、EBSでの使用分はブロックに分けられて、S3に全部コピー＆保存されます。
4.  保存されたブロックを管理するスナップショット管理表（=
    私たちが見るsnap-xxx）もS3に保存されます。

[![](http://1.bp.blogspot.com/-pXJCCaRHz8o/TzYOnIt3SOI/AAAAAAAAPM0/9sGhGGqK2-I/s1600/ebs_first_backup.png)](http://1.bp.blogspot.com/-pXJCCaRHz8o/TzYOnIt3SOI/AAAAAAAAPM0/9sGhGGqK2-I/s1600/ebs_first_backup.png)

☆2回目のスナップショット ☆

1.  前回から、4G中1Gを変更して、さらに新しく1G追加しました。
2.  ２回目のスナップショットでは、変更があった1G分のコピーを
    S3に取り、さらに新しく追加された1GもS3にコピーをとります。
3.  そして**スナップショット管理表2**を作成し、前回S3に保存したブロック先３つ（以下の絵だと黄、緑、ピンク）と、変更、新規追加で作成したブロック先を一覧にしてS3に保存します。

[![](http://4.bp.blogspot.com/-yFjr6cHvHeI/TzYOeigc3MI/AAAAAAAAPMc/58YdqDH_lAU/s640/ebs_second_backup.png){width="640"
height="506"}](http://4.bp.blogspot.com/-yFjr6cHvHeI/TzYOeigc3MI/AAAAAAAAPMc/58YdqDH_lAU/s1600/ebs_second_backup.png)

☆3回目のスナップショット ☆

1.  前回(2回目)から、5G中1G削除しました。
2.  最初に配置した緑、ピンク、２回目に配置した青、紫を一覧にした**スナップショット管理表3**を作成しS3に保存します。

[![](http://3.bp.blogspot.com/-AFpvbcqjSvA/TzYOfwo-rBI/AAAAAAAAPMk/kYrkdJktXw8/s640/ebs_third_backup.png){width="640"
height="340"}](http://3.bp.blogspot.com/-AFpvbcqjSvA/TzYOfwo-rBI/AAAAAAAAPMk/kYrkdJktXw8/s1600/ebs_third_backup.png)

 特記すべき点

-   私たちがAPIで見ているスナップショット(例えば**snap-xxxxx**)は、実際にS3に配置されているバックアップされたデータブロックへのポインタ一覧である
-   S3に取られたスナップショット単体を見る事が出来ない。S3のAPIではアクセスが不可能。EC2のAPI越しにスナップショットの詳細や、ボリューム作成を行う必要がある 
-   最初のスナップショットを消しても、保存したブロックを必要としている別のスナップショットがあれば削除されない。
-   上記の逆を返すとどのスナップショットにも必要とされていないブロックは、紐付けようがないので削除される
-   ~~1インスタンスにマウント出来るEBSは20まで。（AWSに依頼すれば解除してくれる）~~
-   ~~[
    ]~~[1インスタンスに何個でもマウント出来る！\<-
    new]
-   [Windowsインスタンスは12個上限でEBSをマウント出来る。\<-
    new]
-   1インスタンスに10個以上のEBSをマウントするのはよくない by RightScale
-   1AWSアカウントで作れるスナップショットは、500まで（AWSに依頼すれば解除してくれる）
-   EBS側を削除しても、それに紐づくスナップショットが勝手に消えてくれる訳ではないらしい
-   1ブロックの詳細は公表されていないらしく、n回目のスナップショットでどれだけS3のスペースを使うか分からないそう。逆にどれだけスナップショットを削除したら節約出来るかが明確に分からないらしい
-   S3に保存されるデータは圧縮されている
-   EBSのスナップショットを作成している時はEBSのバックグラウンドで稼働し、マウントしているインスタンスには影響がない

データーベースをEBS上で稼働させている場合

-   EBSのスナップショットは非同期で行われるため、スナップショットが取られた瞬間に書き込みが発生すると誤差が生じる場合がある
-   RightScaleお勧めの方法としては、DBやファイルシステムを止める-\>スナップショット-\>再開、という方法がよいらしい

RightScaleのお勧めファイルフォーマット形式はxfs  
xfsには、I/O処理を停止する機能が付いているのでそれを使うと楽との事。  
XFS単体での停止方法の例：  

> xfs\_freeze -f \<mount-point\>
> \#実行中の処理が終わった後は新規書き込みは行われない  
> ec2-create-snapshot \<volume\>  
> xfs\_freeze -u \<mount-point\>  \#再開する

   
LVMとかを使用していたら:  

> dmsetup suspend \<device\>  
> ec2-create-snapshot \<volume\>  
> dmsetup resume \<device\>


なるほどー  
I/Oが高いデータベースとかをEBSに置いてスナップショットを取っている場合は、きちんと取れるように気をつけないとですね。

そう考えるとRDSのスナップショットも気になりますよね。どうなっているのかしら。  
想像だけどRDSは多分内部EC2 on
EBS上に構築されているのではないかしら、と思っているので、RDSのスナップショットもやはりS3?  
気になる木。

という訳でEBSのスナップショットについてでしたー！

これ違うよーというのがあればご指摘くださいm(\_ \_)m

追記2012/2/13:  
EBSのマウント数は、Windowsだと12個まで、それ以外では無制限だそうです！  
（赤で追記）  
<http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html>
