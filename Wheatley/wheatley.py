# Голосовой помощник Уитли.

# Если хочешь понять, как всё работает - оставлю тебе комментарии :)

# Для начала установим часть модулей. Потом остальные
import sys, datetime, os, time

def recognize(secs):
    pass

def calculator(s):
    pass

def answer(t):
    pass

def create_token(oauth_token):
    params = {'yandexPassportOauthToken': oauth_token}
    response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', params=params)                                                   
    decode_response = response.content.decode('UTF-8')
    text = json.loads(decode_response) 
    iam_token = text.get('iamToken')
    expires_iam_token = text.get('expiresAt')
    
    return iam_token, xpires_iam_token

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

# Начало программы.
try:
    import requests, pyaudio, wave, soundfile, json, winsound, datetime, pyperclip

    # Открываем файл с прибамбасами. Он нам нужен.
    f=open("прибамбасы.txt", mode="r", encoding="utf-16-le")
    onstring = f.read().split("\n")
    prefs = dict()
    for item in onstring:
        key = item.split(" : ")[0]
        value = item.split(" : ")[1:]
        prefs[key] = value

    # Берём оттуда инормацию для Яндекса.
    IAM_TOKEN = prefs["IAM_TOKEN"][0]
    expiration_date = prefs["IAM_TOKEN"][1]
    ID_FOLDER = prefs["ID_FOLDER"]
    if is_token_alive(expiration_date):
        raise IndexError

# Давай я тебе всё расскажу.
# Уитли работает на Yandex SpeechKit. Это набор для разработчиков, дающий две возможности:
# 1) Озвучивать текст.
# 2) Распознавать текст.
# Я использую 2-й пункт, чтобы ты мог общаться с Уитли.
# Для того, чтобы работать с Yandex SpeechKit, нужно стать разработчиком.
# Внимательно читай всё, что я пишу.

# Так, здесь если ты только-только первый раз запустил программу, поставь модуль install.
# Я услужливо запускаю командную строку.
except ModuleNotFoundError:
    os.system('pip install requests pyaudio wave soundfile datetime pyperclip')
    raise FileNotFoundError

except FileNotFoundError:
    print("Первый запуск - он такой, падажжи.")
    os.system("echo Подожди секунду, мы тебе установим YANDEX API.")
    time.sleep(1)
    os.system("@\"%SystemRoot%\System32\WindowsPowerShell\\v1.0\powershell.exe\" -Command \"iex ((New-Object System.Net.WebClient).DownloadString('https://storage.yandexcloud.net/yandexcloud-yc/install.ps1'))\" && SET \"PATH=%PATH%;%USERPROFILE%\\yandex-cloud\\bin\"")
    os.system("Теперь напиши 1

except (KeyError, IndexError) as TokenErrors:
    print("Упс! Действие Лёхиного токена кончилось.")
    token = input("Вставь строку, что я тебе пришлю, сюда.\n")
    IAM_TOKEN = token[0]
    expiration_date = token[1]
    ID_FOLDER = token[2]
    f=open("tokens.txt", mode="w", encoding="utf-16-le")
    f.write("IAM_TOKEN : "+IAM_TOKEN+" : "+expiration_date+"\n")
    f.write("ID_FOLDER : "+ID_FOLDER+"\n")
    f.close()
    print("Всё готово! Включи звук через 3..", end="")
    time.sleep(1)
    print("2..", end="")
    time.sleep(1)
    print("1..")
    time.sleep(1)
# Ну, если ошибок нет, то в добрый путь!
else:
    print("|                                                                                                                              |")


# Теперь наконец начинаем программу.

hi()
