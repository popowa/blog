Title: 
Date: 2014-08-15 05:42
Authors: ayakomuro
Tags:  AWS, support
Slug:2014/08/aws-support-api
Status: published


APIでケースを取って来れる期間は一年前まで+今度閉じる社内用AWSアカウントがあったので、サポート内にあるコンテンツを全部バックアップ取っておこうと思ったんですよ。

それで簡単なコード書いたら、  

> /Users/komuro/.rbenv/versions/2.1.1/lib/ruby/gems/2.1.0/gems/aws-sdk-1.50.0/lib/aws/core/client.rb:375:in
> \`return\_or\_raise\': 
> (AWS::Support::Errors::InternalServerError)  
> from
> /Users/komuro/.rbenv/versions/2.1.1/lib/ruby/gems/2.1.0/gems/aws-sdk-1.50.0/lib/aws/core/client.rb:476:in
> \`client\_request\'  
> from (eval):3:in \`describe\_cases\'  
> from get-support-content.rb:11:in \`\<main\>\'

こんなエラーが出て。おや？と思ってパラメーター変えても駄目で、別のAWSアカウントのアクセスキー/シークレットアクセスキーを設定したらちゃんと取れた。  
エラーが出たAWSアカウントの最後の問合せ日時はJul 17, 201304:37 PM
PDTだった。

上記の状況と風の噂で聞いた事を掛け合わせると、

-   AWS Support APIでケース内容を取って来れるのは一年前までである

という事らしい。またAWS Support
APIと、マネージメントコンソールのサポート画面は別のAPIを使っていると思う（マネージメントコンソールでは表示されるのにSupport
APIでは取れない）

マネージメントコンソールで見れるんだからAPIでも取れる様にして欲しいなぁというのがユーザー側の想いですけど何か一年縛りにしている理由があるんですかねー。。  
最後はマネージメントコンソールのサポート画面をあれするしか（うわ、何をするやめr

**追記**：APIのドキュメント調べたら確かに書いてあった！  

> Case data is available for 12 months after creation. If a case was
> created more than 12 months ago, a request for data might cause an
> error.

http://docs.aws.amazon.com/awssupport/latest/APIReference/API\_DescribeCases.html

しょぼーん。
