Title: AWS CloudTrailを解析出来るログアプリ
Date: 2014-10-17 02:10
Authors: ayakomuro
Tags:  cloudtrail
Slug:2014/10/aws-cloudtrail
Status: published

AWS CloudTrail

はそのままで見づらいので、すでにパートナーとして提供されているアプリを試してみます。

参考URL

<http://aws.amazon.com/jp/cloudtrail/>

-   [【AWS発表】 AWS CloudTrail - AWS
    APIコールの記録を保存 ](http://aws.typepad.com/aws_japan/2013/11/aws-cloudtrail-capture-aws-api-activity.html)
-   [【AWS発表】CloudTrailが再び拡大 -
    リージョンとサービスの拡張、素晴らしいビジネスパートナー ](http://aws.typepad.com/aws_japan/2014/07/cloudtrail-expands-again.html)

[CloudTrail
でログとれ〜る](http://www.slideshare.net/kani_b/cloudtrail) 

[AWSの操作履歴を記録するCloudTrailを試してみた « サーバーワークス
エンジニアブログ](http://blog.serverworks.co.jp/tech/2013/11/14/cloudtrail/) 

[【驚愕】CloudTrailログ解析にlogglyを使ってみた結果ｗｗｗ【使わないと損！】
« サーバーワークス
エンジニアブログ ](http://blog.serverworks.co.jp/tech/2014/10/10/loggly/)

[AWS 白帯シリーズ(5) CloudTrail のログを可視化する試み（1） by @inokara
on @Qiita](http://qiita.com/inokappa/items/660303d87af6d2e2dbd4) 

[【Excel改造】AWSへのアクセスログをExcelで表示してみた【CloudTrail編】｜クラスメソッドブログ](http://dev.classmethod.jp/cloud/excel_aws_cloudtrail/) 



今回試したのは

-   CloudCheckr
-   Stackdriver
-   Sumologic
-   Alert Logic



で大半は有料プランじゃないと見れないのが多かったので選んで再度検証を続けたい所。







その他のサービスはまた何か別の機会に試したい。









\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--







[**CloudCheckr**]



<http://cloudcheckr.com/>

提供パターン

金額

-   CloudTrailが使えるのはCloudCheckr Proから。 \$75/mon
-   CloudCheckr Proが14日間お試しで使える
-   <http://cloudcheckr.com/pricing-features/>
-   <http://cloudcheckr.com/wp-content/uploads/2014/04/CloudCheckr-Breakdown.pdf>

ドキュメント: <http://support.cloudcheckr.com/configure-aws-cloudtrail-to-log-trails-in-a-single-s3-bucket/>

-   [【AWS発表】AWS CloudTrail アップデート - 7つの新サービス
    &　CloudCheckr ](http://aws.typepad.com/aws_japan/2014/05/aws-cloudtrail-update-new-services-support-from-cloudcheckr.html)
-   





使える様になるまでのフロー





-   CloudCheckrにアカウントを作る
-   S3のGetObject権限があるIAMを作る -\>
    [設定方法](http://support.cloudcheckr.com/enabling-cloudtrail-reports/)
-   CloudCheckr内にアカウントを作り上記IAMを設定する
-   左側メニューのSecurity \> CloudTrailの所から見る。

[![](http://4.bp.blogspot.com/-30Oi1lywYGA/VEBxpIJcreI/AAAAAAAAcew/OYGGup50PjI/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%2B2014-10-17%2B10.31.36.png){width="169"
height="400"}](http://4.bp.blogspot.com/-30Oi1lywYGA/VEBxpIJcreI/AAAAAAAAcew/OYGGup50PjI/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%2B2014-10-17%2B10.31.36.png)









データの収集は定時か強制に行う事が可能



[![](http://1.bp.blogspot.com/-wRIHXN2_utw/VEByIdVsewI/AAAAAAAAce4/aTvzpW8q-dk/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%2B2014-10-17%2B10.33.46.png)](http://1.bp.blogspot.com/-wRIHXN2_utw/VEByIdVsewI/AAAAAAAAce4/aTvzpW8q-dk/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%2B2014-10-17%2B10.33.46.png)











感想

-   設定自体は簡単だった
-   CloudCheckrがTrusted Advisorとほとんど同じ機能であった
-   CloudTrail用じゃなくてもCloudCheckr便利だった

[![](http://3.bp.blogspot.com/-Vp7oZgX4ydw/VEB2L8ROHsI/AAAAAAAAcfQ/Bra2FzeeSA4/s1600/cloudcheckr_cloudtrail_most_active_ip_addresses_1.png){width="640"
height="310"}](http://3.bp.blogspot.com/-Vp7oZgX4ydw/VEB2L8ROHsI/AAAAAAAAcfQ/Bra2FzeeSA4/s1600/cloudcheckr_cloudtrail_most_active_ip_addresses_1.png)

[[【AWS発表】AWS CloudTrail アップデート - 7つの新サービス
&　CloudCheckr ]](http://aws.typepad.com/aws_japan/2014/05/aws-cloudtrail-update-new-services-support-from-cloudcheckr.html)

[**この機能いいね！ - Alert Builder**]  
CloudCheckrの機能にAlert
Builderというのがあって以下の内容をアラートとして送ってくれる

1.  AWS Costs
2.  CloudTrail(beta)
3.  EC2 Number of Instances
4.  EC2 Resources Utilization
5.  S3 Storage Used (less than/greater than)
6.  S3 Total Objects



AWSの機能を使えば5と6以外は出来るけど、5と6は自分で組む以外は出来なかった気がする。SNSやPagerDutyと連携も出来るので便利〜







[![](http://2.bp.blogspot.com/-NroV2DNcM8A/VEBzwVjorII/AAAAAAAAcfE/dVI_v9OUUjI/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%2B2014-10-17%2B10.41.10.png){width="640"
height="134"}](http://2.bp.blogspot.com/-NroV2DNcM8A/VEBzwVjorII/AAAAAAAAcfE/dVI_v9OUUjI/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%2B2014-10-17%2B10.41.10.png)





\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

[**Stackdriver**]



<http://www.stackdriver.com/>

<https://app.stackdriver.com/>

提供パターン: SaaS

金額: 無料もあるがEliteコースじゃないとCloudTrail使えない　

-   Elite: \$12/mo/per server or hosted AWS service
-   <http://www.stackdriver.com/pricing/>

ドキュメント: <http://support.stackdriver.com/customer/portal/articles/1491719-integrating-with-cloudtrail>



使える様になるまでのフロー





StackDriverのアカウント作成

IAM roleを作成
-\>[設定方法](https://app.stackdriver.com/settings/add_cloud_account/aws)

-   上記の画面で一緒にIAM
    RoleのARNを入力する箇所がありStackDriverと連携をする

instanceの監視もしたいのであればagentインストールを行う

CloudTrailをOnにする

SNSでトピックを作る

SQSのキューを作り、上記のSNSのトピックをSubcribeする





感想





-   有料だったので結局試せなかったのでなし
-   でも設定は簡単だった。
-   Googleアカウントでログイン出来るし、別のクラウドも一緒に管理出来るのはいいね
-   UIもネルフみたいで中二病を感じさせる



TODO



-   後でEliteコースにしてみる



\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--









[**Sumologic**]



-   <http://www.sumologic.com/applications/aws-cloudtrail/>
-   提供パターン: SaaS(Sumo Logic Professional or Sumo Logic Enterprise
    customeじゃないと使えない）
-   金額: Sumo Logic Professional
    (min\$90/mon\~max\$1800/mon:利用するデータ量による)
-   出来る事
-   ドキュメント:
    <https://service.sumologic.com/help/Default.htm#CloudTrail_App.htm>





使える様になるまでのフロー





Sumologicのアカウントを作る

CloudTrailをOnにする

S3の読み込み専用のIAMを作る（Access KeyとSecret Keyが必要）

Hosted Collectorを作る -\>
[設定方法](https://service.sumologic.com/help/Default.htm#Setting_up_a_Hosted_Collector.htm)

-   自分の環境にCollectorを作る事も可能（Installed Collector)

LibraryからCloudTrailのappを入れる -\>
[設定方法](https://service.sumologic.com/help/Default.htm#Installing__the_AWS_Cloud_Trail_App.htm)







[![](http://4.bp.blogspot.com/-drxxMa74t1s/VEA2xkXb8lI/AAAAAAAAceg/6cWlImW3yG4/s1600/CloudTrail_Network_690x374.png)](http://4.bp.blogspot.com/-drxxMa74t1s/VEA2xkXb8lI/AAAAAAAAceg/6cWlImW3yG4/s1600/CloudTrail_Network_690x374.png)







感想





-   有料だったので結局試せなかったのでなし
-   設定は簡単
-   Sumologic自体は操作が簡単に出来るのでCloudTrailもいい感じのはず。。。





\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--









[**Alert Logic**]





-   <http://www.alertlogic.com/products-services/public-cloud-security/cloud-security-for-aws/>
-   <https://aws.amazon.com/marketplace/pp/B00LAJJ2MW>
-   提供パターン：Marketplace経由でのAMI利用課金（選択するスペックによって金額が変わる）Alert
    Log Managerと呼ばれる
-   金額：\$0.15/hr\~\$0.72/hr
-   出来る事
-   ドキュメント: <http://docs.alertlogic.com/#docs/install_and_configure/alert_logic_log_manager/how_to_install_lm_for_log_collection.htm>



使える様になるまでのフロー

上記のMarketplaceからAlert Logic Managerを起動

Alert
Logicにアカウントを作る（起動したインスタンスのFQDNにアクセスすればその旨表示されるのでそこからアカウント作ると良い）

CloudTrailをOnにする-\> [リンク](http://cloud.docs.alertlogic.com/#cloud_partner/aws/lm/cloudtrail/enable_cloudtrail.htm)

SNSでトピックを作る

SQSのキューを作り、上記のSNSのトピックをSubcribeする

IAM Roleを作る(Alert LogicのAWSアカウントがアクセスする為にcross-account
accessがしたいらしい）割と設定が面倒なので[こちらを参考](http://cloud.docs.alertlogic.com/#cloud_partner/aws/lm/cloudtrail/create_an_iam_role.htm)に作る

1.  Alert LogicのAWSアカウント: 239734009475

CloudTrail Logソースを作る
-\>[リンク](http://cloud.docs.alertlogic.com/#docs/log_manager/work_with_collection__alert_rules__and_policies/log_sources/collect_aws_cloudtrail_logs.htm) ←**[今ここで挫折中]**











感想





-   [https://invision.alertlogic.net](https://invision.alertlogic.net/)
    が遅延が凄いあるのでちょっと辛い。。
-   ドキュメント通りクリックしても別の画面に遷移する(涙
-   <https://invision.alertlogic.net/logs.php>　はダミーページなので無視する



TODO











-   サポートに問い合わせる\....



\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

まとめ

-   CloudTrailは大体有料プラン側に入っている
-   如何に簡単に設定出来るか、というのは大事
-   他のインスタンスの監視やコストの監視などまとめてみれると確かに嬉しい
-   遅延があるのは結構辛いなと思った




