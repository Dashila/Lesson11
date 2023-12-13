def victorina():
import random

FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': "15.10.1814",
                 "Сегрей Александрович Есенин": "03.10.1895", "Владимир Семенович Высоцкий": "25,01,1938",
                 "Виктор Робертович Цой": "21.06.1962" }
rounds = int(input('Сколько раз вы хотите сыграть?:'))
for i in range (rounds):
name, date = random.choice(list(FAMOUS_PEOPLE.items()))
answer = input(f'огда родился {name}')
if answer == date:
    print('Верно')
else:
    print('неверно')
print("пока")
victorina()