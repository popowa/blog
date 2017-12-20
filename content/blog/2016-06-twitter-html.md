Title: Twitter企画の簡単キャラシ一覧作成方法
Date: 2016-06-15 04:13
Authors: ayakomuro
Tags:  Twitter企画
Slug:2016/06/twitter
Status: published

Cookpadの[とるだけ](https://cookpad-diet.jp/apps/)というアプリに毎日食事を急かされているコムロです。

私は趣味で絵を描くのですが、カテゴリーとしては[企画](http://dic.pixiv.net/a/%E4%BC%81%E7%94%BB)というのが好きでよく参加してます。  
基本はPixivメインなのですが最近[Twitter企画](http://dic.pixiv.net/a/Twitter%E4%BC%81%E7%94%BB)となるものが多く出てまして、お手軽に参加出来る・簡単に交流出来るという所から最近企画界隈ではブームだと感じです。  
今回の記事はTwitter企画で投稿されたキャラシを簡単に尚且つ自動で一覧にしてくれる仕組みについて説明します。

前提

-   企画主催者の公式Twitterアカウントがある
-   キャラクターシート用のハッシュタグがある

1\) まず参加者は \#企画名キャラシ　や \#企画名CS
と言ったハッシュタグを付けて作ったキャラクターシートを投稿します。

[![](https://4.bp.blogspot.com/-91cLf1gaMnw/V2Cqc70uSDI/AAAAAAAAeus/4PRofXdf4nU52ja5icLYs7JpVbCsl3MhACLcB/s400/1%2B%25281%2529.png){width="400"
height="282"}](https://4.bp.blogspot.com/-91cLf1gaMnw/V2Cqc70uSDI/AAAAAAAAeus/4PRofXdf4nU52ja5icLYs7JpVbCsl3MhACLcB/s1600/1%2B%25281%2529.png)


2\) 企画主催者の公式Twitterアカウントがそれをリツイートします。

[![](https://4.bp.blogspot.com/-KDAmUkpGtSw/V2Cq6C5roRI/AAAAAAAAeu0/X7-oADGAytQ8XoUKZgCj7DYshdzUL8ASQCLcB/s400/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%2589%258D10.09.23.png){width="400"
height="92"}](https://4.bp.blogspot.com/-KDAmUkpGtSw/V2Cq6C5roRI/AAAAAAAAeu0/X7-oADGAytQ8XoUKZgCj7DYshdzUL8ASQCLcB/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%2589%258D10.09.23.png)

これだけでTumblrのキャラシ一覧に**[[自動で]](←大事）**追加されます。


仕組みはとても簡単です。

利用するサービスはIFFFとTumblrとTwitterです。


-   I[FTTT](https://ifttt.com/recipes)（イフト）は、Aが指定の条件を満たせば、Bを実行する、というサービスです。
-   [Tumblr](https://www.tumblr.com/)（タブンラー）は、ブログのようなものです。
-   Twitterは言わずもがな。

流れはこんな感じです。

[![](https://3.bp.blogspot.com/-odQi3-zELTI/V2DSoecLYyI/AAAAAAAAevw/YDDqyYxBnI03ZO-8EnPp4gFx4rfAbvUsQCLcB/s640/2.png){width="640"
height="467"}](https://3.bp.blogspot.com/-odQi3-zELTI/V2DSoecLYyI/AAAAAAAAevw/YDDqyYxBnI03ZO-8EnPp4gFx4rfAbvUsQCLcB/s1600/2.png)


それを叶えるIFTTTの設定はこのような感じです。

[![](https://4.bp.blogspot.com/-oXXTcI3grx8/V2DGcIuFxII/AAAAAAAAevI/kxiu8un77dQwoSbwLZo2hgDWorS9_2U_QCLcB/s640/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%2589%258D11.58.55.png){width="640"
height="220"}](https://4.bp.blogspot.com/-oXXTcI3grx8/V2DGcIuFxII/AAAAAAAAevI/kxiu8un77dQwoSbwLZo2hgDWorS9_2U_QCLcB/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%2589%258D11.58.55.png)

トリガーは企画主催者ツイッターが、指定のハッシュタグをツイートしたら(RTも含まれます）

[![](https://2.bp.blogspot.com/-MBpkMZda4-8/V2DNleWiMfI/AAAAAAAAevY/kGjqMR5o0Bsxk62bL0y5heuC2lO8-T-GwCLcB/s320/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%25BE%258C0.37.15.png){width="320"
height="152"}](https://2.bp.blogspot.com/-MBpkMZda4-8/V2DNleWiMfI/AAAAAAAAevY/kGjqMR5o0Bsxk62bL0y5heuC2lO8-T-GwCLcB/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%25BE%258C0.37.15.png)


Tumblrに自動投稿をする、という設定だけでいいです。

この時に設定するのは**[Quote（引用]**）経由で**[TweetEmbedCode]**として投稿する事が大事です。そうではないとキャラシが1枚以上の時に綺麗に表示が出来ません。

[![](https://4.bp.blogspot.com/-uOK4crDb7hE/V2DN2qMGM8I/AAAAAAAAevg/aTCZrzWmYAwUyrznIFJvVTzfRs3kwuhtgCLcB/s320/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%25BE%258C0.37.09.png){width="264"
height="320"}](https://4.bp.blogspot.com/-uOK4crDb7hE/V2DN2qMGM8I/AAAAAAAAevg/aTCZrzWmYAwUyrznIFJvVTzfRs3kwuhtgCLcB/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%25BE%258C0.37.09.png)

これだけです。これだけで、後は企画公式ツイッターがキャラシタグが付いたツイートをRTするだけで自動でTumblrに投稿が出来ます。


注意点/考慮すべき点としては


-   RTしないもの、また指定のタグが違うツイートは、投稿されない
-   ツイート自体が削除されてしまったには、画像は消えるが投稿自体は自動で削除される機能がないのでリクエストか適時チェックをして対応する必要がある
-   RT漏れは直接企画公式ツイッターに対してメンションしてもらう

自由度/拡張性については


-   Tumblrで固定ページ（例えば世界観に関するページや、企画内企画についてもページ）を管理者が作成する事が可能
-   管理者を複数設定する事が可能（副主催者さんがいる場合など）
-   問い合わせフォームなども設置可能
-   メール投稿なども可能


これでTwitter企画のキャラシを探しやすくなるといいですね〜！

ちなみに見た目はこんな感じになります。テーマ（デザイン）は[Tumblrのテーマ一覧](https://www.tumblr.com/themes)から選べばなんでも！

[![](https://4.bp.blogspot.com/-bCt1pNaIG4w/V2DVqvhjM8I/AAAAAAAAev8/0ls5P8dFDcE0gYvAESA1HNpm6AAejL0MwCLcB/s400/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%25BE%258C1.08.33.png){width="400"
height="252"}](https://4.bp.blogspot.com/-bCt1pNaIG4w/V2DVqvhjM8I/AAAAAAAAev8/0ls5P8dFDcE0gYvAESA1HNpm6AAejL0MwCLcB/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2016-06-15%2B%25E5%258D%2588%25E5%25BE%258C1.08.33.png)


追記


-   上記以外の仕組み（例えばTwitterのハッシュタグを検索してTumblrに投稿する）ですと、他の方によるキャラシRTでTumblrに重複投稿が行われるのであまり綺麗な形で投稿は出来ません (-ω-；)
