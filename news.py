#!/usr/bin/env python3
import psycopg2

x1 = "What are the most popular articles of all time?"
x2 = "What are the most popular article authors of all time?"
x3 = "On which days more than 1% of the requests lead to error?"

first_query = """
SELECT articles.title,
       count(*)
FROM log,
articles
WHERE log.path = '/article/' || articles.slug
GROUP BY articles.title
ORDER BY count(*) DESC
LIMIT 3;
"""

second_query = """
select authors.name, count(*) as views from articles inner join
authors on articles.author = authors.id inner join
log on concat('/article/', articles.slug) = log.path where
log.status like '%200%' group by authors.name order by views desc
"""

third_query = """
select * from (
    select a.day,
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
    as errp from
        (select date(time) as day, count(*) as hits from log group by day) as a
        inner join
        (select date(time) as day, count(*) as hits from log where status
        like '%404%' group by day) as b
    on a.day = b.day)
as t where errp > 1.0;
"""


class Problem:
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except Exception as e:
            print e

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def solve(self, ques, query, suffix='views'):
        query = query.replace('\n', ' ')
        result = self.execute_query(query)
        print ques
        for i in range(len(result)):
            print '\t', i + 1, '.', result[i][0], '->', result[i][1], suffix
        # blank line
        print ''

    def exit(self):
        self.db.close()


if __name__ == '__main__':
    problem = Problem()
    problem.solve(x1, first_query)
    problem.solve(x2, second_query)
    problem.solve(x3, third_query, '% error')
    problem.exit()
