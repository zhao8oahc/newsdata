CREATE VIEW articleslog AS
    SELECT log.id AS logcode, articles.slug, articles.id AS articlenum
    FROM articles, log
    WHERE log.path = '/article/' || articles.slug;

CREATE VIEW poparticles AS
    SELECT articles.title, count(*) AS views
    FROM articles, articleslog
    WHERE articles.slug = articleslog.slug
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 3;

CREATE VIEW popauthors AS
    SELECT authors.name, count(*) AS views
    FROM articles, authors, articleslog
    WHERE articles.author = authors.id and articles.slug = articleslog.slug
    GROUP BY authors.name
    ORDER BY views DESC
    LIMIT 4;

CREATE VIEW errors AS
    SELECT 


    WHERE status = '404 NOT FOUND'