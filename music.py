# Эта программа - автоматическое скачивание и воспроизведение музыки

try: import requests, vlc
except: os.system("pip3 install requests python-vlc")

# Для начала надо скачать музыку, а ты думал.
    
# Мы создаём аудиофайл.
f = open(r"Portal OST - Still alive.mp3", "wb")
print(r"Portal OST - Still alive.mp3")

# Мы скачиваем файл в файл :)
print("Downloading file.", end="")
for i in range(0, 20):
    print(".", end="")
print("")
send = requests.get("https://ruv.hotmo.org/get/music/20190408/Portal_OST_-_Still_Alive_63380133.mp3")
f.write(send.content)
f.close()

# Мы воспроизводим файл.
print("Opening \"Portal OST - Still alive.mp3\"...")
p = vlc.MediaPlayer("Portal OST - Still alive.mp3")
print("Playing...")
p.play()
