from PIL import Image, ImageDraw, ImageFont
from datetime import date
import random

today = date.today()
day = "I love gay sex"
if today.month == 1:
    day = str(today.day) + " января"
if today.month == 2:
    day = str(today.day) + " февраля"
if today.month == 3:
    day = str(today.day) + " марта"
if today.month == 4:
    day = str(today.day) + " апреля"
if today.month == 5:
    day = str(today.day) + " мая"
if today.month == 6:
    day = str(today.day) + " июня"
if today.month == 7:
    day = str(today.day) + " июля"
if today.month == 8:
    day = str(today.day) + " августа"
if today.month == 9:
    day = str(today.day) + " сентября"
if today.month == 10:
    day = str(today.day) + " октября"
if today.month == 11:
    day = str(today.day) + " ноября"
if today.month == 12:
    day = str(today.day) + " декабря"

words1 = ("Сегодня " + day)
words2 = "Мы поздравляем с Днём Рождения:"
print("Сколько людей мы сегодня поздравляем?")
ch = int(input())
print("Кого сегодня поздравляем?")
print("Введите имя и фамилию в ВИНИТЕЛЬНОМ падеже и класс с буквой.")
print("Класс с буквой ученика или фамилию преподавателя отделяйте переводом строки.")
print("Данные разных людей разделяйте переводом строки.")

our_fon = Image.open('Фон1.jpg')
tabl = Image.open('Табл.jpg')
tort1 = Image.open('Торт1.jpg')
tort2 = Image.open('Торт2.jpg')
tort3 = Image.open('Торт3.jpg')
podarok1 = Image.open('Подарок1.jpg')
podarok2 = Image.open('Подарок2.jpg')
podarok3 = Image.open('Подарок3.jpg')
font1 = ImageFont.truetype("comicz.ttf", 65)
font2 = ImageFont.truetype("ComicSansMS3.ttf", 35)
mask = [tort1, tort2, tort3, podarok1, podarok2, podarok3]

date = ImageDraw.Draw(our_fon)
date.text((700, 80), words1, (0, 0, 0), anchor="ms", font=font1)
date.text((700, 150), words2, (0, 0, 0), anchor="ms", font=font1)

People = []
Class = []
tablx = []
tably = []
textx1 = []
texty1 = []
textx2 = []
texty2 = []
giftx = []
gifty = []

for i in range(0, ch):
    people1 = input()
    class1 = input()
    for j in range(0, len(class1)):
        if (class1[j] >= '0' and class1[j] <= '9'):
            class1 = class1 + " класс"
            break
    People.append(people1)
    Class.append(class1)

if ch == 1:
    tablx = [500]
    tably = [300]
    textx1 = [725]
    texty1 = [350]
    textx2 = [725]
    texty2 = [410]
    giftx = [200, 1000, 500]
    gifty = [350, 450, 550]

if ch == 2:
    tablx = [200, 900]
    tably = [250, 700]
    textx1 = [425, 1125]
    texty1 = [300, 750]
    textx2 = [425, 1125]
    texty2 = [360, 810]
    giftx = [200, 1000, 550]
    gifty = [450, 250, 600]

if ch == 3:
    tablx = [200, 900, 550]
    tably = [250, 700, 475]
    textx1 = [425, 1125, 775]
    texty1 = [300, 750, 525]
    textx2 = [425, 1125, 775]
    texty2 = [360, 810, 585]
    giftx = [200, 550, 1100, 750]
    gifty = [450, 750, 450, 200]

if ch == 4:
    tablx = [10, 700, 900, 450]
    tably = [200, 800, 200, 575]
    textx1 = [235, 925, 1125, 675]
    texty1 = [250, 850, 250, 620]
    textx2 = [235, 925, 1125, 675]
    texty2 = [310, 910, 310, 685]
    giftx = [600, 250, 1150, 150]
    gifty = [250, 750, 450, 375]

if ch == 5:
    tablx = [10, 900, 10, 830, 460]
    tably = [200, 200, 650, 740, 875]
    textx1 = [235, 1125, 235, 1055, 685]
    texty1 = [250, 250, 700, 790, 925]
    textx2 = [235, 1125, 235, 1055, 685]
    texty2 = [310, 310, 760, 850, 985]
    giftx = [500, 500, 1150, 200]
    gifty = [200, 650, 330, 380]

if ch == 6:
    tablx = [10, 900, 10, 830, 360, 650]
    tably = [200, 200, 650, 740, 875, 470]
    textx1 = [235, 1125, 235, 1055, 585, 875]
    texty1 = [250, 250, 700, 790, 925, 520]
    textx2 = [235, 1125, 235, 1055, 585, 875]
    texty2 = [310, 310, 760, 850, 985, 580]
    giftx = [500, 500, 1150, 200]
    gifty = [200, 650, 330, 380]

for i in range(0, ch):
    our_fon.paste(tabl, (tablx[i], tably[i]))
    date.text((textx1[i], texty1[i]), People[i], (0, 0, 0), anchor="ms", font=font2)
    date.text((textx2[i], texty2[i]), Class[i], (0, 0, 0), anchor="ms", font=font2)
for i in range(0, len(giftx)):
    present = random.choice(mask)
    our_fon.paste(present, (giftx[i], gifty[i]))
    mask.remove(present)

our_fon.show()
our_fon.save("Картинка1.jpg")

