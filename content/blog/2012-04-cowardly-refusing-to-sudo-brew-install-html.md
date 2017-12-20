Title: 
Date: 2012-04-05 02:13
Authors: ayakomuro
Tags:  brew, Python
Slug:2012/04/cowardly-refusing-to-sudo-brew-install
Status: published


install\'って言われたよ+brewでpythonを入れようと思ったらこんなのが出た

> Komuro-no-MacBook-Air:\~ komuro\$ sudo brew install python  
> Password:  
> Cowardly refusing to \`sudo brew install\'

sudoじゃだめなのか？と思ってsuになってやってみた

[]  

> Komuro-no-MacBook-Air:\~ komuro\$ sudo su  
> sh-3.2\# brew install python  
> Cowardly refusing to \`sudo brew install\'

調べたところ、brewは権限を昇格させる必要がないように設計されており、むしろsudo権限がある状態でのbrew操作しないようにしているそうです。

<https://github.com/mxcl/homebrew/wiki/FAQ>  

> Why does Homebrew say sudo is bad?
> ----------------------------------
>
> **tl;dr** Sudo is dangerous, and you installed TextMate.app without
> sudo anyway.
>
> Homebrew is designed to work without using sudo. You can decide to use
> it but we strongly recommend not to do so. If you have used sudo and
> run into a bug then it is likely to be the cause. Please don't file a
> bug report unless you can reproduce it after reinstalling Homebrew
> from scratch without using sudo.  
> You should only ever sudo a tool you trust. Of course, you can trust
> Homebrew ;) But do you trust the multi-megabyte Makefile that Homebrew
> runs? Developers often understand C++ far better than they understand
> make syntax. It's too high a risk to sudo such stuff. It could break
> your base system, or alter it subtly.  
> And indeed, we've seen some build scripts try to modify `/usr` even
> when the prefix was specified as something else entirely.
>
> Did you `chown root /Applications/TextMate.app`? Probably not. So is
> it that important to `chown root wget`?

make sense!
