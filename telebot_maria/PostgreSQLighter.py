import sqlite3
import psycopg2
import sys
import pprint

class PostgreSQLighter:

    def __init__(self, database):
        conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
        print ("Connecting to database", conn_string)
        self.connection = psycopg2.connect(conn_string) 
        self.cursor = connection.cursor()
        # execute our Query
        # cursor.execute("SELECT * FROM music")
        # records = cursor.fetchall()
        # pprint.pprint(records)

    # def __init__(self, database):
    #     self.connection = sqlite3.connect(database)
    #     self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM music').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM music WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM music').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()