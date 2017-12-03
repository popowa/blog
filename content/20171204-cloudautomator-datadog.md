Title: CloudAutomatorとDatadogを連携して障害時にメンテナンスサーバーへ自動で変更する
Date: 2017-12-2 21:39
Modified: 2010-12-05 19:30
Category: tech
Tags: cloudAutomator, datadog
Slug: cloudAutomator-n-datadog
Authors: ayakomuro
Summary: CloudAutomatorとDatadogを連携させて障害時のメンテナンスサーバーへ自動でリダイレクトさせる方法

 この記事はCloud Automator Advent Calendar 2017の4日目の記事です。
 せっかくなのでPelican + S3 + Githubでブログも移行してみました。残りのコンテンツは後ほどがががっとあげようと思います。

さてみんな大好きCloudAutomator とDatadogですが、私が一番好きな機能はそれぞれ

- CloudAutomator : Route53の値を変更する
- Datadog:インテグレーション機能が多い

という所です。
そこで今回は私が好きなサービス二つを掛け合わせます。
##　今回やる構成



## CloudAutomatorでジョブを作成する

CloudAutomatorにはトリガーにHTTPがあります。

[Cloud Automator | HTTPトリガーをリリースしました](https://cloudautomator.com/blog/2014/08/13/http-trigger-release/)

これを使えばHTTPを叩く事でジョブを実行出来るのです。作り方は上記のリンクをみていただくと分かるので、
ここでは割愛します。CloudAutomatorはジョブ作るの簡単すぎるので、あんまり書く事ないんですよね・・w

作成したジョブのこのデータを取得します。

```sh
$ curl https://manager.cloudautomator.com/trigger/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
>   -X POST \
>   -H "Authorization: CAAuth xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
>   -H "Content-Length: 0"
```

ここの

- httpsから始まるURL
- Authorizationの値
- Content-Lengthの数字

をメモっておきます。後でDatadogを開いた時にコピペでもいいかもしれません。
CloudAutomatorのAPI登録はRoute53のFullアクセス権限のみアタッチしたIAMユーザーで大丈夫です。

## DatadogでWebhook機能としてCloudAutomatorを登録する

![Webhookインテグレーション]({filename}/images/20171204-02.png)

まずDatadogでWebhook機能をONにします。
[Datadog-Webhooks Integration](https://docs.datadoghq.com/integrations/webhooks/)

WebhooksのConfigurationから設定をします。
![Webhookインテグレーション]({filename}/images/20171204-03.png)

その際に先ほどメモをしたCloudAutomatorのジョブの情報を入れます。
![Webhookインテグレーション]({filename}/images/20171204-04.png)

```json
{"Authorization" : "CAAuth xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,
"Content-Length": 0}
```

設定を保存します。
その後[モニター作成](https://app.datadoghq.com/monitors#/create)を選び、障害時の挙動についての設定を行います。

今回はcode.popowa.comにDatadogエージェントを入れて監視しているのですが、2分間データが来なかった場合に自動でURLを切り替える挙動を想定したラーとにします。
ちょうどNotify your teamの箇所でWebhookで作った設定が名前ごとに表示されるので、対象ものを選択し
入れ込みます。

![Webhookインテグレーション]({filename}/images/20171204-05.png)


注意事項としてはCloud AutomatorのRoute53の値変更は同じタイプ(AもしくはCNAME)でしか変更出来ないという事です。
元々Aレコード値を、Failover時にCNAMEに変えることは出来ない ><

## 検証する

検証用のURL: [http://dev.code.popowa.com](http://dev.code.popowa.com)

![正常時]({filename}/images/20171204-06.png)

Datadogエージェントを止めます。[Start/Stop/Restart the Datadog Agent – Datadog](https://help.datadoghq.com/hc/en-us/articles/203764515-Start-Stop-Restart-the-Datadog-Agent)

```sh
aya@codepopowa:~$ sudo /etc/init.d/datadog-agent stop
[ ok ] Stopping Datadog Agent (stopping supervisord): datadog-agent.
```

2分後にWebhookが動くはずなので待ちます。
....
アラートが来た！

![アラート]({filename}/images/20171204-07.png)

切り替わりました！
![Failover時]({filename}/images/20171204-08.png)

Cloud Automatorのイベントログにも追加されていました。

![Failover時]({filename}/images/20171204-09.png)

やったね！今回はCloud Automator + Datadogでの自動切り替えでしたが、Datadogは色々な連携が出来るので、Cloud Automatorでフェイルオーバーしていると時にPageDutyなどで通知などもいいかもしれません。

[Cloud Automator と PagerDuty を組み合わせた便利な使い方 – サーバーワークスエンジニアブログ](http://blog.serverworks.co.jp/tech/2015/10/29/pagerduty-cloudautomator-2/)

## まとめ

Cloud Automator を使って簡単にフェールオーバー設定が出来ました。
もちろん環境に問題がないのが一番ですが、やはり障害時の備えは安く、お手軽にしておきたいですよね〜。
ぜひCloud Automatorを活用して運用の軽減ご検討ください👍
