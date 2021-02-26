# Python-projects

В этом репозитории находятся все мои небольшие проекты на Python 2, 3.

Для работы с программами необходим Python 3, лучше всего использовать 3.8.6.
Далее нужно ввести следующие команды:

pip install --upgrade pip

pip install altgraph beautifulsoup4 certifi chardet click configobj configparser decorator et-xmlfile future httplib2 idna jdcal keyboard lxml networkx nibabel numpy opencv-python openpyxl packaging pandas pefile Pillow pip pyinstaller pyinstaller-hooks-contrib PyMuPDF pyparsing PyPDF2 python-dateutil python-vlc pytz pywin32-ctypes pyxnat requests scipy setuptools six smtp soupsieve urllib3 wheel

pip3 install altgraph beautifulsoup4 certifi chardet click configobj configparser decorator et-xmlfile future httplib2 idna jdcal keyboard lxml networkx nibabel numpy opencv-python openpyxl packaging pandas pefile Pillow pip pyinstaller pyinstaller-hooks-contrib PyMuPDF pyparsing PyPDF2 python-dateutil python-vlc pytz pywin32-ctypes pyxnat requests scipy setuptools six smtp soupsieve urllib3 wheel
Если какие-то модули не установились, то нужен пакет установщика. Пакеты тоже находятся в репозитории.

Репозиторий постоянно будет пополняться и дополняться, у меня много проектов на Python. Также в репозитории есть вспомогательные файлы к программам.

Вот их список с описанием каждого из них:

audiosort.py - программа, берущая список из целых чисел и сортируюшая его. Используя модуль winsound, визуализирует сортировку звуками определённых частот.

azmors keys.py - программа, использующая keyboard и winsound, чтобы считывать нажатие клавиш на клавиатуре и воспроизводить звуки разных частот и длительностей. Удобно при передаче сообщений Азбукой Морзе. 
При нажатии клавиш Q, W, E, R, T, Y, U, I, O соответсвенно воспроизводятся звуки частотой 1000, 2000, 3000, 4000... 9000 ГГц и длительностью 400 мс. При нажатии клавиш A, S, D, F, G, H, J, K, L соответственно воспроизводятся звуки тех же частот, но длительностью 150 мс. 400 и 150 мс считаются официально длинным и коротким сигналом при передаче сообщения Азбукой Морзе.

bally.py - программа для изучения последовательного изменения движения объекта на холсте модуля ToolKit Interface, или Tkinter. Вначале пользователю даётся выбрать размер шара в пикселях, затем его цвет (по-английски). Затем появляется холст, на котором выбранный пользователем шар падает с нулевой скоростью и, ударяясь об нижнюю границу холста, подскакивает "с потерей энергии", вследствие чего его наивысшая точка снижается до тех пор, пока он не остановится у нижней границы. В это время в консоли высвечиваются изменения на холсте.
В начале программы есть переменная Vy, это начальная скорость шара. Её можно изменить для другого результата программы. Поставьте отрицательную скорость, чтобы шар взлетел вверх.
Там же есть переменная dura, которая по умолчанию имеет значение 1.1, что означает "потерю скорости", а именно, скорость отскакивания шара от нижней границы экрана становится делённой на значение переменной dura, или помноженной на 10/11. Её можно увеличить для большей потери скорости, уменьшить для меньшей. Если dura будет меньше 1, то шар начнёт ломать второй закон термодинамики.
Программа несовершенна, шар может застрять, улететь и т.п. Рекомендую ставить размер шара 50, чтобы избежать проблем. Цвета могут быть такими:
red, yellow, orange, blue, pink, purple, gray, white, black, light-gray, light-blue, brown.

CODE.py - программа, дающая возможность кодировать и декодировать текст на русском, английском языках на или с различных шифров.
На данный момент не все добавлены в программу, но уже есть ASCII, Азбука Морзе, Шифр Цезаря (на русском и английском, итого 6 шифров, для каждого шифратор и дешифратор).
Ещё есть аудиовоспроизведение закодированного в Азбуку Морзе сообщения.

Collatz.py - программа для решения гипотезы Коллатца.

fibo.py - вывод чисел Фибоначчи.

graph.py - построение сетки на холсте модуля turtle с помощью большого количества черепашек.

holst_funcs.py - программа для изучения возможностей холста ToolKit Interface, или Tkinter.
В ней представлено множество примеров, и есть огромное количество переменных, которые можно изменять. Есть работа с GIF-изображениями, с полями ввода, кнопками, текстом.
Программа находится во вложенной одноимённой папке, к ней приложен файл C++.gif.

mail.py - находящийся в разработке почтовый мультиклиент. Находится во вложенной одноимённой папке. К нему, возможно, будут приложены мини-программы с функциями, которые надо добавить туда.
Программа использует возможности модулей SMTP, IMAP для подключения к почтовому ящику. Пока программа выглядит как бессвязное месиво кода, но уже рабочая и вмиг может прочитать все письма на почте.
В файле с расширением .txt есть концепт интерфейса. Рекомендую взглянуть.

move.py - программа, визуализирующая движение параллельно горизонту с помощью модуля turtle.

music.py - скачивание аудиофайла через запросы на Python 3.

neurotemp.py - нерабочая (на данный момент) нейросеть с 3 входами, 3 скрытыми слоями и 1 выходом.

Wheatley.py - проект другу на день рождения. Голосовой помощник на базе Yandex API с голосом Константина Карасика. Находится в разработке, файлы приложены в одноимённой папке. Проект довольно крупный, но всё и так понятно.

wiki.py - программа, ищущая заданный запрос в Википедии и анализирующая статью, если таковая есть, и выдающая скомплектованные абзацы.


Версии модулей, с которыми программы работают:

altgraph==0.17

beautifulsoup4==4.9.1

certifi==2020.6.20

chardet==3.0.4

click==7.1.2

configobj==5.0.6

configparser==5.0.0

decorator==4.4.2

et-xmlfile==1.0.1

future==0.18.2

httplib2==0.18.1

idna==2.10

jdcal==1.4.1

keyboard==0.13.5

lxml==4.5.2

networkx==2.5

nibabel==3.1.1

numpy @ file:///C:/Users/avkol/Desktop/Docs/%D0%94%D1%80%D1%83%D0%B3%D0%BE%D0%B5/numpy-1.18.4%2Bmkl-cp38-cp38-win_amd64.whl

Модуль numpy необходимо найти в интернете. Вставьте в поисковик "numpy-1.18.4mkl-cp38-cp38-win_amd64.whl".

opencv-python==4.5.1.48

openpyxl==3.0.5

packaging==20.4

pandas==1.1.1

pefile==2019.4.18

Pillow==8.1.0

pyinstaller==4.2

pyinstaller-hooks-contrib==2020.11

PyMuPDF==1.17.6

pyparsing==2.4.7

PyPDF2==1.26.0

python-dateutil==2.8.1

python-vlc==3.0.11115

pytz==2020.1

pywin32-ctypes==0.2.0

pyxnat==1.3

requests==2.24.0

scipy==1.5.2

six==1.15.0

smtp==0.1.0

soupsieve==2.0.1

urllib3==1.25.10
