Title: \[追記\]　Oracle RDSとSYSDATEの関係
Date: 2012-09-25 07:23
Authors: ayakomuro
Tags:  AWS, Oracle
Slug:2012/09/oracle-rdssysdate
Status: published

\[追記\]Oracle

RDSでsysdate変更が出来る様になった  
<http://aws.amazon.com/jp/about-aws/whats-new/2014/01/13/amazon-rds-for-oracle-now-supports-time-zone-change/>

\[今日の結論\] Oracle RDSでSYSDATEを変更する事は出来ない。

SYSDATE関数は、システム（仮想サーバ？）の日付を返す為、RDSの入っているサーバの日付を変えるしかたぶん対応が出来ないが、そもそもRDSでは仮想サーバにアクセス出来ない。

調べた所、SYSDATEを仮想的に変更するには、FIXED\_DATE初期化パラメーターを使用する必要があり、Oracle
RDSでは、FIXED\_DATEを設定する事は禁止されている。

\[今後のタスク\] Oracleをちゃんと触る
