Title: Ruby で URL を デコードする
Date: 2013-01-28 04:25
Authors: ayakomuro
Tags:  Uncategorized
Slug:2013/01/ruby-url
Status: published

調べたら簡単だった。


    require 'uri'
    url = 'http%3A%2F%2Fblog.popowa.com'
    decodedUrl = URI.decode(url)
    print decodedUrl
