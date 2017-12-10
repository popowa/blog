Title: 
Date: 2013-07-15 21:51
Authors: ayakomuro
Tags:  AWS, S3
Slug:2013/07/amazon-linuxs3cmd
Status: published


LinuxでS3cmdをインストール＆利用する方法+いつ書いた記事か忘れたけど、非公開だったので公開。



なんていつも公開忘れてしまうのだろうか。



\-\--

Amazon
Linuxにはs3cmdが入っていると聞いていたけど入っていなかったので、入れてみた。

wget http://s3tools.org/repo/RHEL\_6/s3tools.repo \~/  
sudo cp s3tools.repo /etc/yum.repos.d/  
sudo yum -y install s3cmd

Loaded plugins: downloadonly, fastestmirror, priorities, security,
update-motd, upgrade-helper  
Loading mirror speeds from cached hostfile  
\* amzn-main: packages.ap-northeast-1.amazonaws.com  
\* amzn-updates: packages.ap-northeast-1.amazonaws.com  
amzn-main \| 2.1 kB 00:00  
amzn-updates \| 2.3 kB 00:00  
s3tools \| 1.3 kB 00:00  
s3tools/primary \| 1.0 kB 00:00  
s3tools 3/3  
Setting up Install Process  
Resolving Dependencies  
\--\> Running transaction check  
\-\--\> Package s3cmd.i386 0:1.0.0-4.1 will be installed  
\--\> Finished Dependency Resolution  
Dependencies Resolved  
===================================================================================================================================================  
Package Arch Version Repository Size  
===================================================================================================================================================  
Installing:  
s3cmd i386 1.0.0-4.1 s3tools 91 k  
Transaction Summary  
===================================================================================================================================================  
Install 1 Package(s)  
Total download size: 91 k  
Installed size: 296 k  
Downloading Packages:  
s3cmd-1.0.0-4.1.i386.rpm \| 91 kB 00:01  
警告: rpmts\_HdrFromFdno: ヘッダ V3 DSA/SHA1 Signature, key ID e612b227:
NOKEY  
Retrieving key from
http://s3tools.org/repo/RHEL\_6/repodata/repomd.xml.key  
Importing GPG key 0xE612B227:  
Userid: \"home:mludvig OBS Project
\<home:mludvig@build.opensuse.org\>\"  
From : http://s3tools.org/repo/RHEL\_6/repodata/repomd.xml.key  
Running rpm\_check\_debug  
Running Transaction Test  
Transaction Test Succeeded  
Running Transaction  
Installing : s3cmd-1.0.0-4.1.i386 1/1  
Verifying : s3cmd-1.0.0-4.1.i386 1/1  
Installed:  
s3cmd.i386 0:1.0.0-4.1

Complete!

\$ s3cmd \--configure

Enter new values or accept defaults in brackets with Enter.  
Refer to user manual for detailed description of all options.

Access key and Secret key are your identifiers for Amazon S3  
Access Key: アクセスキー  
Secret Key: シークレットキー

Encryption password is used to protect your files from reading  
by unauthorized persons while in transfer to S3  
Encryption password:  
Path to GPG program \[/usr/bin/gpg\]:

When using secure HTTPS protocol all communication with Amazon S3  
servers is protected from 3rd party eavesdropping. This method is  
slower than plain HTTP and can\'t be used if you\'re behind a proxy  
Use HTTPS protocol \[No\]:

On some networks all internet access must go through a HTTP proxy.  
Try setting it here if you can\'t conect to S3 directly  
HTTP Proxy server name:

New settings:  
Access Key: アクセスキー  
Secret Key: シークレットキー  
Encryption password:  
Path to GPG program: /usr/bin/gpg  
Use HTTPS protocol: False  
HTTP Proxy server name:  
HTTP Proxy server port: 0

Test access with supplied credentials? \[Y/n\] y  
Please wait\...  
Success. Your access key and secret key worked fine :-)  
Now verifying that encryption works\...  
Not configured. Never mind.

Save settings? \[y/N\] y  
Configuration saved to \'/home/ec2-user/.s3cfg\'




