import config
import telebot
import psycopg2
import sys
import pprint
import os
import random
import utils
import audio
from random import shuffle

bot = telebot.TeleBot(config.token)

# def connect_to_db():
#     conn_string = "host='localhost' dbname='telebot_db' user='alexey' password=''"
#     # print the connection string we will use to connect
#     print ("Connecting to database", conn_string)
#     # get a connection, if a connect cannot be made an exception will be raised here
#     connection = psycopg2.connect(conn_string)
#     # conn.cursor will return a cursor object, you can use this cursor to perform queries
#     cursor = connection.cursor()
#     # execute our Query
#     cursor.execute("SELECT * FROM music")
#     # retrieve the records from the database
#     records = cursor.fetchall()
#     # print(records)
# def select_all():
#     """ Получаем все строки """
#     # return records
#     # with self.connection:
#         # return cursor.execute('SELECT * FROM music').fetchall()

# def select_single(self, rownum):
#     """ Получаем одну строку с номером rownum """
#     with self.connection:
#         return self.cursor.execute('SELECT * FROM music WHERE id = ?', (rownum,)).fetchall()[0]

# def count_rows(self):
#     """ Считаем количество строк """
#     with self.connection:
#         result = self.cursor.execute('SELECT * FROM music').fetchall()
#         return len(result)

# def close(self):
#     """ Закрываем текущее соединение с БД """
#     self.connection.close()
    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.

    # pprint.pprint(records)
    
    # for line in records:
    #     records_line =  line[1]
    #     print('records_line', records_line)
    # print('records_line123', records_line)

    # list = [1,2,3,4,5]
    # list_random = random.choice(list)
    # print ("-----------------------------------------------------list_random", list_random)
    # rows = cursor.fetchall()
    # print ("\nShow me the databases:\n")
    # for row in records:
    #     print ("---", random.choice(row[2]))
# if __name__ == "__main__":
    # main()
# conn = psycopg2.connect(database='telebot_db', user='alexey', 
# password='', host='127.0.0.1', port='5432')
# print("I am unable to connect to the database")
# cur = conn.cursor()
# all = cur.execute("SELECT * from music;")
# print ('-------', conn)
# print ('all', all)
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)

# @bot.message_handler(commands=['game'])
# def game(message):
#     # Подключаемся к БД
#     db_worker = PostgreSQLighter(config.database_name)
#     # Получаем случайную строку из БД
#     row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
#     # Формируем разметку
#     markup = utils.generate_markup(row[2], row[3])
#     # Отправляем аудиофайл с вариантами ответа
#     bot.send_voice(message.chat.id, row[1], reply_markup=markup)
#     # Включаем "игровой режим"
#     utils.set_user_game(message.chat.id, row[2])
#     # Отсоединяемся от БД
#     db_worker.close()

# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def check_answer(message):
#     # Если функция возвращает None -> Человек не в игре
#     answer = utils.get_answer_for_user(message.chat.id)
#     # Как Вы помните, answer может быть либо текст, либо None
#     # Если None:
#     if not answer:
#         bot.send_message(message.chat.id, 'Чтобы начать игру, выберите команду /game')
#     else:
#         # Уберем клавиатуру с вариантами ответа.
#         keyboard_hider = types.ReplyKeyboardRemove()
#         # Если ответ правильный/неправильный
#         if message.text == answer:
#             bot.send_message(message.chat.id, 'Верно!', reply_markup=keyboard_hider)
#         else:
#             bot.send_message(message.chat.id, 'т', reply_markup=keyboard_hider)
#         # Удаляем юзера из хранилища (игра закончена)
#         utils.finish_user_game(message.chat.id)

# def first_messafe_for_user:
#     if id_user == 

''' 
    For users
'''

# def extract_unique_code(text):
#     # Extracts the unique_code from the sent /start command.
#     return text.split()[1] if len(text.split()) > 1 else None

