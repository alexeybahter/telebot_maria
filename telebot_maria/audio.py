from urllib.request import urlretrieve
import os
import config

file = '' 

def download_or_get_audio(en_word):
    if not config.path_audio:
        print('if not config.path_audio')
        print('save_audio: word', en_word)
        filename = '/Users/alexey/Documents/bot/music/' + en_word + '.mp3'
        urlretrieve("http://api.voicerss.org/?key=fd9b853f3f3a414380dfd7f6d3935cfe"
            "&hl=en-us&c=wav&src="+ en_word + '', filename)
        print('filename', filename)
        config.add_path_audio(en_word)
        file = open('music/' + en_word + '.mp3', 'rb')
    else:
        # for file in os.listdir('music/'):
        #     print('music_file = ', file)
        #     if file.lower() == "" + config.en_word.lower() + ".wav":
        #         print("123443212232243223213212312312321321321312", file)
        file = open('music/' + en_word + '.mp3', 'rb')
        print("ffffffff",file)
        # msg = bot.send_voice(message.chat.id, f, None)
        # print("message.chat.id = ", message.chat.id)
    return file

    # print('save_audio: word', word)
    # filename = '/Users/alexey/Documents/bot/music/' + word.lower() + '.wav'
    # urlretrieve("http://api.voicerss.org/?key=fd9b853f3f3a414380dfd7f6d3935cfe"
    #         "&hl=en-us&c=wav&src="+ word + '', filename)
    # webbrowser.open(filename)






# from pyparsing import *

# url = 'https://oauth.vk.com/blank.html#access_token=f9cc1f917c3ba191cd4279be2749' \
#       '4b6b5fba00e12ed71a6c790daf70ff9712cb8d195a875c7dea143f146&expires_in=86400&' \
#       'user_id=91585260'
# url1 = '''абсурдный
# absurd
# абсцесс, нарыв
# abscess
# август
# August
# автобус
# bus
# автомобиль
# саг
# администратор
# receptionist
# адрес
# address
# аккуратный
# accurate
# аллергия
# allergy
# анализ крови
# blood test
# анализ мочи
# urine test
# аппетит
# appetite
# апрель
# April
# аптека
# pharmacy
# ароматный
# aromatic
# аэровокзал
# air-terminal
# аэропорт
# airport
# бабушка
# grandmother
# багаж
# luggage
# '''

# 'абсурдный', 'absurd', 'audio', 'абсцесс, нарыв', 'abscess', 'audio', 'август', 'August', 'audio', 'автобус', 'bus', 'audio', 'автомобиль', 'саг', 'audio', 'администратор', 'receptionist', 'audio', 'адрес', 'address', 'audio', 'аккуратный', 'accurate', 'audio', 'аллергия', 'allergy', 'audio', 'анализ крови', 'blood test', 'audio', 'анализ мочи', 'urine test', 'audio', 'аппетит', 'appetite', 'audio', 'апрель', 'April', 'audio', 'аптека', 'pharmacy', 'audio', 'ароматный', 'aromatic', 'audio', 'аэровокзал', 'air-terminal', 'audio', 'аэропорт', 'airport', 'audio', 'бабушка', 'grandmother', 'audio', 'багаж', 'luggage', 'audio',);

# params = url1.split('.')
# for i in params:
# 	words = i.split('\n')
# 	print(words)
# # print(x)
# print('--------------------------------------------------------')
# # print(words[1])
# numbers = []

# for x in range(0, 10, 3):
# 	numbers.append(x)
# print(numbers)
# i = 0
# for index, item in enumerate(words):
# 	index +=  3
# 	print(index)
# 	print(item)

# print('==========================================================')
# import urllib.request
# request = urllib.request.urlopen("https://translate.google.com/translate_tts?ie=UTF-8&tl=en-TR&client=tw-ob&q=fuck+you+asshole").read()
# print(request)
# ---------------
# import requests
# r = requests.get("https://translate.google.com/translate_tts?ie=UTF-8&tl=en-TR&client=tw-ob&q=fuck+you+asshole")
# # print(r.text)
# type_r = type(r.text)
# print('type_r', type_r)
# f = open('/Users/alexey/Documents/bot/audio1.mpeg', 'w')
# f.write(r.text)
# print('ffffffffffff',f)
# f.close()



# from yandex_translate import YandexTranslate
# translate = YandexTranslate('trnsl.1.1.20171227T201452Z.479e00e9cb5c9599.22a06790ae61b9222ad26f1c608fa1ccdcbf0144')
# print('Languages:', translate.langs)
# print('Translate directions:', translate.directions)
# print('Detect language:', translate.detect('Привет, мир!'))
# print('Translate:', translate.translate('Привет, мир!', 'ru-en'))	
# for word in words[numbers]:
	# print(word)
# names = ['tom', 'john', 'simon']
# namesCapitalized = [capitalize(n) for n in names]
# print(namesCapitalized)
# for i in params[::2]:
	# print(i)

# var = ''
# for i in params:
#     x = i.split('=')
#     print('xxxx', x)
    # token.update({x[0]: x[1]})

# print(token)

# number = Word(nums + ".")
# # var = Word(alphas)
# # var = Regex("[A-Z]")
# # line = number + var
# str = number.parseString('абсурдный', 'absurd', '2.', 'абсцесс, нарыв', 'abscess', '3.', 'август', 'August', '4.,' 'автобус', 'bus', '5.,' 'автомобиль', 'саг', '6.', 'администратор', 'receptionist', '7.', 'адрес', 'address', '8.', 'аккуратный', 'accurate', '9.', 'аллергия', 'allergy', '10.', 'анализ крови', 'blood test', '11.', 'анализ мочи', 'urine test', '12.', 'аппетит', 'appetite', '13.', 'апрель', 'April', '14.', 'аптека', 'pharmacy', '15.', 'ароматный', 'aromatic', '16.', 'аэровокзал', 'air-terminal', '17.', 'аэропорт', 'airport', '18.', 'бабушка', 'grandmother', '19.', 'багаж', 'luggage')
# # print("str = ", str)