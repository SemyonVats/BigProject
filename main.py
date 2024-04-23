from PIL import Image, ImageDraw, ImageFont
import random

#Запрос и генерация сегодняшней даты и именинников, как текстовой строки
print("Введите дату: ")
day = input()
words1 = ("Сегодня " + day)
words2 = "Мы поздравляем с Днём Рождения:"
print("Сколько людей мы сегодня поздравляем?")
ch = int(input())
print("Кого сегодня поздравляем?")
print("Введите имя и фамилию в ВИНИТЕЛЬНОМ падеже и класс с буквой. Класс с буквой отделяйте переводом строки.")
print("Данные разных людей разделяйте переводом строки.")

#Объявление переменных
our_fon1 = Image.open('Фон1.jpg')
our_fon2 = Image.open('Фон2.jpg')
tabl = Image.open('Табл.jpg')
tort1 = Image.open('Торт1.jpg')
tort2 = Image.open('Торт2.jpg')
tort3 = Image.open('Торт3.jpg')
podarok1 = Image.open('Подарок1.jpg')
podarok2 = Image.open('Подарок2.jpg')
podarok3 = Image.open('Подарок3.jpg')
font1 = ImageFont.truetype("arial.ttf", 70)
font2 = ImageFont.truetype("calibri.ttf", 35)
mask = [tort1, tort2, tort3, podarok1, podarok2, podarok3]

#Случайный выбор фона
fonmask = [our_fon1, our_fon2]
our_fon = random.choice(fonmask)
fonmask.remove(our_fon)

# Вывод текста на экран с учётом шрифта и даты
date = ImageDraw.Draw(our_fon1)
date.text((400, 10), words1, (0, 0, 0), font=font1)
date.text((130, 100), words2, (0, 0, 0), font=font1)

if ch == 1:
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"

    #Вывод именинников
    our_fon.paste(tabl, (500, 300))
    date.text((725, 350), people1, (0, 0, 0), anchor="ms", font=font2)
    date.text((725, 410), class1, (0, 0, 0), anchor="ms", font=font2)

    #Вывод подарков для именинников
    present1 = random.choice(mask)
    our_fon.paste(present1, (200, 350))
    mask.remove(present1)
    present2 = random.choice(mask)
    our_fon.paste(present2, (1000, 450))
    mask.remove(present2)
    present3 = random.choice(mask)
    our_fon.paste(present3, (500, 550))
    mask.remove(present3)

    #Экран
    our_fon.show()
    our_fon.save("Картинка1.jpg")

if ch == 2:
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"
    people2 = input()
    class2 = input()
    class2 = class2 + " класс"

    #Вывод именинников
    our_fon.paste(tabl, (200, 250))
    date.text((425, 300), people1, (0, 0, 0), anchor="ms", font=font2)
    date.text((425, 360), class1, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (900, 700))
    date.text((1125, 750), people2, (0, 0, 0), anchor="ms", font=font2)
    date.text((1125, 810), class2, (0, 0, 0), anchor="ms", font=font2)

    #Вывод подарков для именинников
    present1 = random.choice(mask)
    our_fon.paste(present1, (200, 450))
    mask.remove(present1)
    present2 = random.choice(mask)
    our_fon.paste(present2, (1000, 250))
    mask.remove(present2)
    present3 = random.choice(mask)
    our_fon.paste(present3, (550, 600))
    mask.remove(present3)

    #Экран
    our_fon.show()
    our_fon.save("Картинка1.jpg")



if ch == 3:
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"
    people2 = input()
    class2 = input()
    class2 = class2 + " класс"
    people3 = input()
    class3 = input()
    class3 = class3 + " класс"

    #Вывод именинников
    our_fon.paste(tabl, (200, 250))
    date.text((425, 300), people1, (0, 0, 0), anchor="ms", font=font2)
    date.text((425, 360), class1, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (900, 700))
    date.text((1125, 750), people2, (0, 0, 0), anchor="ms", font=font2)
    date.text((1125, 810), class2, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (550, 475))
    date.text((775, 525), people3, (0, 0, 0), anchor="ms", font=font2)
    date.text((775, 585), class3, (0, 0, 0), anchor="ms", font=font2)

    #Вывод подарков для именинников
    present1 = random.choice(mask)
    our_fon.paste(present1, (200, 450))
    mask.remove(present1)
    present2 = random.choice(mask)
    our_fon.paste(present2, (550, 750))
    mask.remove(present2)
    present3 = random.choice(mask)
    our_fon.paste(present3, (1100, 450))
    mask.remove(present3)
    present4 = random.choice(mask)
    our_fon.paste(present4, (750, 200))
    mask.remove(present4)

    #Экран
    our_fon.show()
    our_fon.save("Картинка1.jpg")

