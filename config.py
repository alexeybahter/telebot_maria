import telebot
import psycopg2
import sys
import pprint
import os
import random
# import utils

# token = '499234171:AAHR08WY32nqUO5T8K8YLv4YJVwdJQqHHLg'
token = '482230820:AAGcOEQcM75FXrEpIY_9dZlDKHv6xD7x8rc'
word_id = ''
en_word = ''
ru_word = ''
row_wordlist = ''
row_users_wordlist = ''
path_audio = ''
transcription = ''
msg_word = ''
count_learn = 0
callback = ''
row_repeat_word = ''
count_repeat = 0
# records = ''
def connect_to_db():
    conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM english_words")
    # records = cursor.fetchall()
    # return cursor

def create_new_user(user_id):
    conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    user = cursor.execute('INSERT INTO users (user_id) VALUES (' + str(user_id) + ') RETURNING user_id;')
    cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

def get_username_from_storage(unique_code): 
    conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    print("get_username_from_storage : users = ", users)
    for user in users:
        # print('-0-0-0-0-0-0-user', user[0])
        if user[0] == unique_code:
            print('user == unique_code', user)
            return user
    # return users


def select_row_from_wordlist(user_id):
    conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
    # print ("Connecting to database", conn_string)
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    # cursor.execute('SELECT * FROM public.wordlist, public.users_wordlist WHERE wordlist.word_id NOT IN (SELECT users_wordlist.word_id FROM public.users_wordlist) AND users_wordlist.id = 108 ORDER BY wordlist.word_id ASC LIMIT 10;')
    cursor.execute('SELECT wordlist.* FROM wordlist wordlist LEFT JOIN users_wordlist users_wordlist ON wordlist.word_id = users_wordlist.word_id AND users_wordlist.user_id = ' + str(user_id) + ' WHERE users_wordlist.word_id IS NULL LIMIT 10;')
    # cursor.execute('SELECT * FROM wordlist LEFT JOIN users_wordlist ON users_wordlist.word_id != wordlist.word_id WHERE users_wordlist.learn_word IS NULL LIMIT 1;')
    row_wordlist = cursor.fetchall()
    return row_wordlist

def add_path_audio(path_audio):
    conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    word = cursor.execute("UPDATE wordlist SET path_audio = '" + path_audio + '.mp3' + "' WHERE en_word = '" + path_audio + "' RETURNING path_audio;")
    print("word_word_word_word_word_word_word_word_", word)
    # print('INSERT INTO users VALUES (' + str(user_id) + ');', user_id)
    cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

def learn_word(word_id, user_id):
    conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    word = cursor.execute('INSERT INTO  users_wordlist ( user_id, word_id, learn_word) VALUES ('+ str(user_id) + ',' + str(word_id) + ', true)  RETURNING word_id;')
    print("word_word_word_word_word_word_word_word_", word)
    # print('INSERT INTO users VALUES (' + str(user_id) + ');', user_id)
    cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

def set_know_word(word_id, user_id):
    conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()    
    word = cursor.execute('INSERT INTO  users_wordlist ( user_id, word_id, know_word) VALUES ('+ str(user_id) + ',' + str(word_id) + ', true)  RETURNING word_id;')
    print("ef set_know_word", word)
    # print('INSERT INTO users VALUES (' + str(user_id) + ');', user_id)
    cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

def select_row_from_users_wordlist(user_id):
    conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    cursor.execute('SELECT wordlist.word_id,en_word,ru_word,transcription,user_id FROM wordlist JOIN users_wordlist ON wordlist.word_id = users_wordlist.word_id WHERE users_wordlist.user_id =' + str(user_id) + ';')
    # поставить счетчик для повторений count_repeat_word
    #  дополнить запрос с сравнением по ф
    row_users_wordlist = cursor.fetchall()
    # print("_row", row_users_wordlist)
    return row_users_wordlist



if __name__ == '__main__':
    # bot.polling(none_stop=True)
    # utils.count_rows()
    # random.seed()
    connect_to_db()
    # select_from_row(rownum)
    
