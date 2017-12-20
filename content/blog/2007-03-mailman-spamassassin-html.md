Title: mailman 
Date: 2007-03-22 01:10
Authors: ayakomuro
Tags:  過去ブログややあやや
Slug:2007/03/mailman-spamassassin
Status: published

 spamassassin
KNOWN\_SPAMMERS = \[(\"x-spam-flag\", \"yes\"),\]  
とすると、静かに破棄される  
後は、  
KNOWN\_SPAMMMERS = \[(\"x-spam-level\", \"\*\*\*\"),\]  
spam level 3以上は破棄

となるらしい(未確認)

今はexim4で受けた時に、spamassassinをつかってフィルターにかけて、その後、個人のMaildirに来た時にprocmailrcで分けているから、有効的かと思われる。

SpamAssassinは日本語対応していない。  
問題点(日本語メール)  
-False Positiveになりやすい  
-日本語キーワードチェックルールを書こうとするとキーワードを文字コード(16進表記)にして書かないと行けない

上記を解決するであろうパッチも作ってくれている方々がいる。  
http://www.emaillab.org/spamassassin/  
効果(未確認)  
-ベイズフィルターが賢くなるらしい(現在は文字コードを変換せず、生のコードのままで処理をするらしい、その一方で、新しいパッチは文字コードをUTF-8に統一した上で、MeCabなどのプログラムで語句に区切るらしい)-\>この処理は時間がかかるらしいが、ベイズフィルターの判別力は大幅にアップ(するらしい)  
-ルールが簡単に書ける。UTF-8を書けるエディターを使えばよい

日本語パッチがあたっているspamassassinをダウンロードする場合はこちらから！  
http://spamassassin.jp/download/rules/

というわけで、オープンソースカンファレン2006東京で貰っSpamAssassin活用ヒント集([日本
SpamAssassinユーザ会](http://spamassassin.jp/))からの抜粋でした。早くwikiをたてたいよー