if ch == 4:
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"
    people2 = input()
    class2 = input()
    class2 = class2 + " класс"
    people3 = input()
    class3 = input()
    class3 = class3 + " класс"
    people4 = input()
    class4 = input()
    class4 = class4 + " класс"

    #Вывод именинников
    our_fon.paste(tabl, (10, 200))
    date.text((235, 250), people1, (0, 0, 0), anchor="ms", font=font2)
    date.text((235, 310), class1, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (700, 800))
    date.text((925, 850), people2, (0, 0, 0), anchor="ms", font=font2)
    date.text((925, 910), class2, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (900, 200))
    date.text((1125, 250), people3, (0, 0, 0), anchor="ms", font=font2)
    date.text((1125, 310), class3, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (450, 575))
    date.text((675, 625), people4, (0, 0, 0), anchor="ms", font=font2)
    date.text((675, 685), class4, (0, 0, 0), anchor="ms", font=font2)

    #Вывод подарков для именинников
    present1 = random.choice(mask)
    our_fon.paste(present1, (600, 250))
    mask.remove(present1)
    present2 = random.choice(mask)
    our_fon.paste(present2, (250, 750))
    mask.remove(present2)
    present3 = random.choice(mask)
    our_fon.paste(present3, (1150, 450))
    mask.remove(present3)
    present4 = random.choice(mask)
    our_fon.paste(present4, (150, 375))
    mask.remove(present4)

    #Экран
    our_fon.show()
    our_fon.save("Картинка1.jpg")

if ch == 5:
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"
    people2 = input()
    class2 = input()
    class2 = class2 + " класс"
    people3 = input()
    class3 = input()
    class3 = class3 + " класс"
    people4 = input()
    class4 = input()
    class4 = class4 + " класс"
    people5 = input()
    class5 = input()
    class5 = class5 + " класс"

    #Вывод именинников
    our_fon.paste(tabl, (10, 200))
    date.text((235, 250), people1, (0, 0, 0), anchor="ms", font=font2)
    date.text((235, 310), class1, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (900, 200))
    date.text((1125, 250), people3, (0, 0, 0), anchor="ms", font=font2)
    date.text((1125, 310), class3, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (10, 650))
    date.text((235, 700), people2, (0, 0, 0), anchor="ms", font=font2)
    date.text((235, 760), class2, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (830, 740))
    date.text((1055, 790), people4, (0, 0, 0), anchor="ms", font=font2)
    date.text((1055, 850), class4, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (460, 875))
    date.text((685, 925), people5, (0, 0, 0), anchor="ms", font=font2)
    date.text((685, 985), class5, (0, 0, 0), anchor="ms", font=font2)

    #Вывод подарков для именинников
    present1 = random.choice(mask)
    our_fon.paste(present1, (500, 200))
    mask.remove(present1)
    present2 = random.choice(mask)
    our_fon.paste(present2, (500, 650))
    mask.remove(present2)
    present3 = random.choice(mask)
    our_fon.paste(present3, (1150, 330))
    mask.remove(present3)
    present4 = random.choice(mask)
    our_fon.paste(present4, (200, 380))
    mask.remove(present4)
    present5 = random.choice(mask)
    our_fon.paste(present5, (750, 430))
    mask.remove(present5)

    #Экран
    our_fon.show()
    our_fon.save("Картинка1.jpg")

if ch == 6:
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"
    people2 = input()
    class2 = input()
    class2 = class2 + " класс"
    people3 = input()
    class3 = input()
    class3 = class3 + " класс"
    people4 = input()
    class4 = input()
    class4 = class4 + " класс"
    people5 = input()
    class5 = input()
    class5 = class5 + " класс"
    people6 = input()
    class6 = input()
    class6 = class6 + " класс"

    # Вывод именинников
    our_fon.paste(tabl, (10, 200))
    date.text((235, 250), people1, (0, 0, 0), anchor="ms", font=font2)
    date.text((235, 310), class1, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (900, 200))
    date.text((1125, 250), people3, (0, 0, 0), anchor="ms", font=font2)
    date.text((1125, 310), class3, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (10, 650))
    date.text((235, 700), people2, (0, 0, 0), anchor="ms", font=font2)
    date.text((235, 760), class2, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (830, 740))
    date.text((1055, 790), people4, (0, 0, 0), anchor="ms", font=font2)
    date.text((1055, 850), class4, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (460, 875))
    date.text((685, 925), people5, (0, 0, 0), anchor="ms", font=font2)
    date.text((685, 985), class5, (0, 0, 0), anchor="ms", font=font2)
    our_fon.paste(tabl, (650, 470))
    date.text((875, 520), people6, (0, 0, 0), anchor="ms", font=font2)
    date.text((875, 580), class6, (0, 0, 0), anchor="ms", font=font2)

    #Вывод подарков для именинников
    present1 = random.choice(mask)
    our_fon.paste(present1, (500, 200))
    mask.remove(present1)
    present2 = random.choice(mask)
    our_fon.paste(present2, (500, 650))
    mask.remove(present2)
    present3 = random.choice(mask)
    our_fon.paste(present3, (1150, 330))
    mask.remove(present3)
    present4 = random.choice(mask)
    our_fon.paste(present4, (200, 380))
    mask.remove(present4)

    #Экран
    our_fon.show()
    our_fon.save("Картинка1.jpg")

