Title: 
Date: 2013-01-14 07:06
Authors: ayakomuro
Tags:  Google
Slug:2013/01/google-chart-toolssheadsheet
Status: published


ToolsでSheadsheetを使ったグラフ描写+[統計局のデータ](http://www.stat.go.jp/data/index.htm)を色々見ていたら、グラフにしてみようと思い、Google
Chart ToolsでSheadsheetを使ったグラフ描写をしてみました。

統計局がJSONとかでデータを返してくれるAPIとか公開していたら面白いですよね（もしかしたらあるのかも？？）。

[]ハマりどころとしては、

-   sendMethodは無効にする
-   Queryの[URL](http://d.hatena.ne.jp/keyword/URL)はhttpsに =\>
    <https://spreadsheets.google.com/tq?key=>ファイルID&[gid](http://d.hatena.ne.jp/keyword/gid)=0
-   GeoChartは、最初のロードするパッケージに追加する
    =\> google.load(\"visualization\", \"1\", {packages:\[\"corechart\",
    \"geochart\"\]});



テストがてら作ってみた

-   <http://www.popowa.com/data/bar-chart.html>

後ほど閲覧出来るデータをセレクトボックスとかで選択して動的に表示させたい

ついでに

-   <http://d.hatena.ne.jp/popowa/20130114#1358142241>


