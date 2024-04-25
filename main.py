#Все нужны библиотеки
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import random
import pandas as pd
import time

#Объявление картинок
our_fon = Image.open('Фон1.jpg')
tabl = Image.open('Табл.jpg')
tort1 = Image.open('Торт1.jpg')
tort2 = Image.open('Торт2.jpg')
tort3 = Image.open('Торт3.jpg')
podarok1 = Image.open('Подарок1.jpg')
podarok2 = Image.open('Подарок2.jpg')
podarok3 = Image.open('Подарок3.jpg')
font1 = ImageFont.truetype("comicz.ttf", 65)
font2 = ImageFont.truetype("ComicSansMS3.ttf", 27)
mask = [tort1, tort2, tort3, podarok1, podarok2, podarok3]

#Узнаём сегодняшнюю дату
today = date.today()
we_need = ''
Month = [" января", " февраля", " марта", " апреля", " мая", " июня", " июля", " августа", " сентября", " октября", " ноября", " декабря"]
day = str(today.day) + Month[today.month - 1]

#Читаем таблицу в массивы
xl = pd.read_excel('Table.xlsx')
name = xl['Имя'].tolist()
surname = xl['Фамилия'].tolist()
patronymic = xl['Отчество'].tolist()
durka = xl['Класс'].tolist()
Date = xl['Дата рождения'].tolist()
NormDate = []

for i in range(0, len(Date)):
    Date[i] = str(Date[i])

#ИДЕЙНЫЙ перевод формата ПОЛНОЙ ДАТЫ  в формат ЧИСЛО.МЕСЯЦ
for i in range(0, len(Date)):
    skip = []
    for j in range(0, len(Date[i])):
        if((ord(Date[i][j]) >= ord('0')) and (ord(Date[i][j]) <= ord('9'))):
            skip.append(Date[i][j])
    for i in range(0,6):
        skip.pop()
    skip.reverse()
    for i in range(0,4):
        skip.pop()
    skip.reverse()
    (skip[0] , skip[2]) = (skip[2] , skip[0])
    (skip[1], skip[3]) = (skip[3], skip[1])
    NormDate.append(skip[0] + skip[1] + '.' + skip[2] + skip[3])

#Костыль , чтобы месяц всегда был из 2 цифр
if (len(str(today.month)) == 1):
    we_need = str(today.day) + '.0' + str(today.month)
else:
    we_need = str(today.day) + '.' + str(today.month)

#we_need = "05.01"

#Пошло объявление именинников
People = []
Class = []
for i in range(0, len(NormDate)):
    if (NormDate[i] == we_need):
        if(durka[i] == 'Учитель'):
            People.append(name[i] + " " + patronymic[i])
            Class.append(surname[i])
        else:
            People.append(name[i] + " " + surname[i])
            Class.append(durka[i])
ch = len(People)

#Проверка количества именинников
if ch > 6:
    print("Именинников > 6 , программа не справляется :(")
    time.sleep(10000)
    exit()

#Шапка с учётом количества именинников
words1 = ("Сегодня " + day)
words2 = ''
if ch > 1:
    words2 = "День Рождения празднуют"
else:
    words2 = "День Рождения празднует"

date = ImageDraw.Draw(our_fon)
date.text((700, 80), words1, (0, 0, 0), anchor="ms", font=font1)
date.text((700, 150), words2, (0, 0, 0), anchor="ms", font=font1)


#Координаты центров картинок и текстов

TABLX = [[], [500], [200, 900], [200, 900, 550], [10, 700, 900, 450], [10, 900, 10, 830, 460], [10, 900, 10, 830, 360, 650]]
TABLY = [[], [300], [250, 700], [250, 700, 475], [200, 800, 200, 575], [200, 200, 650, 740, 875], [200, 200, 650, 740, 875, 470]]
TEXTX1 = [[], [725], [425, 1125], [425, 1125, 775], [235, 925, 1125, 675], [235, 1125, 235, 1055, 685], [235, 1125, 235, 1055, 585, 875]]
TEXTY1 = [[], [350], [300, 750], [300, 750, 525], [250, 850, 250, 620], [250, 250, 700, 790, 925], [250, 250, 700, 790, 925, 520]]
TEXTX2 = [[], [725], [425, 1125], [425, 1125, 775], [235, 925, 1125, 675], [235, 1125, 235, 1055, 685], [235, 1125, 235, 1055, 585, 875]]
TEXTY2 = [[], [410], [360, 810], [360, 810, 585], [310, 910, 310, 685], [310, 310, 760, 850, 985], [310, 310, 760, 850, 985, 580]]
GIFTX = [[], [200, 1000, 500], [200, 1000, 500], [200, 550, 1100, 750], [600, 250, 1150, 150], [500, 500, 1150, 200, 750], [500, 500, 1150, 200]]
GIFTY = [[], [350, 450, 550], [450, 250, 600], [450, 750, 450, 200], [250, 750, 450, 375], [200, 600, 330, 380, 400], [200, 650, 330, 380]]

#Вывод всех объектов на экран
for i in range(0, ch):
    our_fon.paste(tabl, (TABLX[ch][i], TABLY[ch][i]))
    date.text((TEXTX1[ch][i], TEXTY1[ch][i]), People[i], (0, 0, 0), anchor="ms", font=font2)
    date.text((TEXTX2[ch][i], TEXTY2[ch][i]), Class[i], (0, 0, 0), anchor="ms", font=font2)

for i in range(0, len(GIFTX[ch])):
    present = random.choice(mask)
    our_fon.paste(present, (GIFTX[ch][i], GIFTY[ch][i]))
    mask.remove(present)

our_fon.show()
our_fon.save(f"{we_need}.jpg")
