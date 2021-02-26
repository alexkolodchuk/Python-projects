# Голосовой помощник Уитли.
# Если хочешь понять, как всё работает - оставлю тебе комментарии :)

# Это - функция проигрывания файлов
def p(file):
    try: winsound.PlaySound("audio\\"+file+".wav", winsound.SND_FILENAME)
    except TypeError: pass

# Это - начальное приветствие.
# С вероятностью 30% скажет, что ты ужасно выглядишь,
# И рандомно выбирает один из приветов.
def hi():
    privets = ["Привет!..", "Привет"]
    if random.randint(0, 10)==0 or random.randint(0, 10)==2 or random.randint(0, 10)==3:
        p("А! Ты выглядишь ужасно")
    p(privets[random.randint(0, 1)])

def recognize(secs):
    pass

def calculator(s):
    pass

def answer(t):
    pass

# Начало программы.
try: import winsound, sys, datetime, os, random
except ModuleNotFoundError:
    print("Вставь это в командную строку:\n\npip install winsound")
    os.startfile(r'C:\WINDOWS\system32\cmd.exe')
    sys.exit()

print("Добавь звук")

hi()

#while True:
#    pass
