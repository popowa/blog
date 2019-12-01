Title: DatadogでWorkSpacesを監視する
Date: 2017-03-15 09:02
Authors: ayakomuro
Tags:  AWS, Datadog, workspaces
Slug:2017/03/datadogworkspaces
Status: published

前DatadogがWorkSpaces（Win10）に入らない！とブログ書いたのですが、Windows

7には入りました。

![画像](https://4.bp.blogspot.com/-NZyPadh184g/WMkPuPXPO6I/AAAAAAAAfqQ/W32gSwu-n_8UNTn2bMqf8sCPaZZf9vw1gCLcB/s320/datadog_logo_share_tt.png)
こんな感じ。

![画像](https://2.bp.blogspot.com/-EA8Ul2nHnXg/WMkCX2--dCI/AAAAAAAAfp4/5umPGDw8p4wOZ0oyvYoD_RmnFfyVavlOQCLcB/s640/list.jpg)

![画像](https://1.bp.blogspot.com/-uo9E0jQfcdI/WMkCTg_mqDI/AAAAAAAAfp0/TUKWkwsMhtwCiO-_96iux_Mf5o4FJz2QwCLcB/s640/hostinfo.jpg)

![画像](https://3.bp.blogspot.com/-sQn4gmBASQA/WMkCMdf-vhI/AAAAAAAAfpw/99QVoXeNVfAZezUgZf3G3xJEvn75y3b0QCLcB/s640/dashboard.jpg)

WorkSpaces内

![画像](https://1.bp.blogspot.com/-JXti9bRFWMg/WMkCe0jhfxI/AAAAAAAAfp8/U3dgWeXMWt8NoxIiInhEjKbGBmoML0S_QCLcB/s1600/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2017-03-15%2B13.20.37.png)



言いたかったのはそれだけ。Datadogはエージェントが動くと課金されるので、CloudWatch側でのWorkSpacesの値を取ってきてDashboard作るのいいかもしれないですね。ダッシュボード一覧にはWorkSpaces用のダッシュボードがないので、自分作る必要がありますが、値が少ないので簡単に作れるかと。

-   [Amazon WorkSpaces メトリクスのモニタリング - Amazon
    WorkSpaces](http://docs.aws.amazon.com/ja_jp/workspaces/latest/adminguide/monitoring.html) 


WorkSpacesでGoogle Hangoutで会議している時の状態



![画像](https://2.bp.blogspot.com/-tlPSknffuOE/WMoAi-G9nfI/AAAAAAAAfqg/v4SEgIyXS2E0mzQ6s6Qq5Flforx5dAn4ACLcB/s640/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588%2B2017-03-16%2B12.02.50.png)
