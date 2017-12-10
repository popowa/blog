Title: IAMでインスタンスを生成させない設定
Date: 2013-11-04 07:37
Authors: ayakomuro
Tags:  IAM
Slug:2013/11/iam
Status: published

ローカルを掃除していたら出て来たドキュメント。








誰かに役に立つかもしれないのでアップする











**[[IAM]{lang="EN-US"
style="font-family: メイリオ; mso-hansi-font-family: メイリオ;"}][[でインスタンスを生成させない設定[]]]**





[Amazon]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}[マネージメントコンソールにログインし、[IAM]にアクセスします。[]]





[そして該当ユーザーを選択し、[Permission]を追加します。[]]





[ポップアップの二番目の箇所に[Policy
Generator]というラジオボタンがあるので、選択し、[Select]を押します。[]]



[![](http://3.bp.blogspot.com/-MzyaEFOOUfc/UndOfSzzEWI/AAAAAAAAYz0/SaH0Z46RE80/s640/1.png){width="640"
height="86"}](http://3.bp.blogspot.com/-MzyaEFOOUfc/UndOfSzzEWI/AAAAAAAAYz0/SaH0Z46RE80/s1600/1.png)



[  
]





[]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ; mso-no-proof: yes;"}[]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}





[Manage User Permission]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}[にて、[Deny]を選択し、対象サービス（[EC2]）選択ご、対象アクション（[RunInstance:]インスタンスを起動させる）にチェックを入れます。[]]



[![](http://4.bp.blogspot.com/-UYo3sHog-8I/UndOkkJCpvI/AAAAAAAAY0E/6BHmoFXM_Xk/s640/2.png){width="640"
height="349"}](http://4.bp.blogspot.com/-UYo3sHog-8I/UndOkkJCpvI/AAAAAAAAY0E/6BHmoFXM_Xk/s1600/2.png)



[  
]





[  
]





[]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ; mso-no-proof: yes;"}[]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}





[必要があれば、リソース指定をして、特定インスタンスだけのアクションを禁止する、という事も可能です。[]]





[]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ; mso-no-proof: yes;"}[]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}



[![](http://1.bp.blogspot.com/-fInqHAeG5xU/UndOokO4kAI/AAAAAAAAY0M/BIcoHXFPj3Y/s1600/3.png)](http://1.bp.blogspot.com/-fInqHAeG5xU/UndOokO4kAI/AAAAAAAAY0M/BIcoHXFPj3Y/s1600/3.png)







[参考[URL]]





[Policy generator ]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}[[[http://awspolicygen.s3.amazonaws.com/policygen.html]](http://awspolicygen.s3.amazonaws.com/policygen.html)][]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}





[TecTec Cloud: IAM]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}[で[AWS]アカウントのユーザー管理を行なう[1]]





[<http://ttcloud.net/aws/iam/20110310/978>]{lang="EN-US"
style="font-family: メイリオ; font-size: 10.0pt; mso-hansi-font-family: メイリオ;"}








