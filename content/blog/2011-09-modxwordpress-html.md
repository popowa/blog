Title: MODxからWordpressにデータを変換する方法
Date: 2011-09-25 20:47
Authors: ayakomuro
Tags:  MODx, MySQL, wordpress
Slug:2011/09/modxwordpress
Status: published

前はMODxを使って構築をしていたのですが、色々自由すぎて作り込むのが大変なので、MODxからWordPressにデータを移行してみました。  

[]  
MODxのTableは色々あるのですが、メインなTableはmodx_site_contentです。  
そして今回は、MODx側で色々作り込んでいたので、以下の点をクリアしないといけません。

気をつける事

-   MODxのテンプレート変数機能を使っている
-   MODxの複数サイトが管理出来るContextを使っている
-   MODxの特定Contextの特定のページ（フォルダー）配下にある記事のみWordpressに移行
-   Wordpress側で、特定のカテゴリに紐付ける必要がある

MODx側Table

-   modx_site_content => メインコンテンツ
-   modx_site_templates => テンプレート
-   modx_site_tmplvars => テンプレート変数
-   modx_site_tmplvar_contentvalues　=> 実際のテンプレート変数の値
-   modx_site_tmplvar_templates
    =>テンプレートとテンプレート変数を紐付ける

関係性

1.  modx_site_content.template = modx_site_templates.id  
   コンテンツとテンプレートの紐付け
2.  modx_site_tmplvar_templates.templateid = modx_site_templates.id
3.  modx_site_tmplvar_templates.tmplvarid = modx_site_tmplvars.id  
   テンプレート変数とテンプレートの紐付け（２と３）
4.  modx_site_tmplvar_contentvalues.tmplvarid =
    modx_site_tmplvars.id
5.  modx_site_tmplvar_contentvalues.contentid =
    modx_site_content.id  
   実際の変数値とコンテンツの紐付け(4と5)

になっており、
modx_site_tmplvar_templatesと、modx_site_tmplvar_contentvaluesがassociative
entityになっております。

Wordpress側Table

-   wp_posts => コンテンツ
-   wp_term_taxonomy　=> カテゴリ
-   wp_term_relationships　=> カテゴリとコンテンツを紐付ける

関係性

1.  wp_posts.id = wp_term_taxonomy.object_id
2.  wp_term.id = wp_term_taxonomy.term_id
3.  wp_term_relationships.term_taxonomy_id = wp_term_taxonomy.id

になっており、 wp_term_relationshipsがassociative
entityになっております。

このMODxからコンテンツをWordpressに移行するのをなるべくSQL上で簡潔させたく、色々調べたら結構出来る事が分かったのでやってみました。

    /* Procedure作成
     * ここではWordpressのコンテンツとカテゴリを紐付けるProcudureを作成します。
     * wp_term_relationshipsに追加するカテゴリは既に作成されていてidが1である事を想定してます。
    */

    DROP PROCEDURE IF EXISTS insertcategory;
    DELIMITER //
    CREATE PROCEDURE insertcategory(IN param1 INT,IN param2 INT)
    BEGIN
     DECLARE v1 INT;
     DECLARE v2 INT;
     SET v1 = param1;
     SET v2 = param2;
      WHILE v1 < v2 DO
        SET v1 = v1 + 1;
        INSERT INTO wp_term_relationships VALUES(v1, 1, 0);
      END WHILE;
    END//
    DELIMITER ;

    /* Procedure作成
     * WPのtitleはURLエンコードされて入っているので、URLENCODEしてくれるProcedureを作成します。
     *
    */
    DELIMITER //
    CREATE FUNCTION urlencode (s VARCHAR(4096)) RETURNS VARCHAR(4096)
    DETERMINISTIC
    CONTAINS SQL
    BEGIN
           DECLARE c VARCHAR(4096) DEFAULT '';
           DECLARE pointer INT DEFAULT 1;
           DECLARE s2 VARCHAR(4096) DEFAULT '';

           IF ISNULL(s) THEN
               RETURN NULL;
           ELSE
           SET s2 = '';
           WHILE pointer <= length(s) DO
              SET c = MID(s,pointer,1);
              IF c = ' ' THEN
                 SET c = '+';
              ELSEIF NOT (ASCII(c) BETWEEN 48 AND 57 OR
                    ASCII(c) BETWEEN 65 AND 90 OR
                    ASCII(c) BETWEEN 97 AND 122) THEN
                 SET c = concat("%",LPAD(CONV(ASCII(c),10,16),2,0));
              END IF;
              SET s2 = CONCAT(s2,c);
              SET pointer = pointer + 1;
           END while;
           END IF;
           RETURN s2;
    END//
    DELIMITER ;

    /*
     * 実際にMODxからデータをWPに挿入します。
     * MODxでは複数サイトを一括で管理画面で管理、記事投稿が出来るので、
     * WHERE句で、特定のContext（ここではMyBlog）を選択し、
     * 特定の記事（Parent Idに紐づいている）のみをWPに移行します。
     *
    */
    INSERT INTO wp_posts (
     post_author,
     post_date,
     post_date_gmt,
     post_content,
     post_title,
     post_name,
     post_modified,
     post_modified_gmt
    )
    SELECT
     '1',
     FROM_UNIXTIME(c.publishedon,'%Y-%m-%d %H:%i:%S') as post_date,
     FROM_UNIXTIME(c.publishedon,'%Y-%m-%d %H:%i:%S') as post_date,
     concat(c.content, u.value),
     c.pagetitle,
     urlencode(c.pagetitle),
     FROM_UNIXTIME(c.publishedon,'%Y-%m-%d %H:%i:%S') as post_date,
     FROM_UNIXTIME(c.publishedon,'%Y-%m-%d %H:%i:%S') as post_date
    FROM
     modx_site_content as c
    LEFT JOIN
     modx_site_tmplvar_contentvalues as u
    ON c.id = u.contentid
    WHERE
     c.type="document" AND
     c.context_key="MyBlog" AND
     c.published=1 AND
     c.parent=5;

    / * WPに挿入しましたが、WP側の記事のカテゴリと紐付けていないので、紐付ける為にも
     * wp_term_relationshipsから最後のid番号を取得し（元々のwp_postsの最後のid）
     * MODxから挿入されたwp_postsの最新idを取得し、loopします。
    */

    SET @a1 = "1";
    SELECT @a1:=MAX(object_id) FROM wp_term_relationships;
    SET @b1 = "1";
    SELECT @b1:=MAX(id) FROM wp_posts;
    call insertcategory(@a1, @b1);

あまりにも特殊で誰も得をしないのではないか、と思ったのですが、とりあえずアップしておきます。
