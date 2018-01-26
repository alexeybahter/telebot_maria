from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import time

# re = '''<p class="ex_t human"> Стэнли, подойди и поздоровайся со своим племянником.<a href="/sentence/update/14872923706" class="no_mobile link_edit" onclick="return openWindow(this.href, 660, 860)">&ensp;&#9776;</a> </p> <p class="ex_o"> Every morning they exchanged polite hellos.<span class="plus" onClick="addItemToEdu({sentence_id:266195, word_id:16798})">&ensp;<img id="pi_266195" src="/images/pi_v3.gif"></span> </p>'''
# r = requests.get('http://wooordhunt.ru/word/hello')
# soup = BeautifulSoup(r.text, 'html.parser')
# x = soup.find('span', class_="transcription").string

words_en = '''begin.appear.late.continue.take.put off.finish.end.stop.cease'''
words_ru = '''начинать(ся) появляться опаздывать продолжать(ся) занимать(время) откладывать завершать(ся) завершать(ся) прекращать переставать'''
category = 'Глагол стадии'


array_words_en = words_en.split(".")
array_words_ru = words_ru.split(" ")
print(array_words_en)
array_transcription = []
array_description = []
path_audio = ''
t1 = time.time()
for word in array_words_en:
    r = requests.get('http://wooordhunt.ru/word/' + word.lower())
    filename = '/Users/alexey/Documents/bot/music/' + word.lower() + '.mp3'
    if len(word.split(' ')) == 2:
        arr_with_2_words = word.split(' ')
        dash = '-'
        path_audio = arr_with_2_words[0] + dash + arr_with_2_words[1]
        print("12345675432134567890-987654321345678908765432", path_audio)
        url = "http://wooordhunt.ru/data/sound/word/uk/mp3/" + path_audio + ".mp3"
    else:
        path_audio = word.lower()
        url = "http://wooordhunt.ru/data/sound/word/uk/mp3/" + path_audio + ".mp3"
        print("12345675432134567890-987654321345678908765432", path_audio)
    
    x = urlretrieve(url, filename)
    print('xxxxx', url)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        transcription = soup.findAll('div', id="uk_tr_sound")[0].find('span', class_="transcription").string
        print('transcription =', transcription)
    except IndexError:
        print("transcription --- None")
        continue

    # description = soup.findAll('div', class_='block')[1].findAll('p', class_='ex_o').string
    # description = soup.findAll('div', 'block')[1].prettify()
    together = []
    for i in range(0,4):
        # print(i)
        # print(word)
        # print('1212121212')
        # description_en = soup.findAll('div', 'block')[1].findAll('p', 'ex_o')[i].next
        try:
            description_en = soup.findAll('div', 'block')[2].findAll('p', 'ex_o')[i].next
            # print('------- '+word+' -------\n ', description_en)
            description_ru = soup.findAll('div', 'block')[2].findAll('p', 'ex_t')[i].next
        except IndexError:
            print("ERROR --- out of range")
            continue
        # print(' ',description_ru, end='\n')
        together.extend([description_en, description_ru])
    array_description.append(together)
    array_transcription.append(transcription)
    # array_description.append(description)
print("-------\n",array_description, end='\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        
for item in range(len(array_description)):
    word_el_en = array_words_en[item]
    description_el_ru = array_description[item]
    # print('\nword_el_ru =         [' + str(item) + ']', word_el_en)
    # print('\ndescription_el =    ', description_el_ru)
    # print('filename', filename)


# array_key_of_words = [0]
# array_key_of_descriptions = [0]
# for item_w in range(len(array_description)-1):
#     try:
#         if item_w == array_key_of_words[item_w]:
#             print('1$$$$$$$$', item_w)
#             # print('range(len(array_description)-1)', range(len(array_description)-1))
#             try:
#                 for item_d in range(4):
#                     print('2$$$$$$$$', item_w)
#                     print('$$$$$ for item in range(len(array_description)) - item_d', item_d)
#                     if not item_d == array_key_of_descriptions[item_d]:
#                         # array_description.extend([item_d])
#                         del array_description[item_d]
#                         # print('######',array_description[item_d])
#             except IndexError:
#                 # print('######',item_d)
#                 print('if', item_d == array_key_of_descriptions[item_d])
#                 if not item_d == array_key_of_descriptions[item_d]:
#                         # array_description.extend([item_d])
#                         del array_description[item_d]
#                         print('######',array_description[item_d])
#                 continue
#     except IndexError:
#         break
# print('8888888888888888888', array_description)

t2 = time.time()
t = t2 - t1
# print("--------------\n",t1)
# print("--------------\n",t2)
length =len(array_words_en) 
print("length", length)
print("------time--------\n",t)
# x = r.text
# print(x)
f = open('test.txt', 'w')
str_SQL = '\n--------------------------------------------------------  %s\n' % (category)
for item in range(length):
    try:
        word_el_en = array_words_en[item]
        # path_audio = array_words_en[item].lower() + '.mp3'
        word_el_ru = array_words_ru[item]
        transcription_el = array_transcription[item]
        description_el_ru = array_description[item]
        description_el_en = array_description[item]
    except IndexError:
        continue
    print('---------------'+str(item)+'---------------\nword_el_en =         ', word_el_en)
    print('word_el_ru =         ', word_el_ru)
    print('path_audio =         ', path_audio)
    print('transcription_el =  ', transcription_el)
    print('description_el_56 =    ', description_el_ru)
    for desc in array_description[item]:
        print('description_el =    ', desc)
    str_SQL += '''
                INSERT INTO public.wordlist( en_word, transcription, ru_word, path_audio, description, category) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');
              ''' % (word_el_en, transcription_el, word_el_ru, path_audio, description_el_ru, category)
f.write(str_SQL)
f.close()
print('------ str_SQL -----\n', str_SQL, end='\n---------------------\n')







