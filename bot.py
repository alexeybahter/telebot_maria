import config
import telebot
import psycopg2
import sys
import pprint
import os
import random
import utils
import audio
from random import randint
# import request
# from flask import Flask, request
from random import shuffle

# WEBHOOK_HOST = 'IP'
# WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
# WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

# WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
# WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу

# WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# WEBHOOK_URL_PATH = "/%s/" % (config.token)

bot = telebot.TeleBot(config.token)

# base_url = 'https://api.telegram.org/bot' + config.token + '/'
# data = {"url": ""}
# requests.post(base_url + 'setWebhook', data=data)

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
    row = config.select_row_from_wordlist(message.chat.id)
    print('------row = ', row)
    print('lenght_row',len(row))
    for word in row:
        config.word_id = word[0]
        config.en_word = word[1]
        config.ru_word = word[2]
        config.path_audio = word[3]
        config.transcription = word[4]
        print('config.word_id', config.word_id)
        print('config.en_word', config.en_word)
        print('config.path_audio', config.path_audio)
        print('config.transcription', config.transcription)
        config.msg_word = "<b>" + config.en_word.upper() + "</b> - " + config.transcription + " - <i>" + config.ru_word + "</i>"
        print('---\n', config.msg_word, end='----\n')
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row('/learn', '/know')
    bot.send_message(message.chat.id, config.msg_word, reply_markup=markup, parse_mode="HTML")
    print('audio.file', audio.file)
    msg = bot.send_voice(message.chat.id, audio.download_or_get_audio(config.en_word), None)

# говорим что данное слово уже знаем
@bot.message_handler(commands=['learn'])
def handle_learn_word(message):
    print("@bot.message_handler(commands=['learn']) config.word_id", config.word_id)
    config.learn_word(config.word_id, message.chat.id)
    config.count_learn += 1
    # callback = telebot.types.CallbackQuery(config.count, message.chat.id, config.count, message.chat.id)
    if config.count_learn != 5:
        print('config.count', config.count)
        # print("callback", callback)
        handle_learning(message)
    else:
        config.count_learn = 0
        # callback = ''
        # bot.send_message(message.chat.id, "Ты узнал 10 новых слов, пора их повторить!")
        markup = telebot.types.ReplyKeyboardMarkup(True, True)
        markup.row('/learning', '/repeat')
        bot.send_message(message.chat.id, "Ты узнал 5 новых слов, пора их повторить!", reply_markup=markup)
    # bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
# def check_repeat_words(word, click_word):

@bot.message_handler(commands=['know'])
def handle_know_word(message):
    config.set_know_word(config.word_id, message.chat.id)
    print("Я уже знаю это слово, дай мне другое!")
    bot.send_message(message.chat.id, "Я рада что ты уже знаешь это слово! Давай попробуем другое")
    handle_learn_word(message)

# заходим в режим повторения слов
# @bot.message_handler(func=lambda message: message.text == "/repeat")
@bot.message_handler(commands=['repeat'])
def handle_repeat(message):
    bot.send_message(message.chat.id, 'Давай повторим слова! \U0001F393 \nВыбери правильный ответ с клавиатуры \U00002705 \nИли напиши сам \U0000270F Старайся! \U0001F4AA ')
    config.row_repeat_word = config.select_row_from_users_wordlist(message.chat.id)
    # print('len before',len(config.row_repeat_word))
    print('arr before = ', config.row_repeat_word)
    random.shuffle(config.row_repeat_word)
    # config.row_repeat_word.extend([config.row_repeat_word[1], config.row_repeat_word[2], config.row_repeat_word[0]])
    print('-------\narr before =', config.row_repeat_word)
    print('len\n',len(config.row_repeat_word))
    new_en_word_send_for_repeat(message)

def rand(start, stop, count):
    gamma = []
    for i in range(count):
        while True:
            item = randint(start, stop)
            if not gamma.count(item):
                gamma.append(item)
                yield item
                break

