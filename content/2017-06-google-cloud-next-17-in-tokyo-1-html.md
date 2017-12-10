Title: [Google Cloud Next '17] GKE/機械学習/ネットワークインフラ技術セッションのメモ #googlenext17
Date: 2017-06-14 15:08
Authors: ayakomuro
Tags:  Google, googlenext
Slug:2017/06/google-cloud-next-17-in-tokyo-1
Status: published

Google Cloud Next '17 in Tokyoに参加した。

福岡からの参加だったので、残念ながら午前中の基調講演は聞き逃した。しょうがない。  
クラウド関連のイベントは大体出展側に居る事がほとんどだったし、今回はGoogleで専門外なので、初心者として参加中。

まず所感だけ言うと、楽しい。やっぱり知らない事を知るのは楽しいし、技術を使った事例を聞くだけでもこう言う使い方があるのか！とかニーズがあれば技術はあとで付いてくるんだな〜とか色々考える。

もっとみんな専門外の技術イベントに参加すればいいのにね。

以下は聞いたセッションのメモ(長い）

### Google Container Engine 入門 : ヒントとベスト プラクティス

Kubernetes　<https://kubernetes.io/>

-   Containerのオーケストレーションの仕組み
-   監視やスケーリングも一緒に出来るOSS
-   元々Google開発→OSSになった

ポッドとは

コンテナとボリュームの小さいなグループ

[Pods \|
Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/pod/#what-is-a-pod)

-   ポッドはEC2とEIPの組み合わせっぽい、と聞いてて思ったがドキュメント見たらやはり少し違うもののようだ
-   [Compare Kubernetes vs ECS (EC2 Container Service) \|
    Platform9 ](https://platform9.com/blog/compare-kubernetes-vs-ecs/)

デプロイメント（アプリを展開する）

-   アプリのインスタンスを作成・更新する

サービス

連動するポッドのグループ

-   ELBみたいなの。仮想IPを持つことができる
-   エンドユーザーから見たときのエンドポイントである

node

-   コンテナの単位

kubectl を使えば大体の事はできる（このセッションの結論）

-   debugも上記コマンドで可能

Horizontal pod autoscaler

レプリカを作りポッドを増加が可能

[Horizontal Pod Autoscaling \|
Kubernetes](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) 

Elastic Autoscaling の仕組みと似ている

-   min/max指定する等

こちらは人が任意に決める設定である

Cluster Autoscaler

スケジューラーがポッドにアサインができなくなると、新しいノードを作り、ポッドを作成する仕組み

自動で設定してくれる

-   Horizontal Pod Autoscalerが詰まっているとCluster
    Autoscalerが全体の調整をしてくれるイメージ

1分単位の課金らしい（すごい！

Kubernetes はDashboardもあるよ！

-   リアルタイムのモニタリング、ロギングも対応！

基本のトラブルシューティングは皆んな大好きStackDriverでみよう！

### 民主化が進む機械学習：すでに始まっている、Tensorflow を活用したビジネス活用事例のご紹介



人工知能：物事を賢くする技術 \>
機械学習：「学べる」コンピューターの作り方 \>
ニュートラルネットワーク：機械学習の手法の一つ

機械学習（ML)の三種の神器

-   ニューラルネットワーク（アルゴリズム）
-   豊富な計算資源（サーバー）
-   データ（データー）

それがある状態であるなどの人間の判断が必要な時はModelをtensorFlowを使って実装する

Google Machine Learning Engine is now GA provided by TensorFlow

キューピー事例

人＝知力と体力

知力の機械化

-   AI
-   人の気持ち、感情などは人が担う箇所

体力の機械化

-   ロボットなど

発想の逆転

-   不良品を除くのではなく、良品を選ぶような仕組みを実装

BrainPad

PoCを実施している模様

Find your candyはOSSで公開している

-   [BrainPad/FindYourCandy ](https://github.com/BrainPad/FindYourCandy)
-   機材に\$2500かかるけど頑張れば出来るよ！

転移学習（Transfer learning)

-   よく分からなかった。調べて見たらQiitaや多分以下の方の文献が多く引用されていたので、ここら辺から始めるのが良さげ
-   [発表文献 \| 神嶌 敏弘 ](http://www.kamishima.net/jp/happyo/)

密漁を調べる取り組み

-   船が出すGPS情報（AIS）を集めてする
-   沢山の情報をニューラルネットワークに入れて、最後は15種類の船に分類する

SMFG ＆JSOLにてクレジットカード不正利用防止のために機械学習を導入

-   確かPaypalも似たような事してたし、金融業界と機械学習は向いて居るかもしれない（のにあまり進まないのはなぜ）

将来のテーマとして財務パフォーマンス変化予測の検討

その他事例

アクサダイレクトなど、大きな損失を出す事故を予測出来ないか試しているらしい

-   事故を起こす可能性がある人は料金が高く、そうでないない人は料金を下げる仕組みなど

（未来への疑問）人間が絡む未来を予測する事と、現状がどうであるか識別する、という二つは確かにMLとかで取り組むことは出来るけど、その差異が縮まるのはいつぐらいなんだろう？

### Google のデータサイエンティストが語る現場で使える機械学習入門





MLとはルールベースで分類できない例外処理を人でなく技術で解決する

Machine Learning → Deep Learning

機械学習のステップ

-   人の判断の代替にはならないが、サイトの最適化などには向いている

目的を明確にする

データを集める

-   本当にデータは答えを導く上で必要なものなのか、確認
-   1回について1000行未満なら機械学習には向かない

データの前処理

-   列志向のデータに変える必要がある
-   前処理は全リソースの8割を消費する
-   君も前処理nistになろう

モデル学習とその方法

-   割愛

モデル学習のチューニング

-   機械学習はチューニングがないと完璧な結果を出さない

汎化精度

-   ノイズに振り回されず真のデータに最もよくフィットする事で、未知データに対して高い精度を発揮する度合い

検証

-   A/Bなど、ROIを見る
-   小さなところから始める

改善サイクル

-   機械学習モデルは時間とともに劣化する（つらたん

BigQuery + TensorFlowのデモ

Cloud DataLab

[Cloud Datalab - インタラクティブなデータ分析ツール  \|  Google
Cloud ](https://www.blogger.com/Platform%20https://cloud.google.com/datalab/)

-   ブラウザー内でPythonコードで機械学習ができるサービス
-   1時間デモでもよかったクオリティ

忘れがちだけどGoogleは広告会社

### Google Maps ビジネス事例：位置情報の有効活用で変わる生活



実は間違えて部屋に入ってしまったのだが結果オーライ

位置情報を使って、自動販売機の前でアプリ操作で商品を買うことができる

-   自動販売機にICカードやカード決済の機能をつけなくてもよい

[駐車場予約ならakippa \|
予約できるどこでも駐車場サービス](https://www.akippa.com/) 

### プリンシパル・ソフトウェアエンジニアが語る Google のネットワークインフラ技術





内部的ネットワークはあまり公開されていないが、実は（？）論文としては公開されているので論文を読むと論理上理解する事は可能

データセンターネットワーク

-   高速ネットワーク
-   Closトポロジー（L2ネットワーク
-   ハードも独自設計
-   ロードバランスのために経路情報（複数経路）をソフトで自動制御

B2ネットワーク

-   インターネットとの相互接続のためのグローバルなネットワーク

B4ネットワーク

データセンター間の相互接続するグルーバルな内部ネットワーク

OpenFlowを用いたトラフィックエンジニアリング（以後TE）によりパケットの優先順位に応じて送信を行う

-   このパケットの優先度が低いものはある程度のドロップを許容しているらしい

OpenFlowコントローラーがB4サイトスイッチを制御してグローバルな経路の最適化を実現

つまりDatacenters ars a computerなんだ！ :fumufumu:

-   詳しくはJupiter Rising読めよ

SDNベースのデータセンターネットワーク

Datacenter cluster

-   今まで余剰や足りてない箇所などデータセンターごとに偏りがあった  
   データセンターのクラスターに対しての帯域をSDN側で管理できるようにしたことによって活用ができるようになった(やったね！

Rack \< Edge Aggregation Block \<---\> Spine Block

ネットワークがスケールアウトするようにその下にあるものは全て拡張可能な状態にした

-   この図でぼんやり理解したが、Spine
    Blockが何をするのがイマイチ分からなかった。これがメッシュ構造でネットワークを拡張する部分だろうか？

ネットワーク自体はColsトポロジーを利用しメッシュ構造で拡張できるようにしている

2012年 1.3Pbps流している

-   👀💥

経路制御はFirepathで！

client (switch) link station \-\--物理的に接続\-\--master

FMRP protocol

-   これが何か分からなかった。
-   どうやらFirepath Master Redundancy Protocol (FMRP)の意味らしい
-   [Jupiter Rising: A Decade of Clos Topologies andCentralized Control
    in Google's Datacenter
    Network](https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p183.pdf)(PDF)

外部のルーターに関してはFirepath
clientに対してBGPも扱えるようにしている（ここがB2）

チップ上のバッファ容量不足の解決は、スイッッチ（ECN）とホスト（DCTCP)のチューニングを実施した

B4ができた理由としてはインターネットを使うだけでは難しいサービス（主に配信系、youtube等）が増えて来たため

-   B4ネットワークの使い方の私の理解==\>データを内部ネットワークで流して近くのインターネットから流す仕組みと思ったのだが間違っていたら教えて欲しい。

TEを使ったことによりSPFルーティングにおいて20％以上のスループット改善

論文読んでね！

Jupiter Rising

-   [Jupiter Rising: A Decade of Clos Topologies and Centralized Control
    in Google's Datacenter
    Network ](https://research.google.com/pubs/pub43837.html)

B4

-   [B4: Experience with a Globally-DeployedSoftware Defined
    WAN](https://people.eecs.berkeley.edu/~sylvia/cs268-2014/papers/b4-sigcomm13.pdf)(PDF)

BwE

-   [BwE: Flexible, Hierarchical Bandwidth Allocation forWAN Distributed
    Computing](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p1.pdf)(PDF)

Evolve or Die

-   [Evolve or Die: High-Availability Design Principles Drawn from
    Google\'s Network
    Infrastructure](https://research.google.com/pubs/pub45623.html)



### 今日のまとめ

-   どのセッションも盛り上がってて参加している方も楽しい
-   wifi欲しい
-   人の流れに文句を言っても多分しょうがない。それより有益なツイートしよう
-   顔認識勉強してQRコードスキャン無くしたい
-   浅草はカオスだった！
-   でも技術に希望も持てたしまだまだ楽しい事沢山あるなって実感した。
-   明日も楽しみ！
