#!/usr/bin/env python

import psycopg2,bleach
import sys

def main():
    """

    """
    db = psycopg2.connect(database="news")
    c = db.cursor()

    popular_articles(db,c)
    popular_authors(db,c)
    #error_days(db,c)

    db.close()


def popular_articles(db,c):
    """
    """
    c.execute("SELECT * FROM poparticles")
    results = c.fetchall()
    print("\nWhat are the most popular three articles of all time?\n")

    for title, views in results:
        print('\"{}\" - {} views'.format(title, views))
    

def popular_authors(db,c):
    """
    """
    c.execute("SELECT * FROM popauthors")
    results = c.fetchall()
    print("\nWho are the most popular article authors of all time?\n")
    for title, views in results:
        print('{} - {} views'.format(title, views))

def error_days(db,c):
    """
    """
    c.execute("")
    results = c.fetchall()
    print("\nOn which days did more than 1% of requests lead to errors\n")
    



if __name__ == "__main__":
    main()