# отправляет одно слово на повторение и показывает клавиатуру выбора правильного слова
def new_en_word_send_for_repeat(message):
    print('---------------------\n', len(config.row_repeat_word) > config.count_repeat)
    if len(config.row_repeat_word) > config.count_repeat:
        # markup = telebot.types.ReplyKeyboardMarkup(True, True)
        # print('row__select_row_from_users_wordlist', config.row_repeat_word)
        # random.shuffle(config.row_repeat_word)
        # print('-------------------------shuffle\nconfig.row_repeat_word', config.row_repeat_word)
        words_length = len(config.row_repeat_word)
        # if words_length != 10:
            # bot.send_message(message.chat.id, "Тебе нечего повторять. Изучи первые 10 слов.")
        # print('len = ', words_length)
        # print('config.count_repeat', config.count_repeat)
        # print('config.row_repeat_word[config.count_repeat]', config.row_repeat_word[config.count_repeat][1])
        for item in config.row_repeat_word:
            print('item = ', item[1])
        # if len(config.row_repeat_word) != len(config.row_repeat_word) + 3:
        #     config.row_repeat_word.extend([config.row_repeat_word[1], config.row_repeat_word[2], config.row_repeat_word[0]])
        #     print("xxxxxx", len(config.row_repeat_word))
        config.word_id = config.row_repeat_word[config.count_repeat][0]
        config.en_word = config.row_repeat_word[config.count_repeat][1]
        config.ru_word = config.row_repeat_word[config.count_repeat][2]
        print('--\nconfig.word_id', config.word_id)
        print('config.en_word', config.en_word)
        print('config.ru_word', config.ru_word + '\n--')
        config.msg_word =  "<b> " + config.ru_word.title() + "</b>"
        markup = telebot.types.ReplyKeyboardMarkup(True, True)
        # correct_answer = config.row_repeat_word.pop(config.count_repeat)
        # print('after correct_answer =', config.row_repeat_word)

        # print('correct_answer', correct_answer)
        list_answer = [config.en_word.title()]
        # numbers = []
        # даже не спрашивай как это работает (%_%)
        for number in rand(0, len(config.row_repeat_word) - 1, 4):
            # numbers.apend(number)
            print('NUMBER =',number)
            # print('LEN_RAND = ', len(config.row_repeat_word))
            print('x_rand', config.row_repeat_word[number][1].title())
            if not config.row_repeat_word[number][1].title() == config.en_word.title() and len(list_answer) <= 3:
                list_answer.append(config.row_repeat_word[number][1].title())
            else:
                continue
                # while True:
                #     for number in rand(0, len(config.row_repeat_word) - 1, 1):

        # list_answer = []
        # config.row_repeat_word[random.randrange(0, len(config.row_repeat_word), 1)][1]
        # config.row_repeat_word[random.randrange(0, len(config.row_repeat_word), 1)][1]
        # config.row_repeat_word[random.randrange(0, len(config.row_repeat_word), 1)][1]
        # print('random',random.randrange(0, len(config.row_repeat_word), 1))
        # print('random',random.randrange(0, len(config.row_repeat_word), 1))
        # print('random',random.randrange(0, len(config.row_repeat_word), 1))
        # print('random',random.randrange(0, len(config.row_repeat_word), 1))
        # print('random',random.randrange(0, len(config.row_repeat_word), 1))
        # print('random',random.randrange(0, len(config.row_repeat_word), 1))

        # for word in config.row_repeat_word[config.count_repeat:config.count_repeat + 3]:
            # print('word', word[1])
            # list_answer.append(word[1].title())
        print('list_answer',list_answer)
        shuffle(list_answer)
        for item in list_answer:
            markup.row(item)
        bot.send_message(message.chat.id, config.msg_word, reply_markup=markup, parse_mode="HTML")
        config.callback = telebot.types.CallbackQuery(message.message_id, message.chat.id, config.en_word, message.chat.id)
        print('----\nlen = ', words_length)
        print('config.count_repeat', config.count_repeat)
        # print('config.row_repeat_word[config.count_repeat]', config.row_repeat_word[config.count_repeat][1])
    else:
        # config.row_repeat_word = config.select_row_from_users_wordlist(message.chat.id)
        # bot.send_message(message.chat.id, "У тебя нет слов для повторения!")
        markup = telebot.types.ReplyKeyboardMarkup(True, True)
        markup.row('/learning')
        bot.send_message(message.chat.id, "У тебя нет слов для повторения!", reply_markup=markup)


# после неудачной попытки угадывания слова отправляем новое слово
@bot.message_handler(commands=['next'])
def next_word_repeat(message):
    config.count_repeat += 1
    print('-------------------------------')
    print('next_word_repeat : config.count_repeat', config.count_repeat)
    new_en_word_send_for_repeat(message)

# проверка слов в режиме повторения, также проверка лишних сообщений пользователя
@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_repeat_words(message):
    if config.callback:
        print('config.callback.data', config.callback.data)
        print('message.text',message.text)
        if config.callback.data.title() == message.text:
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
            markup = telebot.types.ReplyKeyboardMarkup(True, True)
            markup.row('/next')
            bot.send_message(message.chat.id, config.msg_word, reply_markup=markup, parse_mode="HTML")
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



