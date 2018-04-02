#!/usr/bin/env python3

import psycopg2

# Database Connection
conn = psycopg2.connect("dbname='news'")
cur = conn.cursor()


# Helper Methods
def query(sql_query):
    cur.execute(sql_query)
    return cur.fetchall()


# Output Methods
def get_top_three_articles():
    print("\n    ------------ Top 3 Articles of All Time ------------ \n")
    rows = query("SELECT title, count(*) as num \
                FROM articles \
                JOIN log ON articles.slug = SUBSTRING(log.path, 10) \
                GROUP BY articles.title \
                ORDER BY num desc LIMIT 3")
    for row in rows:
        print("    \"{}\" - {} Views".format(row[0], row[1]))


def get_popular_authors():
    print("\n    --------- Most Popular Authors of All Time --------- \n")
    rows = query("SELECT name, count(*) as num \
                FROM articles \
                JOIN log ON articles.slug = SUBSTRING(log.path, 10) \
                JOIN authors ON articles.author = authors.id \
                GROUP BY authors.name ORDER BY num desc")
    for row in rows:
        print("    {} - {} Views".format(row[0], row[1]))


def get_high_error_days():
    print("\n    -------- Days Where Greater Than 1% Errors --------- \n")
    rows = query("SELECT CAST(time as date), \
                CAST(SUM(CASE WHEN status = '404 NOT FOUND' \
                THEN 1 ELSE 0 END) as float) / \
                CAST(SUM(CASE WHEN status = '200 OK' \
                THEN 1 ELSE 0 END) as float) \
                FROM log \
                GROUP BY CAST(time as date)")
    for row in rows:
        if row[1] > 0.01:
            perc = "%.2f" % (row[1]*100)
            print("    {} - {}%".format(row[0], perc))


# Program Begin
print("---------------------------------------------------------")
print("                    Article Log Analysis")
print("---------------------------------------------------------")

get_top_three_articles()
get_popular_authors()
get_high_error_days()

print()  # Empty line before program ends

conn.close()
