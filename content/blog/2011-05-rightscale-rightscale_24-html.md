Title: RightScaleが出来ることは？
Date: 2011-05-23 16:26
Authors: ayakomuro
Tags:  RightScale
Slug:2011/05/rightscale-rightscale_24
Status: published

〜RightScaleで何が出来るか〜+次はRightScaleは「クラウド管理が出来るSaaS型のサービスである」と前回書きましたが、それじゃそのサービスで何が出来るの！？と列挙していきたいと思います。  


もちろん以下列挙している事の多くは個々のクラウドのAPI経由やダッシュボード（マネージメントコンソール等）で行う事が出来ますが、RightScaleを使い自動化設定をする事でより簡単に、インフラエンジニア大量雇用しなくても、また既存資源を使いつつ、よりスケールアウトや自動化などクラウドの利点を活用する事が出来ます。  

 
出来る事（順不同）
------------------



1.  マルチクラウドを[一元的に管理]出来る  

    1.  ここで言うマルチクラウド、というのは、世の中に出ているクラウド（パブリック、プライベート）を一元的に同じように管理出来る（対応クラウドに関しては以下を参照）
    2.  IaaSだけではなく、PaaSと呼ばれるようなクラウドも扱う事が出来る
    3.  一つのクラウドにベンダーロックされない



2.  ハイブリット構成が構築出来る  

    1.  データーベースだけはオンプレミスやプライベートクラウドに配置し、レスポンス返すHttpdサーバはパブリッククラウドに置く等



3.  サーバーテンプレートと呼ばれるインフラ（サーバーやアプリ）構成についてのレシピ集が多数あり、選ぶだけでサーバー構築が出来る  

    1.  サーバーテンプレートは自前で作る事が出来る
    2.  面倒ならばRightScaleにサーバーテンプレートを作ってもらう事が出来る
    3.  作ったテンプレートを公開する事が出来る
    4.  公開したテンプレートを課金対象とする事が出来る



4.  個々のサーバー管理ではなく構成を管理する事が出来る  

    1.  サーバーが落ちれば自動で他のサーバーで立て直す事も可能
    2.  構成はバージョン管理されており、バージョンを戻したり、一部のスクリプトだけ上げたりという事が出来る



5.  サーバー構築だけではなく保守もする事が出来る  

    1.  例えばパッケージ（PHPやRuby等）のアップデートを行ったり、設定ファイルを書き換えたり、アプリを展開して再配置したりする事が出来る
    2.  構築した構成を簡単に変える事が出来る



6.  監視機能を簡単につける事が出来る  

    1.  取得値によって、自動でサーバーを増やしたり減らしたりする事が出来る
    2.  自動でサーバーを大きくしたり小さくしたりする事が出来る



7.  RightScaleを自前クラウドに載せて再販出来るリセラープログラムがある
8.  特定の業界や、要望に合わせたソリューションパックを選ぶ事が出来る  

    1.  開発とテストソリューションパック
    2.  グリッドソリューションパック
    3.  Zend PHP ハイアベーラビリティ(HA)ソリューションパック
    4.  ソーシャルゲームソリューションパック






RightScaleが対応しているクラウド一覧
------------------------------------



-   public  

    -   [Amazon EC2](http://aws.amazon.com/ec2/)
    -   [GoGrid](http://www.gogrid.com/)
    -   [FlexiScale](http://www.flexiant.com/products/flexiscale/)
    -   [RackSpace](http://www.rackspace.com/cloud/)



* private  
    * [Eucalyptus](http://www.eucalyptus.com/)
    * [Cloud.com](http://cloud.com/)
    * [OpenStack](http://www.openstack.org/)
![VMware  vCloud](http://www.rightscale.com/news_events/press_releases/2009/RightScale-Adds-VMware-vCloud-Express-to-Arsenal-of-Supported-Clouds.php)

*   PaaS  
      * [Azure](http://d.hatena.ne.jp/keyword/Azure)([Blog](http://www.rightscale.com/news_events/press_releases/2009/RightScale-Announces-Planned-Support-for-Windows-Azure-Platform.php))
      * [Cloud Foundry](http://blog.rightscale.com/2011/04/12/launch-vmwares-cloudfoundry-paas-using-rightscale/)

※もしかしたら他にもあるかもしれません。抜けがありましたらお知らせください。  
