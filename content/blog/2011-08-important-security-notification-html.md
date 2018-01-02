Title: S3のsettings気をつけようね！
Date: 2011-08-24 15:43
Authors: ayakomuro
Tags:  AWS
Category: tech
Slug:2011/08/important-security-notification
Status: published


ちょっと前ですが、表題のメールがAmazonから来ました。  
なぬ！？と思って見てみましたが、自分が設定した通りの設定で、はて？と思いました。  

なんでこんなメールが来たんだろう、と考えた際に、元々S3は公開を前提としていない製品なのかなぁとまず思いました。DBのdumpファイル置いたり、アプリのソースを置いたりしてますもんね。  

後、S3の用途はとても多岐に渡っていて、本当に機密情報をも保管出来てしまうため、AWSが対応出来る以外の対応策（ユーザー主導のセキュリティ対策）について喚起したのでしょう。  

IAMが出来てからより細かな設定が出来るようになりましたので、ぜひよりセキュリアなデータをS3に起きつつも、公開用としての画像やファイルの配布などで適材適所の使い方をして行きたいですね。  

   
> [Dear Amazon S3 Customer,  
>   
> We've noticed that your Amazon S3 account has a bucket where your
> permissions allow anonymous requestors to perform READ operations,
> enumerating the contents of the bucket. Amazon S3 buckets are private
> by default. Recently, some tools and scripts have emerged which scan
> services like Amazon S3 and enumerate objects in publicly listable
> buckets. These tools could be used to identify objects in your bucket.
> The use of these tools against your buckets may also produce
> unintended charges in your account.  
>   
> We're always looking for ways to better serve our customers. We wanted
> to contact you in case you'd like to re-enable additional access
> control on your bucket to protect against unintended uses. We know
> there are good reasons why some of our customers prefer to allow
> anonymous access on buckets. This can simplify development against S3.
> Instead of using an authenticated client to access objects and pass
> them to end users, you allow end users to access objects directly.
> However, if you would like to modify your security configuration to
> protect your bucket by restricting access, Amazon S3 provides a number
> of powerful, simple means to define controls. Access Control Lists
> (ACLs) allow you to selectively grant permissions for a bucket (read,
> write, read ACL, and write ACL) to a list of grantees. You can also
> use Bucket Policies. Bucket Policies enable you to add or deny
> permissions across all or a subset of objects within a bucket. You can
> use wildcarding to define sets of objects within a bucket against
> which policy is applied, more granularly control the allowed
> operations, and even control access based on request properties.  
>   
> You can apply bucket policies or ACLs to your bucket using the [AWS
> Management
> Console](http://www.amazon.com/gp/r.html?R=O6R0FDUCS6A4&C=3I9Y3TLVAZY0I&H=WTOSANDX8CPTRE6WUCOHESL771UA&T=C&U=http%3A%2F%2Faws.amazon.com%2Fconsole%3Fref_%3Dpe_12300_20912970)
> or the [AWS
> SDK](http://www.amazon.com/gp/r.html?R=O6R0FDUCS6A4&C=3I9Y3TLVAZY0I&H=SZ99CBJ5VMJQLPRDLL53GSH4WE4A&T=C&U=http%3A%2F%2Faws.amazon.com%2Fcode%3Fref_%3Dpe_12300_20912970).
> You can also monitor use of your buckets by setting up Server Access
> Logging, described in our Developer Guide under [Setting Up Server Access Logging](http://www.amazon.com/gp/r.html?R=O6R0FDUCS6A4&C=3I9Y3TLVAZY0I&H=SBI6OCDEPWAWBO8JANT7P6NPMKMA&T=C&U=http%3A%2F%2Fdocs.amazonwebservices.com%2FAmazonS3%2Flatest%2Fdev%2Findex.html%3FLoggingHowTo.html).
> For further information on managing permissions on Amazon S3, please
> visit the [Amazon S3 Developer Guide](http://www.amazon.com/gp/r.html?R=O6R0FDUCS6A4&C=3I9Y3TLVAZY0I&H=ROAU1KAKZQBCJPSUL9NTRPTDJWKA&T=C&U=http%3A%2F%2Fdocs.amazonwebservices.com%2FAmazonS3%2Flatest%2Fdev%2F)
> topics on [Amazon S3 Access Control](http://www.amazon.com/gp/r.html?R=O6R0FDUCS6A4&C=3I9Y3TLVAZY0I&H=SBI6OCDEPWAWBO8JANT7P6NPMKMA&T=C&U=http%3A%2F%2Fdocs.amazonwebservices.com%2FAmazonS3%2Flatest%2Fdev%2Findex.html%3FLoggingHowTo.html)
> and the [AWS Security Center](http://www.amazon.com/gp/r.html?R=O6R0FDUCS6A4&C=3I9Y3TLVAZY0I&H=KVRQBHTZXBVAJCDCCPR5CDUGYTQA&T=C&U=http%3A%2F%2Faws.amazon.com%2Fsecurity%2F%3Fref_%3Dpe_12300_20912970).
> We also recommend Jeff Barr's blog post [Amazon S3 Bucket Policies -Another Way to Protect Your Content](http://www.amazon.com/gp/r.html?R=O6R0FDUCS6A4&C=3I9Y3TLVAZY0I&H=TU3BK9JAFWASDZA3K56OXVZRMSGA&T=C&U=http%3A%2F%2Faws.typepad.com%2Faws%2F2010%2F07%2Famazon-s3-bucket-policies-another-way-to-protect-your-content.html).  
>   
> Sincerely,  
>   
> The Amazon S3 Team  
>   