# def in_storage(unique_code): 
#     # Should check if a unique code exists in storage
#     return True

# # def get_username_from_storage(unique_code): 
# #     # Does a query to the storage, retrieving the associated username
# #     # Should be replaced by a real database-lookup.
# #     return "ABC" if in_storage(unique_code) else None

# def save_chat_id(chat_id, username):
#     # Save the chat_id->username to storage
#     # Should be replaced by a real database query.
#     pass
# @bot.message_handler(func=lambda message: message.text="Кафель")
@bot.message_handler(commands=['start1'])
def send_welcome(message):
    unique_code = message.chat.id
    print('unique_code = ', unique_code)
    if unique_code: # if the '/start' command contains a unique_code
        username = config.get_username_from_storage(unique_code)
        print('username', username)
        if username: # if the username exists in our database
            bot.send_message(message.chat.id, "Вы уже писали мне, я Вас знаю!")
        else:
            # print('user_unique_code', unique_code)
            user = config.create_new_user(unique_code)
            # print('config.create_new_user : users = ', user)
            bot.send_message(message.chat.id, "Это твой первый раз, Поздравляю! Теперь я тебя знаю.")
    else:
        bot.send_message(message.chat.id, "Что-то с чем-то")

# Обработчик команд '/start' и '/help'.
# @bot.message_handler(func=lambda message: message.text == "Главная")
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    # markup.row('\U0001F4DD /learn','\U0001F504 /repeat')
    markup.row('/learning','/repeat')
    bot.send_message(message.chat.id, "Привет! Что ты хочешь, милый? \U0001F60F", reply_markup=markup)


# @bot.message_handler(func=lambda message: message.text == "/learn")
@bot.message_handler(commands=['learning'])
def handle_learning(message):
    row = config.select_row_from_english_words()
    print('------row = ', row)
    for word in row:
        config.word_id = word[0]
        config.en_word = word[1]
        config.ru_word = word[2]
        config.path_audio = word[3]
        config.msg_word = "<b>" + config.en_word.upper() + "</b> - " + config.ru_word + " "
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row('/learn', '/know')
    bot.send_message(message.chat.id, config.msg_word, reply_markup=markup, parse_mode="HTML")
    print('audio.file', audio.file)
    msg = bot.send_voice(message.chat.id, audio.download_or_get_audio(config.en_word), None)

@bot.message_handler(commands=['learn'])
def handle_learn_word(message):
    print("word_id_word_id_word_id_word_id_word_id_", config.word_id)
    config.learn_word(config.word_id, message.chat.id)
    config.count += 1
    # callback = telebot.types.CallbackQuery(config.count, message.chat.id, config.count, message.chat.id)
    if config.count != 5:
        print('config.count', config.count)
        # print("callback", callback)
        handle_learning(message)
    else:
        config.count = 0
        # callback = ''
        # bot.send_message(message.chat.id, "Ты узнал 10 новых слов, пора их повторить!")
        markup = telebot.types.ReplyKeyboardMarkup(True, True)
        markup.row('/learning', '/repeat')
        bot.send_message(message.chat.id, "Ты узнал 5 новых слов, пора их повторить!", reply_markup=markup)
    # bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

# def check_repeat_words(word, click_word):

@bot.message_handler(commands=['know'])
def handle_learn_word(message):
    config.set_know_word(config.word_id, message.chat.id)
    print("know_know_know_know")

