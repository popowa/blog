Title: 
Date: 2011-10-04 02:32
Authors: ayakomuro
Tags:  Noah cloud
Slug:2011/10/noah-ssh
Status: published


ポートの設定、SSHログイン+NOAHクラウドの登録、仮想マシンの起動は簡単だったのですが、ポートを開ける方法が分からずあれこれしたので、メモとして残しておきます。  
[]  
追加した仮想マシンは、ダッシュボードの横にあるリソースから見る事が出来ます。

[![](http://4.bp.blogspot.com/-8QzoyXQiv5Y/Topq_vnzaUI/AAAAAAAANks/sWB8KszGpt8/s1600/resource.png)](http://4.bp.blogspot.com/-8QzoyXQiv5Y/Topq_vnzaUI/AAAAAAAANks/sWB8KszGpt8/s1600/resource.png)

リソースをクリックすると、仮想マシン一覧が表示されますが、そこに表示されているIPアドレスはSSHやHTTPなどで外からアクセス出来る物はありません。

[![](http://2.bp.blogspot.com/-txnO7pieK-U/TopsH6WYV_I/AAAAAAAANkw/6rML1EhHDVI/s400/machine.png){width="400"
height="108"}](http://2.bp.blogspot.com/-txnO7pieK-U/TopsH6WYV_I/AAAAAAAANkw/6rML1EhHDVI/s1600/machine.png)

左側メニューにあるIPアドレス、というのをクリックすると、IPアドレス一覧が表示されます(AWSでいうとElastic
IP)。

[![](http://1.bp.blogspot.com/-W9Of-R3ipwU/Topss2YFBoI/AAAAAAAANk0/8J8q_ooucMM/s400/ip.png){width="400"
height="83"}](http://1.bp.blogspot.com/-W9Of-R3ipwU/Topss2YFBoI/AAAAAAAANk0/8J8q_ooucMM/s1600/ip.png)

その下に選択したIPアドレスの詳細、ファイヤーウォール、ポートフォワーディング、ロードバランサーのタブが表示されます。

[![](http://1.bp.blogspot.com/-5h754JC8LKg/ToptHZtE14I/AAAAAAAANk4/zsHDY-t5Dts/s1600/tab.png)](http://1.bp.blogspot.com/-5h754JC8LKg/ToptHZtE14I/AAAAAAAANk4/zsHDY-t5Dts/s1600/tab.png)

 SSHで接続出来るようにしてみます。  
まずファイヤーウォールに22ポートを開けます。接続元が動的IPなので、ソースCIDRは0.0.0.0/0にします。会社など固定IPならそのように設定した方がいいでしょう。

[![](http://3.bp.blogspot.com/-fgJLwy3BxOM/TopuGzWkdAI/AAAAAAAANk8/kQodmZLrm14/s1600/sshfw.png)](http://3.bp.blogspot.com/-fgJLwy3BxOM/TopuGzWkdAI/AAAAAAAANk8/kQodmZLrm14/s1600/sshfw.png)

 その後ポートフォワーディングタブをクリックし、外部の22ポートを個別仮想マシンのポートを紐付けます。

[![](http://2.bp.blogspot.com/-_TWmbSrWRWM/TopughqIiGI/AAAAAAAANlA/xEqnp7AuTOM/s1600/sshpf.png)](http://2.bp.blogspot.com/-_TWmbSrWRWM/TopughqIiGI/AAAAAAAANlA/xEqnp7AuTOM/s1600/sshpf.png)

その後、ターミナルを開き、先ほど保存した秘密鍵を使ってSSH接続してみます。

> aya-air:AccountInfo aya\$ ls -la \| grep tangerine.pem  
> -rwxrwxr-x@  1 aya  staff    887 10  4 06:14 tangerine.pem  
> aya-air:AccountInfo aya\$ chmod 700 tangerine.pem  
> aya-air:AccountInfo aya\$ ls -la \| grep tangerine.pem  
> -rwx\-\-\-\-\--@  1 aya  staff    887 10  4 06:14 tangerine.pem  
> aya-air:AccountInfo aya\$  ssh -i tangerine.pem root@xxx.xxx.xxx.xxx  
> The authenticity of host \'xxx.xxx.xxx.xxx (xxx.xxx.xxx.xxx)\' can\'t
> be established.  
> RSA key fingerprint is
> 58:a8:16:38:0c:31:32:28:b4:c6:8a:64:b8:ea:51:95.  
> Are you sure you want to continue connecting (yes/no)? yes  
> Linux ubuntu 2.6.32-33-server \#72-Ubuntu SMP Fri Jul 29 21:21:55 UTC
> 2011 x86\_64 GNU/Linux  
> Ubuntu 10.04.3 LTS
>
> Welcome to the Ubuntu Server!  
>  \* Documentation:  http://www.ubuntu.com/server/doc
>
> The programs included with the Ubuntu system are free software;  
> the exact distribution terms for each program are described in the  
> individual files in /usr/share/doc/\*/copyright.
>
> Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
> applicable law.  
> root@ubuntu:\~\#

ログイン出来ました！
