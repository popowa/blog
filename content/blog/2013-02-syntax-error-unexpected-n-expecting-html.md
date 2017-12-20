Title: syntax error, unexpected \'n\', expecting tCOLON2 or \'\[\' or \'.\'
Date: 2013-02-11 06:34
Authors: ayakomuro
Tags:  error, Rails
Slug:2013/02/syntax-error-unexpected-n-expecting
Status: published






急にdb:migrateしようとしたら怒られる様になった。



20130211061203\_create\_settings.rbを見ても特に普段と変わらない様子。

> \$rake db:migrate  
> rake aborted!  
> /Users/komuro/rails-demo/db/migrate/20130211061203\_create\_settings.rb:4:
> syntax error, unexpected \'n\', expecting tCOLON2 or \'\[\' or \'.\'

何だろうと思ったらどうやら  

> \$ rails generate scaffold Setting accesskey:string[,
> ]secretkey:string

設定のカンマ(,)がいらなかったようです。

そのような場合は一度作成した一式を削除しましょう。

> \$ rails destroy scaffold Setting

それから再度カンマ無しで作成。



>   
> \$ rails generate scaffold Setting accesskey:string secretkey:string

\--  
english  
\--



Suddenly, db:migrate gave me a error (see below)



20130211061203\_create\_settings.rb doesn\'t look so strange from
path..hmmm

> \$rake db:migrate  
> rake aborted!  
> /Users/komuro/rails-demo/db/migrate/20130211061203\_create\_settings.rb:4:
> syntax error, unexpected \'n\', expecting tCOLON2 or \'\[\' or \'.\'

I googled and found out that I typed comma when I generate scaffold.  

> \$ rails generate scaffold Setting
> accesskey:string[, ]secretkey:string

No comma!

If you type it with comma, delete scaffold first.  

> \$ rails destroy scaffold Setting

Then type again w/o comma.



> \$ rails generate scaffold Setting accesskey:string secretkey:string
>
> 
>
> 




