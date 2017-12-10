Title: 
Date: 2011-07-31 05:50
Authors: ayakomuro
Tags:  RightScript
Slug:2011/07/sys-syslog-remote-logging-client
Status: published


client+個別のライトスクリプトを日本語化してみます：SYS Syslog remote
logging client  
[]  
**SYS Syslog remote logging client**  
  

>   
>
>     #!/bin/bash -ex
>     # Copyright (c) 2007-2011 by RightScale Inc., all rights reserved
>     set +e
>     #シェルオプション設定コマンドsetでコマンドが0以外のステータスで終了した場合，
>     #一部の場合を除いて即座に終了しないようにする
>     which rs_tag
>     #
>     if [ "$?" -ne 0 ]; then
>     #rs_tagのパスの値（$?)が0ではなかった場合、
>       echo -e "FATAL ERROR: this RightScript only supports v5 based
>     　RightImages that have rs_tag support!
>     　You must use SYS Syslog Remote Logging Client v7 instead if you are using a v4 RightImage"
>      #ライトスクリプトはrs_tagに対応しているv5ベースのライトイメージに対応している 
>      #v4のライトイメージだった場合は、SYS Syslog Remote Logging client v7を使う必要がある
>     exit 1
>     fi
>     set -e
>     # Auto-gernerate config file
>     function write_config
>     #write_config関数を作成する
>     {
>       [ -e /etc/syslog-ng/syslog-ng.conf ] && mv -f /etc/syslog-ng/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf.bak.$(date "+%Y%m%d%H%M%S")
>     　#syslog-ng.confがあって、そのファイルを日時付きでバックアップ出来たら
>       cp $RS_ATTACH_DIR/syslog-ng-remote.conf /etc/syslog-ng/syslog-ng.conf
>       #RS_ATTACH_DIRに添付されているsyslog-ng-remote.confからコピーする
>       #Inject Instance ID into config
>       perl -p -i -e 's/i-123456/'$SERVER_UUID'/' /etc/syslog-ng/syslog-ng.conf
>     　#InstanceのIDをコンフィグ内に書き込む
>       #set syslog server.
>       perl -p -i -e 's/syslog.rightscale.com/'$SYSLOG_SERVER'/' /etc/syslog-ng/syslog-ng.conf
>       # Set apache log dir (for haproxy.log)
>       sed -i "/@@APACHE_LOG_DIR@@/s//$apache_log_dir/" /etc/syslog-ng/syslog-ng.conf
>     }
>     if [ "$RS_DISTRO" = ubuntu ]; then #ディストリビューションがUbuntuだったら
>       logrotate_file=/etc/logrotate.d/syslog-ng
>       apache_log_dir=apache2
>     elif [ "$RS_DISTRO" = centos ]; then #ディストリビューションがCenntosだったら
>       logrotate_file=/etc/logrotate.d/syslog
>       apache_log_dir=httpd
>     fi
>
>     # Test if this script has already run.  If so it is either a boot script being re-run
>     # or the server is being started from a stopped state.  Update the config - same as reboot.
>     if test "$RS_REBOOT" = "true" -o "$RS_ALREADY_RUN" = "true"; then
>     #もしリブート処理だったり、すでに起動済みだった場合
>       echo "Update SYSLOG configuration on REBOOT."
>       write_config
>       #先ほどの関数を走らせて、アップデートを行う
>       service syslog-ng restart
>       #syslogn-ngをリスタートさせる
>       # Tag instance for start/stop support
>       rs_tag -a "rs_logging:state=active" && echo "Setting logging active tag"
>     　#rs_tagで設定する（rs_tag説明部分を参照）
>       logger -t RightScale "Updated SYSLOG configuration on REBOOT."
>     　#logに記録
>       exit 0
>     fi
>
>     if [ "$RS_DISTRO" = ubuntu ]; then
>       apt-get install -y syslog-ng #必要パッケージをインストール
>       if [ "$(lsb_release -rs)" == "8.04" ]; then
>     　#lsb_releaseコマンドを使って現在のバージョンを確認。8.04だったら
>         export DEBIAN_FRONTEND="noninteractive"; apt-get install  -y sysvconfig
>     　　#syslong-ngだけではなくsysvconfigもインストール
>       fi
>     elif [ "$RS_DISTRO" = centos ]; then
>       yum install -y syslog-ng
>     fi
>
>     #create a new /dev/null for syslog-ng to use
>     #
>     if [ ! -e /dev/null.syslog-ng ]; then #もしスペシャルファイル作成されていなかったらmknodで作成する
>       mknod /dev/null.syslog-ng c 1 3
>     fi
>
>     write_config #先ほどの関数を走らせる
>     # Ensure everything in /var/log is owned by root, not syslog.
>     chown root /var/log/* #ファイル/ディレクトリの所有者を変更する
>     service syslog-ng restart #syslog-ngを再起動
>
>     # Set up log file rotation #ログローテイトの設定
>     perl -p -i -e 's/weekly/daily/; s/rotates+d+/rotate 7/' /etc/logrotate.conf
>
>     # fix /var/log/boot.log issue #ブートログのバグを対応する
>     [ ! -e /var/log/boot.log ] && touch /var/log/boot.log 
>
>     [ -z "$(grep -lir "missingok" $logrotate_file)" ] && sed -i '/sharedscripts/ a    missingok' $logrotate_file
>     #logrotate_fileからmissingokを検索して、文字数が0だったら、logrotate_fileに'sharedscripts'の後に'missingok'を追加する
>     [ -z "$(grep -lir "notifempty" $logrotate_file)" ] && sed -i '/sharedscripts/ a    notifempty' $logrotate_file
>
>     # add mail to logrotate
>     mkdir -p /var/spool/oldmail
>     chmod 775 /var/spool/oldmail
>     chown root:mail /var/spool/oldmail
>
>     cat <<EOF> /etc/logrotate.d/mail
>     /var/spool/mail/* {
>        daily
>        compress
>        notifempty
>        missingok
>        olddir /var/spool/oldmail
>     }
>     #/etc/logrotate.d/mailを上書きする
>     EOF
>
>     # tag required for RightLink enabled images
>     rs_tag -a "rs_logging:state=active" && echo "Setting logging active tag"
>     #rs_tagを使ってタグを追加する
>
>   

  
 
