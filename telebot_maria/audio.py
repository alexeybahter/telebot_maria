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



# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('the', '[ðə:]','определенный артикль')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('and', '[ænd]','и; а, но')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('a', '[ə]','неопределенный артикль')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('to', '[tu:]','к, в, на, до, для')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('was', '[wɔz]','был, была, было;')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('I', '[ʌi]','я')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('is', '[iz]','3- е л. ед. ч. наст. врем. гл. to be')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('of', '[ɔv]','из, от, о, об')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('that', '[ðæt]','тот, та, то')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('you', '[ju:]','ты, вы')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('he', '[hi:]','он')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('it', '[it]','он, она, оно; это')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('in', '[in]','в')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('his', '[hiz]','его')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('had', '[hæd]','имел, получал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('do', '[du:]','делать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('with', '[wið]','с, вместе с')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('not', '[nɔt]','не, нет; ни')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('her', '[hз:]','её')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('for', '[fɔ:]','в течение, на, для')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('on', '[ɔn]','на')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('at', '[æt]','около, у; в, на')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('but', '[bʌt]','только, лишь, кроме, но, а')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('she', '[ʃi:]','она')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('him', '[him]','его')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('as', '[æz]','как, когда')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('are', '[a:(r)]','мн. ч. наст. врем. гл. to be')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('said', '[sed]','говорил, сказал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('they', '[ðei]','они')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('we', '[wi:]','мы')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('all', '[ɔ:l]','все, вся, всё')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('this', '[ðis]','этот, эта, это')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('have', '[hæv]','иметь; получать; быть должным')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('there', '[ðɛə]','там, туда, здесь')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('what', '[(h)wɔt]','что')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('out', '[aut]','вне, снаружи; за')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('up', '[ʌp]','наверх(у), выше; вверх по, вдоль по')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('one', '[wʌn]','один')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('from', '[frɔm]','от, из, с')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('me', '[mi:]','мне, меня')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('go', '[gəu]','идти, ехать ; уходить')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('were', '[wз:]','были')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('would', '[wud]', '1) вспом. глагол.; 2) модальный глагол')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('like', '[laik]','похожий; как, подобно; любить, нравиться')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('when', '[(h)wen]','когда')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('could', '[kud]','мог, умел')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('then', '[ðen]','тогда; затем')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('be', '[bi:]','быть, существовать; находиться')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('them', '[ðem]','их , им')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('did', '[did]','делал, выполнял')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('been', '[bi:n]','был, была, было')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('now', '[nau]','теперь, сейчас')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('look', '[luk]','взгляд, смотреть')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('back', '[bæk]','спина, задний')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('my', '[mai]','мой')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('no', '[nəu]','нет, не')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('your', '[jɔ:]','твой, ваш')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('which', '[(h)witʃ]','который; что')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('about', "[ə'baut]",'кругом, вокруг; около; о, об, относительно')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('time', '[taim] время; раз')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('down', '[daun] вниз, внизу; вниз по, вдоль по')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('into', "['intu:]",'в')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('who', '[hu:]','кто; который')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('can', '[kæn]','мочь; уметь')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('know', '[nəu]','знать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('if', '[if]','если')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('just', '[dʒʌst]','только что')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('their', '[ðɛə]','их')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('get', '[get]','получать; брать; приобретать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('over', "['əuvə]",'над; свыше')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('more', '[mɔ:]','больше, более')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('some', '[sʌm]','несколько')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('man', '[mæn]','человек, мужчина')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('come', '[kʌm]','приходить, приезжать; случаться')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('an', '[æn]','неопределённый артикль')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('so', '[səu]','так; тоже, также')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('other', "['ʌðə]",'другой, иной, еще')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('little', "['litl]",'маленький')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('see', '[si:]','видеть')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('here', '[hiə]','здесь, тут')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('thing', '[θiŋ]','вещь, предмет')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('hand', '[hænd]','рука')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('by', '[bai]','у , около')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('will', '[wil]','1) вспом. гл. будущ. врем.; 2) модальный глагол')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('way', '[wei]','путь, дорога')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('again', "[ə'gein]",'опять, снова')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('right', '[rait]','правый; верно')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('only', "['əunli]",'только')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('am', '[æm]','1-е л. ед.ч. наст. врем. гл. to be')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('how', '[hau]','как')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('think', '[θiŋk]','думать; считать, полагать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('or', '[ɔ:]','или')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('got', '[gɔt]','получил')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('good', '[gud]','хороший; добро')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('eye', '[ai]','глаз; взгляд')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('well', '[wel]','хорошо')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('thought', '[θɔ:t]','думал, мысль')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('day', '[dei]','день; сутки')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('two', '[tu:]','два')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('than', '[ðæn]','чем, нежели')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('before', "[bi'fɔ:]",'перед; раньше')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('where', '[(h)wɛə]','где; куда')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('very', "['veri]",'очень')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('say', '[sei]','говорить, сказать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('came', '[keim]','приходил, приезжал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('any', "['eni]",'какой-нибудь')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('old', '[əuld]','старый')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('still', '[stil]','тихий; все еще')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('after', "['a:ftə]",'после, через; потом')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('off', '[ɔv]','с , от')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('has', '[hæz]','имел, имела')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('never', "['nevə]",'никогда')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('going', "['gəiŋ]",'живущий, существующий, ходьба')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('even', "['i:v(ə)n]",'даже; ровно')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('much', '[mʌtʃ]','много')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('went', '[went]','шёл, ехал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('too', '[tu:]','также; слишком')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('away', "[ə'wei]",'далеко; прочь')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('something', "['sʌmθiŋ]",'что-то, что-нибудь; примерно')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('first', '[fз:st]','первый; сначала')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('make', '[meik]','делать, производить; совершать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('head', '[hed]','голова')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('want', '[wɔnt]','хотеть')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('turn', '[tз:n]','поворачивать(ся)')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('face', '[feis]','лицо')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('made', '[meid]','сделан, сделанный')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('seem', '[si:m]','казаться')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('call', '[kɔ:l]','призыв; звать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('ask', '[a:sk]','спрашивать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('should', '[ʃud]','1) вспом. глагол; 2) должен, следует')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('through', '[θru:]','через , сквозь')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('long', '[lɔŋ]','длинный; долго')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('let', '[let]','позволять')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('take', '[teik]','брать; доставлять; принимать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('saw', '[sɔ:]','видел, пила')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('around', "[ə'raund]",'кругом, вокруг; поблизости')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('our', "['auə]",'наш')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('door', '[dɔ:]','дверь')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('last', '[la:st]','последний')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('tell', '[tel]','говорить')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('might', '[mait]','мог, мог бы, энергия')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('own', '[əun]','свой; владеть')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('night', '[nait]','ночь; вечер')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('year', '[jiə]','год')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('must', '[mʌst]','должен, обязан')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('because', '[bi:kɔz]','потому что')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('voice', '[vɔis]','голос')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('such', '[sʌtʃ]','такой, тот, подобный')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('room', '[ru:m]','комната')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('place', '[pleis]','место; помещать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('those', '[ðəuz]','те')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('work', '[wз:k]','работа; работать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('put', '[put]','положить')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('bill', '[bil]','счёт, законопроект, клюв')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('nothing', "['nʌθiŋ]",'ничего')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('most', '[məust]','самый большой, наибольший')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('house', '[haus]','дом')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('why', '[(h)wai]','почему')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('may', '[mei]','май')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('side', '[said]','сторона')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('great', '[greit]','большой, великий')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('these', '[ði:z]','эти')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('white', '[(h)wait]','белый')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('people', "['pi:pl]",'люди, нация, народ')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('upon', "[ə'pɔn]",'на')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('left', '[left]','левый, налево, покинул, уехал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('open', "['əup(ə)n]",'открывать(ся)')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('himself', "[him'self]",'себя; сам')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('friend', '[frend]','друг')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('felt', '[felt]','чувствовал, войлок')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('three', '[θri:]','три')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('knew', '[nju:]','знал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('another', "[ə'nʌðə]",'другой')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('once', '[wʌn(t)s]','один раз, однажды, когда-то')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('give', '[giv]','давать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('almost', "['ɔ:lməust]",'почти')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('mind', '[maind]','разум; мнение')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('took', '[tuk]','брал, хватал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('light', '[lait]','свет; освещать(ся)')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('yes', '[jes]','да')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('love', '[lʌv]','любовь, любить')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('end', '[end]','конец; кончать(ся)')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('boy', '[bɔi]','мальчик, парень')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('looking', "['lukiŋ]",'смотреть')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('while', '[(h)wail]','в то время как')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('sound', '[saund]','звук; звучать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('moment', "['məumənt]",'миг, момент')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('men', '[men]','люди, мужчины')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('ever', "['evə]",'когда-либо')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('under', "['ʌndə]",'под; ниже')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('told', '[təuld]','говорил, рассказывал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('really', "['riəli]",'действительно')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('life', '[laif]','жизнь')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('world', '[wз:ld]','мир, свет; вселенная')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('same', '[seim]','тот же самый')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('sure', '[ʃuə]','уверенный; конечно')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('new', '[nju:]','новый')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('found', '[faund]','находил, встречал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('being', "['bi:iŋ]",'жизнь, существование')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('enough', "[i'nʌf]",'достаточно')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('gone', '[gɔn]','ушли, ушёл, ушедший')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('many', "['meni]",'много, многие')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('big', '[big]','большой')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('does', '[dʌz]','3-е л. ед. наст. времени от do')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('every', "['evri]",'каждый, всякий')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('began', "[bi'gæn]",'начинал, начиналось')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('always', "['ɔ:lweiz]",'всегда')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('girl', '[gз:l]','девочка, девушка')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('home', '[həum]','дом')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('without', "[wi'ðaut]",'без, в отсутствие')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('heard', '[h:зd]','слышал, услышал')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('toward',"[tə'wɔ:dz] ",'к')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('need', '[ni:d]','нуждаться')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('stop', '[stɔp]','остановка; останавливать(ся)')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('maybe', "['meibi]",'может быть')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('part', '[pa:t]','доля, часть, отчасти')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('use', '[ju:z]','применение, польза; употреблять')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('okay', "[əu'kei]",'хорошо!, ладно!, есть!')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('use', '[ju:z]','использовать, применять')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('though', '[ðəu]','хотя, даже, тем не менее')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('far', '[fa:]','дальний; далеко')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('name', '[neim]','имя; название')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('word', '[wз:d]','слово')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('behind', "[bi'haind]",'за; сзади , позади')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('try', '[trai]','пытаться, пробовать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('help', '[help]','помощь; помогать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('also', "['ɔ:lsəu]",'тоже, также')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('better', "['betə]",'лучший, наилучший')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('mean', '[mi:n]','середина; значить; подразумевать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('father', "['fa:ðə]",'отец')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('against', "[ə'gen(t)st]",'против')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('anything', "['eniθiŋ]",'что-нибудь; что угодно')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('start', '[sta:t]','начало; начинать(ся)')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('yet', '[jet]','ещё, всё ещё')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('walk', '[wɔ:k]','ходьба; ходить')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('woman', "['wumən]",'женщина')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('seen', '[si:n]','видел')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('close', '[kləuz]','близкий, тесный; близко; закрывать(ся)')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('remember', "[ri'membə]",'помнить, вспоминать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('car', '[ka:]','автомобиль, машина')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('between', "[bi'twi:n]",'между')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('until', "[(ə)n'til]",'до, (до тех пор) пока (не)')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('both', '[bəuθ]','оба')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('done', '[dʌn]','сделанный; выполненный')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('god', '[gɔd]','бог')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('find', '[faind]','находить, обнаруживать')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('water', "['wɔ:tə]",'вода')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('arm', '[a:m]','рука')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('few', '[fju:]','немного; a ~ несколько')
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('hear', '[hiə]','слышать; слушать')

# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('the', '[ðə:]','определенный артикль');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('and', '[ænd]','и; а, но');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('a', '[ə]','неопределенный артикль');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('to', '[tu:]','к, в, на, до, для');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('was', '[wɔz]','был, была, было;');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('I', '[ʌi]','я');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('is', '[iz]','3- е л. ед. ч. наст. врем. гл. to be');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('of', '[ɔv]','из, от, о, об');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('that', '[ðæt]','тот, та, то');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('you', '[ju:]','ты, вы');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('he', '[hi:]','он');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('it', '[it]','он, она, оно; это');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('in', '[in]','в');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('his', '[hiz]','его');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('had', '[hæd]','имел, получал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('do', '[du:]','делать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('with', '[wið]','с, вместе с');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('not', '[nɔt]','не, нет; ни');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('her', '[hз:]','её');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('for', '[fɔ:]','в течение, на, для');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('on', '[ɔn]','на');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('at', '[æt]','около, у; в, на');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('but', '[bʌt]','только, лишь, кроме, но, а');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('she', '[ʃi:]','она');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('him', '[him]','его');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('as', '[æz]','как, когда');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('are', '[a:(r)]','мн. ч. наст. врем. гл. to be');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('said', '[sed]','говорил, сказал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('they', '[ðei]','они');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('we', '[wi:]','мы');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('all', '[ɔ:l]','все, вся, всё');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('this', '[ðis]','этот, эта, это');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('have', '[hæv]','иметь; получать; быть должным');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('there', '[ðɛə]','там, туда, здесь');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('what', '[(h)wɔt]','что');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('out', '[aut]','вне, снаружи; за');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('up', '[ʌp]','наверх(у), выше; вверх по, вдоль по');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('one', '[wʌn]','один');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('from', '[frɔm]','от, из, с');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('me', '[mi:]','мне, меня');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('go', '[gəu]','идти, ехать ; уходить');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('were', '[wз:]','были');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('would', '[wud]', '1) вспом. глагол.; 2) модальный глагол');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('like', '[laik]','похожий; как, подобно; любить, нравиться');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('when', '[(h)wen]','когда');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('could', '[kud]','мог, умел');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('then', '[ðen]','тогда; затем');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('be', '[bi:]','быть, существовать; находиться');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('them', '[ðem]','их , им');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('did', '[did]','делал, выполнял');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('been', '[bi:n]','был, была, было');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('now', '[nau]','теперь, сейчас');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('look', '[luk]','взгляд, смотреть');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('back', '[bæk]','спина, задний');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('my', '[mai]','мой');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('no', '[nəu]','нет, не');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('your', '[jɔ:]','твой, ваш');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('which', '[(h)witʃ]','который; что');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('about', '[ə''baut]','кругом, вокруг; около; о, об, относительно');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('time', '[taim] время; раз');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('down', '[daun] вниз, внизу; вниз по, вдоль по');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('into', '[''intu:]','в');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('who', '[hu:]','кто; который');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('can', '[kæn]','мочь; уметь');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('know', '[nəu]','знать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('if', '[if]','если');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('just', '[dʒʌst]','только что');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('their', '[ðɛə]','их');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('get', '[get]','получать; брать; приобретать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('over', '[''əuvə]','над; свыше');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('more', '[mɔ:]','больше, более');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('some', '[sʌm]','несколько');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('man', '[mæn]','человек, мужчина');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('come', '[kʌm]','приходить, приезжать; случаться');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('an', '[æn]','неопределённый артикль');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('so', '[səu]','так; тоже, также');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('other', '[''ʌðə]','другой, иной, еще');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('little', '[''litl]','маленький');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('see', '[si:]','видеть');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('here', '[hiə]','здесь, тут');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('thing', '[θiŋ]','вещь, предмет');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('hand', '[hænd]','рука');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('by', '[bai]','у , около');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('will', '[wil]','1) вспом. гл. будущ. врем.; 2) модальный глагол');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('way', '[wei]','путь, дорога');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('again', '[ə''gein]','опять, снова');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('right', '[rait]','правый; верно');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('only', '[''əunli]','только');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('am', '[æm]','1-е л. ед.ч. наст. врем. гл. to be');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('how', '[hau]','как');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('think', '[θiŋk]','думать; считать, полагать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('or', '[ɔ:]','или');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('got', '[gɔt]','получил');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('good', '[gud]','хороший; добро');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('eye', '[ai]','глаз; взгляд');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('well', '[wel]','хорошо');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('thought', '[θɔ:t]','думал, мысль');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('day', '[dei]','день; сутки');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('two', '[tu:]','два');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('than', '[ðæn]','чем, нежели');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('before', '[bi''fɔ:]','перед; раньше');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('where', '[(h)wɛə]','где; куда');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('very', '[''veri]','очень');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('say', '[sei]','говорить, сказать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('came', '[keim]','приходил, приезжал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('any', '[''eni]','какой-нибудь');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('old', '[əuld]','старый');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('still', '[stil]','тихий; все еще');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('after', '[''a:ftə]','после, через; потом');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('off', '[ɔv]','с , от');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('has', '[hæz]','имел, имела');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('never', '[''nevə]','никогда');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('going', '[''gəiŋ]','живущий, существующий, ходьба');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('even', '[''i:v(ə)n]','даже; ровно');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('much', '[mʌtʃ]','много');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('went', '[went]','шёл, ехал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('too', '[tu:]','также; слишком');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('away', '[ə''wei]','далеко; прочь');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('something', '[''sʌmθiŋ]','что-то, что-нибудь; примерно');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('first', '[fз:st]','первый; сначала');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('make', '[meik]','делать, производить; совершать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('head', '[hed]','голова');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('want', '[wɔnt]','хотеть');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('turn', '[tз:n]','поворачивать(ся)');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('face', '[feis]','лицо');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('made', '[meid]','сделан, сделанный');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('seem', '[si:m]','казаться');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('call', '[kɔ:l]','призыв; звать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('ask', '[a:sk]','спрашивать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('should', '[ʃud]','1) вспом. глагол; 2) должен, следует');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('through', '[θru:]','через , сквозь');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('long', '[lɔŋ]','длинный; долго');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('let', '[let]','позволять');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('take', '[teik]','брать; доставлять; принимать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('saw', '[sɔ:]','видел, пила');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('around', '[ə''raund]','кругом, вокруг; поблизости');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('our', '[''auə]','наш');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('door', '[dɔ:]','дверь');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('last', '[la:st]','последний');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('tell', '[tel]','говорить');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('might', '[mait]','мог, мог бы, энергия');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('own', '[əun]','свой; владеть');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('night', '[nait]','ночь; вечер');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('year', '[jiə]','год');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('must', '[mʌst]','должен, обязан');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('because', '[bi:kɔz]','потому что');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('voice', '[vɔis]','голос');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('such', '[sʌtʃ]','такой, тот, подобный');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('room', '[ru:m]','комната');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('place', '[pleis]','место; помещать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('those', '[ðəuz]','те');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('work', '[wз:k]','работа; работать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('put', '[put]','положить');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('bill', '[bil]','счёт, законопроект, клюв');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('nothing', '[''nʌθiŋ]','ничего');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('most', '[məust]','самый большой, наибольший');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('house', '[haus]','дом');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('why', '[(h)wai]','почему');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('may', '[mei]','май');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('side', '[said]','сторона');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('great', '[greit]','большой, великий');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('these', '[ði:z]','эти');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('white', '[(h)wait]','белый');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('people', '[''pi:pl]','люди, нация, народ');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('upon', '[ə''pɔn]','на');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('left', '[left]','левый, налево, покинул, уехал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('open', '[''əup(ə)n]','открывать(ся)');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('himself', '[him''self]','себя; сам');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('friend', '[frend]','друг');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('felt', '[felt]','чувствовал, войлок');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('three', '[θri:]','три');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('knew', '[nju:]','знал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('another', '[ə''nʌðə]','другой');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('once', '[wʌn(t)s]','один раз, однажды, когда-то');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('give', '[giv]','давать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('almost', '[''ɔ:lməust]','почти');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('mind', '[maind]','разум; мнение');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('took', '[tuk]','брал, хватал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('light', '[lait]','свет; освещать(ся)');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('yes', '[jes]','да');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('love', '[lʌv]','любовь, любить');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('end', '[end]','конец; кончать(ся)');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('boy', '[bɔi]','мальчик, парень');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('looking', '[''lukiŋ]','смотреть');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('while', '[(h)wail]','в то время как');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('sound', '[saund]','звук; звучать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('moment', '[''məumənt]','миг, момент');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('men', '[men]','люди, мужчины');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('ever', '[''evə]','когда-либо');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('under', '[''ʌndə]','под; ниже');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('told', '[təuld]','говорил, рассказывал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('really', '[''riəli]','действительно');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('life', '[laif]','жизнь');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('world', '[wз:ld]','мир, свет; вселенная');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('same', '[seim]','тот же самый');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('sure', '[ʃuə]','уверенный; конечно');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('new', '[nju:]','новый');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('found', '[faund]','находил, встречал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('being', '[''bi:iŋ]','жизнь, существование');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('enough', '[i''nʌf]','достаточно');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('gone', '[gɔn]','ушли, ушёл, ушедший');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('many', '[''meni]','много, многие');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('big', '[big]','большой');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('does', '[dʌz]','3-е л. ед. наст. времени от do');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('every', '[''evri]','каждый, всякий');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('began', '[bi''gæn]','начинал, начиналось');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('always', '[''ɔ:lweiz]','всегда');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('girl', '[gз:l]','девочка, девушка');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('home', '[həum]','дом');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('without', '[wi''ðaut]','без, в отсутствие');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('heard', '[h:зd]','слышал, услышал');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('toward','[tə''wɔ:dz]','к');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('need', '[ni:d]','нуждаться');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('stop', '[stɔp]','остановка; останавливать(ся)');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('maybe', '[''meibi]','может быть');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('part', '[pa:t]','доля, часть, отчасти');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('use', '[ju:z]','применение, польза; употреблять');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('okay', '[əu''kei]','хорошо!, ладно!, есть!');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('use', '[ju:z]','использовать, применять');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('though', '[ðəu]','хотя, даже, тем не менее');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('far', '[fa:]','дальний; далеко');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('name', '[neim]','имя; название');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('word', '[wз:d]','слово');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('behind', '[bi''haind]','за; сзади , позади');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('try', '[trai]','пытаться, пробовать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('help', '[help]','помощь; помогать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('also', '[''ɔ:lsəu]','тоже, также');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('better', '[''betə]','лучший, наилучший');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('mean', '[mi:n]','середина; значить; подразумевать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('father', '[''fa:ðə]','отец');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('against', '[ə''gen(t)st]','против');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('anything', '[''eniθiŋ]','что-нибудь; что угодно');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('start', '[sta:t]','начало; начинать(ся)');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('yet', '[jet]','ещё, всё ещё');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('walk', '[wɔ:k]','ходьба; ходить');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('woman', '[''wumən]','женщина');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('seen', '[si:n]','видел');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('close', '[kləuz]','близкий, тесный; близко; закрывать(ся)');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('remember', '[ri''membə]','помнить, вспоминать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('car', '[ka:]','автомобиль, машина');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('between', '[bi''twi:n]','между');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('until', '[(ə)n''til]','до, (до тех пор) пока (не)');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('both', '[bəuθ]','оба');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('done', '[dʌn]','сделанный; выполненный');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('god', '[gɔd]','бог');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('find', '[faind]','находить, обнаруживать');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('water', '[''wɔ:tə]','вода');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('arm', '[a:m]','рука');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('few', '[fju:]','немного; a ~ несколько');
# INSERT INTO public.wordlist( en_word, transcription, ru_word) VALUES ('hear', '[hiə]','слышать; слушать');

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