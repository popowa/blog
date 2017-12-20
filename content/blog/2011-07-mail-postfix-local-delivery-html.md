Title: ライトスクリプト：MAIL Postfix local delivery
Date: 2011-07-31 05:59
Authors: ayakomuro
Tags:  RightScript
Slug:2011/07/mail-postfix-local-delivery
Status: published




    個別のライトスクリプトを日本語化してみます：MAIL Postfix local delivery

  

  

    MAIL Postfix local delivery

  
  

>   
>
>     #!/bin/bash -ex
>     #
>     # Copyright (c) 2008-2011 RightScale, Inc, All Rights Reserved Worldwide.
>     #
>
>     postfix_file=/etc/postfix/main.cf
>     backupfile_time=`date +%H%M%S`
>     cp $postfix_file $postfix_file.$backupfile_time
>     #変数を設定しオリジナル設定ファイルをコピーしておく
>
>   
>
>     if [  "$RS_DISTRO" ==  "ubuntu" ]; then
>       if [ "$(lsb_release -rs)" == "8.04" ]; then
>         export DEBIAN_FRONTEND="noninteractive"; apt-get install  -y sysvconfig
>       fi
>       echo "Using Ubuntu default main.cf config"
>     else
>     # Make the changes needed for centos
>     sed -i 's/inet_interfaces = localhost/#inet_interfaces = localhost/' $postfix_file
>     #設定ファイルを書き換える（inet_interface=localhostを無効にする）
>     sed -i 's/#inet_interfaces = all/inet_interfaces = all/' $postfix_file
>     #設定ファイルを書き換える（inet_interface=allを有効にする）
>
>   
>
>     # Replace everything after the localhost.  This assumes that the last host entry is
>     # The host that this script added.  If there are other hosts added to this line by
>     # some other script then this will break.  A specialized script must be written to
>     # handle this case.
>     sed -i "s/^mydestination = $myhostname, localhost.$mydomain, localhost.*$/mydestination = $myhostname, localhost.$mydomain, localhost, $EC2_LOCAL_HOSTNAME/" $postfix_file
>     #さらに設定を追加する
>     service postfix reload
>     #postfixをリロード
>     fi
>
>   
