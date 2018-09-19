# -*- coding: utf-8 -*-
import psycopg2

DBNAME = "news"


def main(query):
    # connect to database
    connection = psycopg2.connect(database=DBNAME)
    c = connection.cursor()
    c.execute(query)
    results = c.fetchall()
    connection.close()
    return results


def topposts_print():
    print ("Posts mais populares")
    print ('----------------------')
    query1 = """
        select topposts.title , topposts.views as views
        from topposts order by topposts.views desc limit 5;
        """
    popular_articles = main(query1)
    for (title, views) in popular_articles:
        print(" {} - {} views".format(title, views))
    print ("\n")


def topauthors_print():
    print ("Autores mais populares")
    print ('----------------------')
    query2 = """
        select topauthors.name,topauthors.views
        as views from topauthors order by views desc;
        """
    popular_authors = main(query2)
    for(name, views) in popular_authors:
        print(" {} - {} views".format(name, views))
    print ("\n")


def error_day_print():
    print("Dias em que tiveram mais de 1 por cento de falha nas requisições")
    print ('----------------------')
    query3 = """
        select * from error_per_day;
        """
    errorDay = main(query3)
    for i in errorDay:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1] * 1, 1)) + "%" + " errors"
        print(date + "---" + errors)


if __name__ == "__main__":
    topposts_print()
    topauthors_print()
    error_day_print()
