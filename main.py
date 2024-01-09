import pygame
import random
import time
import keyboard
print("Project Start")
pygame.font.init()
sc = pygame.display.set_mode((1200, 700))
sc.fill((0, 255, 160))
a = False
a1 = False
f = []
e = 0
etk = 0
sl = ["АНОНИМ", "СКВОРЕЧНИК", "ВИСКИ", "ТАДЖИК", "ИНТЕЛЛЕКТ", "ПОМОЩНИК", "КВАС", "СИНТЕЗАТОР", "РИНАТ", "ДУБАЙ", "17594", "МЁД"]
sl2 = ["АНОНИМ", "СКВОРЕЧНИК", "ВИСКИ", "ТАДЖИК", "ИНТЕЛЛЕКТ", "ПОМОЩНИК", "КВАС", "СИНТЕЗАТОР", "РИНАТ", "ДУБАЙ", "17594", "МЁД"]
sl3 = ["1 - АНОНИМ", "2 - СКВОРЕЧНИК", "3 - ВИСКИ", "4 - ТАДЖИК", "5 - ИНТЕЛЛЕКТ", "6 - ПОМОЩНИК", "7 - КВАС", "8 - СИНТЕЗАТОР", "9 - РИНАТ", "10 - ДУБАЙ", "11 - 17594", "12 - МЁД"]
azamat = sl
random.shuffle(azamat)
mouse_pressed = pygame.mouse.get_pressed()
pygame.draw.rect(sc, (64, 128, 255), (260, 20, 790, 185), 8)
f1 = pygame.font.SysFont("Serif", 46)
text1 = f1.render('Hello! Привет! С днем рождения!', True, (180, 0, 0))
sc.blit(text1, (337, 32))

f2 = pygame.font.SysFont("Serif", 28)
text2 = f2.render('Предлагаю пройти занимательный тест и проверить', True, (180, 0, 0))
sc.blit(text2, (337, 95))

f3 = pygame.font.SysFont("Serif", 28)
text3 = f3.render('остроту своей памяти', True, (180, 0, 0))
sc.blit(text3, (475, 138))

pygame.draw.rect(sc, (64, 128, 255), (260, 250, 790, 350), 8)

f4 = pygame.font.SysFont("Serif", 78)
text4 = f4.render('Понеслись!', True, (64, 51, 35))
sc.blit(text4, (437, 295))

f5 = pygame.font.SysFont("Serif", 78)
text5 = f5.render('ЛКМ чтобы начать', True, (184, 51, 35))
sc.blit(text5, (377, 375))

while a != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                a = True
    pygame.display.update()
    pygame.time.delay(15)

for i in range(100):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        sc.fill((184, 115, 51))
        f6 = pygame.font.SysFont("Serif", 278)
        text6 = f6.render('3', True, (184, 51, 35))
        sc.blit(text6, (377, 375))
    pygame.display.update()
    pygame.time.delay(15)

sc.fill((184, 115, 51))
for i in range(100):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f7 = pygame.font.SysFont("Serif", 278)
    text7 = f7.render('2', True, (184, 51, 35))
    sc.blit(text7, (377, 375))
    pygame.display.update()
    pygame.time.delay(15)

sc.fill((184, 115, 51))
for i in range(100):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f8 = pygame.font.SysFont("Serif", 278)
    text8 = f8.render('1', True, (184, 51, 35))
    sc.blit(text8, (377, 375))
    pygame.display.update()
    pygame.time.delay(15)

sc.fill((184, 155, 51))
for i in range(75):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f9 = pygame.font.SysFont("Serif", 278)
    text9 = f9.render('СТАРТ!', True, (45, 95, 255))
    sc.blit(text9, (177, 375))
    pygame.display.update()
    pygame.time.delay(15)

