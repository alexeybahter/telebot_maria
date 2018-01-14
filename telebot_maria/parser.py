from pyparsing import *

url = 'https://oauth.vk.com/blank.html#access_token=f9cc1f917c3ba191cd4279be2749' \
      '4b6b5fba00e12ed71a6c790daf70ff9712cb8d195a875c7dea143f146&expires_in=86400&' \
      'user_id=91585260'
url1 = '''абсурдный
absurd
абсцесс, нарыв
abscess
август
August
автобус
bus
автомобиль
саг
администратор
receptionist
адрес
address
аккуратный
accurate
аллергия
allergy
анализ крови
blood test
анализ мочи
urine test
аппетит
appetite
апрель
April
аптека
pharmacy
ароматный
aromatic
аэровокзал
air-terminal
аэропорт
airport
бабушка
grandmother
багаж
luggage
'''

'абсурдный', 'absurd', 'audio', 'абсцесс, нарыв', 'abscess', 'audio', 'август', 'August', 'audio', 'автобус', 'bus', 'audio', 'автомобиль', 'саг', 'audio', 'администратор', 'receptionist', 'audio', 'адрес', 'address', 'audio', 'аккуратный', 'accurate', 'audio', 'аллергия', 'allergy', 'audio', 'анализ крови', 'blood test', 'audio', 'анализ мочи', 'urine test', 'audio', 'аппетит', 'appetite', 'audio', 'апрель', 'April', 'audio', 'аптека', 'pharmacy', 'audio', 'ароматный', 'aromatic', 'audio', 'аэровокзал', 'air-terminal', 'audio', 'аэропорт', 'airport', 'audio', 'бабушка', 'grandmother', 'audio', 'багаж', 'luggage', 'audio',);

params = url1.split('.')
for i in params:
	x = i.split('\n')
	x[]
	print(x)
print(params)
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