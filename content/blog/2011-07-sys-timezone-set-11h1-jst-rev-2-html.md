Title: 
Date: 2011-07-31 05:42
Authors: ayakomuro
Tags:  RightScript
Slug:2011/07/sys-timezone-set-11h1-jst-rev-2
Status: published


2\]+個別のライトスクリプトを日本語化してみます。SYS Timezone set - 11H1
JST \[rev 2\]  
  
[]  
  
**SYS Timezone set - 11H1 JST \[rev 2\]**  
  

>   
>
>     #!/bin/bash -ex
>     #
>     # Copyright (c) 2008-2011 RightScale, Inc, All Rights Reserved Worldwide.
>     #
>
>     #
>     # Test for a reboot,  if this is a reboot just skip this script.
>     #
>     if test "$RS_REBOOT" = "true" ; then 
>     #もしリブートだったら
>
>   
>
>       echo "Skip re-setting Timezone on reboot."
>     　#タイム設定をスキップする
>       exit 0 # Leave with a smile ...
>     　#exit 0値が返るとスクリプトは終了します
>     fi
>
>     #
>     # If this parameter is not set leave unchanged and use localtime
>     #
>     if [ "$SYS_TZINFO" = "localtime" ]; then
>     　#localtimeなら
>       echo "SYS_TZINFO set to localtime.  Not changing /etc/localtime..."
>     　#変更しない。
>       exit 0
>     　#スクリプトを抜ける
>     else
>       tzset="$SYS_TZINFO"
>       #Inputの$SYS_TZINFOで設定した値をtzsetという変数値に入れる
>     fi
>     #
>     # Set the Timezone
>     #
>     ln -sf /usr/share/zoneinfo/$tzset /etc/localtime
>     #シンボリックリンクを貼って設定する
>     echo "Timezone set to $tzset"
>     # $tzset(=$SYS_TZINFO)に設定したとエコー
>
>     logger -t RightScale "Timezone set to $tzset"
>     #ログに記録
>     exit 0
>     #スクリプトを終了
>
>   

  
 
