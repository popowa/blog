Title: UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 3131: invalid start byte
Date: 2017-12-30 10:25
Authors: ayakomuro
Tags:  python
Category: tech
Slug:2017/12/UnicodeDecodeError
Status: published

時々ディレクトリ配下にあるファイル一覧を取得して、ファイルの中身をごにょごにょする時があると思う。そういう時表題のエラー出たら、大体の場合 `.DS_Store` を読み込もうとしているからなので、それをスキップすればよい
