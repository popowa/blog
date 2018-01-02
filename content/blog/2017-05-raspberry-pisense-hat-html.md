Title: Raspberry PiでSense Hatを始める時のドキュメント一覧
Date: 2017-05-07 07:00
Authors: ayakomuro
Tags:  RaspberryPi, SenseHat
Slug:2017/05/raspberry-pisense-hat
Status: published

Sense HATで出来る事
-------------------

[✔︎]Gyroscope、ジャイロスコープ

-   ボードがどちら上を向いているか
-   角速度計

Accelerometer 

-   加速度計

Magnetometer

-   磁力計

[✔︎]Temperature

-   温度

[✔︎]Barometric pressure

-   気圧

[✔︎]Humidity

-   湿度


![HAT]({filename}/images/image-1444117187018.jpg)

Raspberry PiにSense hatを取り付けると、元々Raspiに付いていたケースに綺麗にフィットしなくなる。作った方がいいのかもしれない....👀

### 参考リンク
-   製品ページ <https://www.raspberrypi.org/products/sense-hat/>
-   Raspberry Pi上でのSense Hatの扱い　<https://www.raspberrypi.org/documentation/hardware/sense-hat/> 

### コード関連
SenseHat

-   <https://pythonhosted.org/sense-hat/>
-   APIに関してはここを見る　<https://pythonhosted.org/sense-hat/api/>

とりあえずPythonコードでSenseHatを試したい時は以下のリンクに簡単なチュートリアルがあるので試すとわかりやすくていいかも。後は上記のsense-hat/apiで関数を試せばよいと思う

-  [Getting started with the Sense HAT](https://www.raspberrypi.org/learning/getting-started-with-the-sense-hat/worksheet/)

とりあえず部屋に置いているRaspiから部屋の温度、湿度、気圧をTwitterに定期的にツイートさせるようにしたけども、だからといって何か意味がある形にした訳じゃないから、次は他の事と組み合わせてみたい。

-   -   <https://github.com/bear/python-twitter>
-   Twitterの認証情報はこちらで生成　<https://apps.twitter.com/>
-   Twitter認証 --> センサーデータ取得 --> ツイート