sc.fill((184, 170, 51))
for i in range(600):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f10 = pygame.font.SysFont("Serif", 48)
    text10 = f10.render('Запомни эти слова и их номера(20 сек)', True, (184, 51, 35))
    sc.blit(text10, (227, 75))
    f11 = pygame.font.SysFont("Serif", 38)
    text11 = f11.render('1 - аноним', True, (0, 71, 171))
    sc.blit(text11, (167, 135))
    f12 = pygame.font.SysFont("Serif", 38)
    text12 = f12.render('2 - скворечник', True, (0, 71, 171))
    sc.blit(text12, (167, 195))
    f13 = pygame.font.SysFont("Serif", 38)
    text13 = f13.render('3 - виски', True, (0, 71, 171))
    sc.blit(text13, (167, 255))
    f14 = pygame.font.SysFont("Serif", 38)
    text14 = f14.render('4 - таджик', True, (0, 71, 171))
    sc.blit(text14, (167, 315))
    f15 = pygame.font.SysFont("Serif", 38)
    text15 = f15.render('5 - интеллект', True, (0, 71, 171))
    sc.blit(text15, (167, 375))
    f16 = pygame.font.SysFont("Serif", 38)
    text16 = f16.render('6 - помощник', True, (0, 71, 171))
    sc.blit(text16, (167, 435))
    f17 = pygame.font.SysFont("Serif", 38)
    text17 = f17.render('7 - квас', True, (0, 71, 171))
    sc.blit(text17, (517, 135))
    f18 = pygame.font.SysFont("Serif", 38)
    text18 = f18.render('8 - синтезатор', True, (0, 71, 171))
    sc.blit(text18, (517, 195))
    f19 = pygame.font.SysFont("Serif", 38)
    text19 = f19.render('9 - Ринат', True, (0, 71, 171))
    sc.blit(text19, (517, 255))
    f20 = pygame.font.SysFont("Serif", 38)
    text20 = f20.render('10 - Дубай', True, (0, 71, 171))
    sc.blit(text20, (517, 315))
    f20 = pygame.font.SysFont("Serif", 38)
    text20 = f20.render('11 - 17594', True, (0, 71, 171))
    sc.blit(text20, (517, 375))
    f21 = pygame.font.SysFont("Serif", 38)
    text21 = f21.render('12 - мёд', True, (0, 71, 171))
    sc.blit(text21, (517, 435))
    pygame.display.update()
    pygame.time.delay(15)

sc.fill((205, 87, 0))
for i in range(90):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f22 = pygame.font.SysFont("Serif", 138)
    text22 = f22.render('Начинаем!', True, (0, 71, 171))
    sc.blit(text22, (317, 235))
    pygame.display.update()
    pygame.time.delay(15)
pygame.quit()
print("--------------------------")

for i in range(12):
    e1 = int(input("Введите цифру, под которым было слово " + azamat[i] + " - "))
    f.append(e1)
    x = azamat[i]
    y = sl2.index(x) + 1
    if etk == 3 and i == 1:
        z = e1
    else:
        if e1 == 155 and i == 0:
            print("Чит-код 155 успешно активирован!")
            print("Вне зависимости от ответов которые вы будете вводить дальше, в конце ваш результат все равно будет 12 баллов!")
            etk = 1
        else:
            if f[i] == y and e1 <= 12 and e1 >= 1:
                print("Верно! +1 балл")
                e = e + 1
                print("--------------------------")
            else:
                if e1 >= 1 and e1 <= 12:
                    print("Неверно")
            print("--------------------------")
        if e1 == 156 and i == 0:
            etk = 2
            print("Чит-код 156 успешно активирован!")
            e = e + 1
            print("Вот подсказки")
            print(sl3)
            print("--------------------------")
        if e1 == 157 and i == 0:
            print("Чит-код 157 успешно активирован!")
            print("В следующем вопросе, не обращая внимание на его содержание, укажите какое число баллов вы хотели бы иметь, и это число, введенную вами, счетчик покажет в конце теста")
            print("Число может быть от 0 до 200")
            etk = 3
if etk == 1:
    e = 12
if etk == 3:
    e = z
sc = pygame.display.set_mode((1350, 700))
sc.fill((240, 174, 0))
pygame.font.init()
while a1 != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f23 = pygame.font.SysFont("Serif", 138)
    text23 = f23.render('Поздравляем!', True, (0, 71, 171))
    sc.blit(text23, (251, 55))
    f24 = pygame.font.SysFont("Serif", 68)
    text24 = f24.render('Вы набрали целых', True, (65, 105, 225))
    sc.blit(text24, (131, 235))
    f25 = pygame.font.SysFont("Serif", 118)
    text25 = f25.render(str(e), True, (65, 105, 225))
    sc.blit(text25, (731, 181))
    f26 = pygame.font.SysFont("Serif", 118)
    text26 = f26.render('баллов!', True, (65, 105, 225))
    sc.blit(text26, (907, 181))
    f30 = pygame.font.SysFont("Serif", 69)
    text30 = f30.render('Верной дорогой идете, товарищ!!', True, (65, 105, 225))
    sc.blit(text30, (218, 331))
    f27 = pygame.font.SysFont("Serif", 39)
    text27 = f27.render('Спасибо за прохождение моего теста!)', True, (163, 62, 0))
    sc.blit(text27, (694, 525))
    f28 = pygame.font.SysFont("Serif", 39)
    text28 = f28.render('Автор - tutboroma7777@gmail.com', True, (163, 62, 0))
    sc.blit(text28, (705, 585))
    f29 = pygame.font.SysFont("Serif", 39)
    text29 = f29.render('Discord - КТО НАСРАЛ ТОТ УБРАЛ#6991', True, (163, 62, 0))
    sc.blit(text29, (739, 645))
    pygame.display.update()
    pygame.time.delay(15)
