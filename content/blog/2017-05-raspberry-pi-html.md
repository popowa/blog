Title: Raspberry Piの初回設定
Date: 2017-05-07 06:53
Authors: ayakomuro
Tags:  RaspberryPi
Category: tech
Slug:2017/05/raspberry-pi
Status: published

Raspberry Piを買ったので、初回設定をした時もメモ  
インターネットにドキュメントが沢山転がっているので、簡単に出来る( ˇωˇ )b

![RaspberryPi]({filename}/images/RaspberryPi.png)

# Raspberry
Piの箱に入っていたマニュアルに設定方法が記載してあるのでまずそれを読みます。
* <https://www.raspberrypi.org/files/legacy/qsg.pdf>

上記のフローをやれば簡単に出来るかと思います。legacyってあるから、もしかしたら今はもっと違う方法があるのかも？

準備するものは上記に記載がある通り。後はあちらこちらに記事があるから、そこを見れば良いかと

SDカードをフォーマットするアプリをダウンロード

*   <https://www.sdcard.org/downloads/formatter_4/>

SDカードにRaspberry Pi OSを入れる。私はNOOBSにしてみた。

*   <https://www.raspberrypi.org/downloads/>

その後、リモートでも入れるようにsshdを有効にします。

*   <https://www.raspberrypi.org/documentation/remote-access/ssh/README.md>

wifiを設定してapt-get
updateやrpi-updateなどを実施しレポジトリやファームウェアをアップデートした後に、ローカルIPアドレスを固定させます。ここら辺はDebianやLinuxを使っていると一般的かと思われます。

# WLAN0設定

* [How to setup a static IP address on your Raspberry Pi](https://thepihut.com/blogs/raspberry-pi-tutorials/16683276-how-to-setup-a-static-ip-address-on-your-raspberry-pi)
*  [Raspberry PI: How to Add Static/Manual IP to Wireless wlan0 and eth0](http://www.electroschematics.com/9496/static-manual-ip-wireless-raspberry-pi/)

音が出るか確認します。スピーカーを差し込んで試してみます。

-   [PLAYING AUDIO ON THE RASPBERRY PI](https://www.raspberrypi.org/documentation/usage/audio/README.md)

VNCも試してみたのですが、カクカクだったのと、sshしてvim使えたらとりあえずいいので、オフにしました。

-   [設定はこちら](https://www.raspberrypi.org/documentation/remote-access/vnc/README.md)
-   [RealVNCだと便利](https://www.realvnc.com/download/viewer/macosx/)

Raspberry Piの準備はとても簡単です。よく大変だーとかありますが、いつの時代もマニュアルを読んでそれに沿って進めれば半分ぐらい上手く行くので、素直にやるのがよいかと思いました。
