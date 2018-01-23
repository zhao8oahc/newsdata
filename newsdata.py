#!/usr/bin/env python

import psycopg2
import sys

"""Connect to database
"""
db = psycopg2.connect(database="news")
c = db.cursor()

with open('results.txt', 'w') as f:
    f.truncate()
    """Gnerate the report of popular authors,
       popular articles and on which
       day errors occur more than 1%,
       and write the results into the text file
   """

    # List the top 3 popular articles
    c.execute("SELECT * FROM poparticles")
    results = c.fetchall()
    f.write("\n\n1.What are the most popular three articles of all time?\n")

    for title, views in results:
        f.write('\"{}\" - {} views \n'.format(title, views))

    # List the top 4 popular authors
    c.execute("SELECT * FROM popauthors")
    results = c.fetchall()
    f.write("\n\n2. Who are the most popular article authors of all time?\n")
    for title, views in results:
        f.write('{} - {} views \n'.format(title, views))

    # List the date that errors occur more than 1%
    c.execute("SELECT * FROM errorsrate")
    results = c.fetchall()
    f.write("\n\n3. On which days did more than 1% of requests "
            "lead to errors?\n")
    for dates, rate in results:
        f.write('{0:%B %d, %Y} - {1:.1f}% errors \n'.format(dates, rate))

f.close()
db.close()
