Title: 
Date: 2013-02-11 01:17
Authors: ayakomuro
Tags:  Rails
Slug:2013/02/security-warning-no-secret-option
Status: published


と出たら+  
Rails関連で何かコマンドを打つと以下の様に出るようになった。

SECURITY WARNING: No secret option provided to Rack::Session::Cookie.  
        This poses a security threat. It is strongly recommended that
you  
        provide a secret to prevent exploits that may be possible from
crafted  
        cookies. This will not be supported in future versions of Rack,
and  
        future versions will even invalidate your existing user cookies.

調べてみたら以下のissueで議論されていた。

-   <https://github.com/rails/rails/issues/7372>

2013年1月に出た3.2.11で対応したもよう。

-   <https://github.com/rails/rails/commit/95fe9ef945a35f56fa1c3ef356aec4a3b868937c>

一度Rails/rackをアップデートするといいかもしれない。

\$ gem list \--local  
で確認して、アップデートの必要があれば  
\$ gem update rails  
とか  
\$ gem update rack  
とかする
