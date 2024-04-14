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
our_fon = Image.open('Фон.jpg')
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


if(ch == 1):
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"

    # Вывод текста на экран с учётом шрифта и даты
    date = ImageDraw.Draw(our_fon)
    date.text((400, 10), words1, (0, 0, 0), font=font1)
    date.text((130, 100), words2, (0, 0, 0), font=font1)

    #Вывод именинников
    our_fon.paste(tabl, (500, 300))
    date.text((500, 320), people1, (0, 0, 0), font=font2)
    date.text((660, 360), class1, (0, 0, 0), font=font2)

    #Вывод подарков для именинников
    present1 = random.choice(mask)
    our_fon.paste(present1, (200, 350))
    mask.remove(present1)
    present2 = random.choice(mask)
    our_fon.paste(present2 , (1000, 450))
    mask.remove(present2)
    present3 = random.choice(mask)
    our_fon.paste(present3, (500, 550))
    mask.remove(present3)

    #Экран
    our_fon.show()
    our_fon.save("Картинка1.jpg")

if(ch == 2):
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"
    people2 = input()
    class2 = input()
    class2 = class2 + " класс"

    # Вывод текста на экран с учётом шрифта и даты
    date = ImageDraw.Draw(our_fon)
    date.text((400, 10), words1, (0, 0, 0), font=font1)
    date.text((130, 100), words2, (0, 0, 0), font=font1)

    #Вывод именинников
    our_fon.paste(tabl, (200, 250))
    date.text((200, 270), people1, (0, 0, 0), font=font2)
    date.text((360, 310), class1, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (900, 700))
    date.text((900, 720), people2, (0, 0, 0), font=font2)
    date.text((1060, 760), class2, (0, 0, 0), font=font2)

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



if(ch == 3):
    people1 = input()
    class1 = input()
    class1 = class1 + " класс"
    people2 = input()
    class2 = input()
    class2 = class2 + " класс"
    people3 = input()
    class3 = input()
    class3 = class3 + " класс"

    # Вывод текста на экран с учётом шрифта и даты
    date = ImageDraw.Draw(our_fon)
    date.text((400, 10), words1, (0, 0, 0), font=font1)
    date.text((130, 100), words2, (0, 0, 0), font=font1)

    #Вывод именинников
    our_fon.paste(tabl, (200, 250))
    date.text((200, 270), people1, (0, 0, 0), font=font2)
    date.text((360, 310), class1, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (900, 700))
    date.text((900, 720), people2, (0, 0, 0), font=font2)
    date.text((1060, 760), class2, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (550, 475))
    date.text((550, 495), people3, (0, 0, 0), font=font2)
    date.text((710, 535), class3, (0, 0, 0), font=font2)

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

if(ch == 4):
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
    # Вывод текста на экран с учётом шрифта и даты
    date = ImageDraw.Draw(our_fon)
    date.text((400, 10), words1, (0, 0, 0), font=font1)
    date.text((130, 100), words2, (0, 0, 0), font=font1)

    #Вывод именинников
    our_fon.paste(tabl, (10, 200))
    date.text((10, 220), people1, (0, 0, 0), font=font2)
    date.text((170, 260), class1, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (700, 800))
    date.text((700, 820), people2, (0, 0, 0), font=font2)
    date.text((860, 860), class2, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (900, 200))
    date.text((900, 220), people3, (0, 0, 0), font=font2)
    date.text((1060, 260), class3, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (450, 575))
    date.text((450, 595), people4, (0, 0, 0), font=font2)
    date.text((610, 635), class4, (0, 0, 0), font=font2)

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

if(ch == 5):
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
    # Вывод текста на экран с учётом шрифта и даты
    date = ImageDraw.Draw(our_fon)
    date.text((400, 10), words1, (0, 0, 0), font=font1)
    date.text((130, 100), words2, (0, 0, 0), font=font1)

    #Вывод именинников
    our_fon.paste(tabl, (10, 200))
    date.text((10, 220), people1, (0, 0, 0), font=font2)
    date.text((170, 260), class1, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (900, 200))
    date.text((900, 220), people3, (0, 0, 0), font=font2)
    date.text((1060, 260), class3, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (10, 650))
    date.text((10, 670), people2, (0, 0, 0), font=font2)
    date.text((170, 720), class2, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (830, 740))
    date.text((830, 760), people4, (0, 0, 0), font=font2)
    date.text((990, 800), class4, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (460, 875))
    date.text((460, 895), people5, (0, 0, 0), font=font2)
    date.text((620, 935), class5, (0, 0, 0), font=font2)

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

if(ch == 6):
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
    # Вывод текста на экран с учётом шрифта и даты
    date = ImageDraw.Draw(our_fon)
    date.text((400, 10), words1, (0, 0, 0), font=font1)
    date.text((130, 100), words2, (0, 0, 0), font=font1)

    # Вывод именинников
    our_fon.paste(tabl, (10, 200))
    date.text((10, 220), people1, (0, 0, 0), font=font2)
    date.text((170, 260), class1, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (900, 200))
    date.text((900, 220), people3, (0, 0, 0), font=font2)
    date.text((1060, 260), class3, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (10, 650))
    date.text((10, 670), people2, (0, 0, 0), font=font2)
    date.text((170, 720), class2, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (830, 740))
    date.text((830, 760), people4, (0, 0, 0), font=font2)
    date.text((990, 800), class4, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (460, 875))
    date.text((460, 895), people5, (0, 0, 0), font=font2)
    date.text((620, 935), class5, (0, 0, 0), font=font2)
    our_fon.paste(tabl, (650, 470))
    date.text((650, 490), people6, (0, 0, 0), font=font2)
    date.text((810, 530), class6, (0, 0, 0), font=font2)

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
