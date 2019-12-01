Title: wkhtmltopdfで無限ループでPDFを作り出してしまうバグ
Date: 2017-12-18 09:40
Category: tech
Tags: python
Slug: 2017/12/wkhtmltopdf-CG_CONTEXT_SHOW_BACKTRACE
Authors: ayakomuro
Summary: pythonでpdfkit経由でwkhtmltopdfを使っていた時に出たエラーについて

やりたい事はただ一つ、HTMLファイルをPDFにしたいだけだ。

# set CG_CONTEXT_SHOW_BACKTRACE environmental variable

何かしらの方法で取得したHTMLがあるとする


```
#!python
import pdfkit
pdfkit.from_file('201708.htm', '201708.pdf')
```

上記を実行すると

`Dec 18 08:05:15  wkhtmltopdf[45102] <Error>: CGContextSetFillColor: invalid context 0x0.
If you want to see the backtrace, please set CG_CONTEXT_SHOW_BACKTRACE environmental variable.`


が大量に出力されて出力されたPDFファイルが1000ページぐらいになる
調べたらまだバグとしては直っていない模様。

[Infinite loop of errors · Issue #2196 · wkhtmltopdf/wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf/issues/2196)


まずは他のツールがないかと探して見た

# xhtml2pdf <= 不採用

- [xhtml2pdf/xhtml2pdf: A library for converting HTML into PDFs using ReportLab](https://github.com/xhtml2pdf/xhtml2pdf)
- [Welcome to xhtml2pdf’s documentation! — xhtml2pdf 0.1b3 documentation](http://xhtml2pdf.readthedocs.io/en/latest/index.html)

このツールはissues見ている限りバギーだし、実際に動かしてみてもバギーだった。まともに動かない

# WeasyPrint <= 採用

- [Kozea/WeasyPrint: WeasyPrint converts web documents (HTML with CSS, SVG, …) to PDF.](https://github.com/Kozea/WeasyPrint)
- [WeasyPrint — WeasyPrint 0.41 documentation](http://weasyprint.readthedocs.io/en/latest/index.html)

```
#!sh
pip install weasyprint
brew install cairo pango gdk-pixbuf libffi
```

素直にいい感じに動いてくれた。

# 結論

pdfkit, wkhtmltopdfを捨ててweasyprint使おう