def new_en_word_send_for_repeat(message):
    print('config.row_repeat_word', config.row_repeat_word)
    if config.row_repeat_word:
        # markup = telebot.types.ReplyKeyboardMarkup(True, True)
        # print('row__select_row_from_users_wordlist', config.row_repeat_word)
        words_length = len(config.row_repeat_word)
        print('len = ', words_length)
        print('config.count_repeat', config.count_repeat)
        print('config.row_repeat_word[config.count_repeat]', config.row_repeat_word[config.count_repeat][1])
        config.word_id = config.row_repeat_word[config.count_repeat][0]
        config.en_word = config.row_repeat_word[config.count_repeat][1]
        config.ru_word = config.row_repeat_word[config.count_repeat][2]
        config.msg_word =  "<b> " + config.ru_word + "</b>"
        markup = telebot.types.ReplyKeyboardMarkup(True, True) # вот этой кнопки
        x = [[i] for i in range(10)]
        list_answer = [config.en_word,'*****','*****','*****']
        shuffle(list_answer)
        for item in list_answer:
            markup.row(item)
        bot.send_message(message.chat.id, config.msg_word, reply_markup=markup, parse_mode="HTML")
        # msg = bot.send_voice(message.chat.id, audio.download_or_get_audio(config.en_word), None)

        # msg = bot.send_voice(message.chat.id, f, None)
        # 
        config.callback = telebot.types.CallbackQuery(message.message_id, message.chat.id, config.en_word, message.chat.id)
    else:
        config.row_repeat_word = config.select_row_from_users_wordlist()
    
# @bot.message_handler(func=lambda message: message.text == "/repeat")
@bot.message_handler(commands=['repeat'])
def handle_repeat(message):
    bot.send_message(message.chat.id, 'Давай повторим слова! \U0001F393 \nВыбери правильный ответ с клавиатуры \U00002705 \nИли напиши сам \U0000270F Старайся! \U0001F4AA ')
    config.row_repeat_word = config.select_row_from_users_wordlist()
    # вот тут написать код проверки нажатой кнопки. см.выше
    new_en_word_send_for_repeat(message)

@bot.message_handler(commands=['next'])
def next_word_repeat(message):
    config.count_repeat += 1
    print('next_word_repeat : config.count_repeat', config.count_repeat)
    new_en_word_send_for_repeat(message)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_repeat_words(message):
    if config.callback:
        print('config.callback.data', config.callback.data)
        print('message.text',message.text)
        if config.callback.data == message.text:
            # выполняется если слово угаданно
            bot.send_message(message.chat.id, 'Правильно! \U0000263A')
            config.count_repeat += 1
            new_en_word_send_for_repeat(message)
        else:
            # выполняется если слово неугаданно
            bot.send_message(message.chat.id, "Ты не угадал! \U0000274C")
            config.row_repeat_word[config.count_repeat]
            markup = telebot.types.ReplyKeyboardMarkup(True, True)
            config.word_id = config.row_repeat_word[config.count_repeat][0]
            config.en_word = config.row_repeat_word[config.count_repeat][1]
            config.ru_word = config.row_repeat_word[config.count_repeat][2]
            config.msg_word = "<b>" + config.en_word.upper() + "</b> - " + config.ru_word + " "
            markup = telebot.types.ReplyKeyboardMarkup(True, True) # вот этой кнопки
            markup.row('/next')
            # for file in os.listdir('music/'):
            #     if file == "" + config.en_word.lower() + ".mp3":
            #         f = open('music/'+file, 'rb')
            bot.send_message(message.chat.id, config.msg_word, reply_markup=markup, parse_mode="HTML")
            # msg = bot.send_voice(message.chat.id, f, None)
            msg = bot.send_voice(message.chat.id, audio.download_or_get_audio(config.en_word), None)

    else:
        bot.send_message(message.chat.id, "Не пиши мне такое, я глупа и ничего не понимаю, кроме команд!")

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    print('\-\-\-\-\-\-\-\-\-\-\-\-\--\-\-\-\-\-\-\-\-\-\-', config.select_from_row(1))
    print('------------records------------', config.connect_to_db())
    for file in os.listdir('music/'):
        if file == config.en_word + "ogg":
            print("123443212232243223213212312312321321321312", file)
        if file.split('.')[-1] == 'ogg':
            print('file',file)
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        # time.sleep(3)


if __name__ == '__main__':
    bot.polling(none_stop=True)
    # utils.count_rows()
    # random.seed()
    # connect_to_db()



