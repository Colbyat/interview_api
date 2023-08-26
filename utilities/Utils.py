import sqlite3
import pandas
from sqlite3 import Error


def verticaljsontopandasdf(json):
    return pandas.DataFrame(json[1:], columns=json[0])


verticaljsontopandasdf.__doc__ = """Takes a given json in the format of: [[column_labels], [row_1], [row_2],...[row_n]]
                                     and outputs a pandas dataframe with the given data."""


def savecsvtodb(id_url, csv):
    connection = None
    try:
        connection = sqlite3.connect("C:/Users/Colby/PycharmProjects/interview/db.db")
        cursor = connection.cursor()
        query = """INSERT INTO persist(url, csv)
                    VALUES (?, ?)"""
        cursor.execute(query, (id_url, csv))
        connection.commit()
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()
    return None


def grabfromdb(id_url):
    connection = None
    select_val = None
    try:
        connection = sqlite3.connect("C:/Users/Colby/PycharmProjects/interview/db.db")
        cursor = connection.cursor()
        query = "SELECT csv FROM persist where url=?"
        cursor.execute(query, (id_url,))
        select_val = cursor.fetchone()
        if select_val is not None:
            select_val = select_val[0]
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()
    return select_val