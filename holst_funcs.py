# Функции холста.


# Устанавливаем всякие модули.
from tkinter import *
import time, random, os, _tkinter, threading

# Эти модули автоматически установятся при первом запуске.
try:
    from PIL import Image
    import requests
    import vlc
except:
    os.system("pip3 install Pillow requests python-vlc")



'''Вот с этими переменными можно играться, и смотреть, что будет на холсте :)'''

# Для холста:
X_SIZE = 900             # Размер по X.
Y_SIZE = 500             # Размер по Y.
TITLE = "тестовый холст" # Название окна.
HL_TK = 3                # Толщина краёв. Напиши 0 для того, чтобы сделать окно без рамок.
RESIZABLE = True         # Можно ли изменять размеры окна? True - можно, False - нельзя.
TOPMOST = False          # Показывается ли приложение выше всех? True - да, False - нет.

# Для гифки:
XGIF = 100       # Расположение на холсте.
YGIF = 100
FILE = 'C++.gif' # Название файла
FRAMES = 16      # Кол-во кадров в гифке
WIDTH = 400      # Длина изображения
HEIGHT = 300     # Высота изображения
RESIZE_KOEF = 2  # Коэффициент уменьшения
FPS = 25         # Сколько кадров в секунду будет.

# Для текста:

                                                                    # Это мы создаём текст "Hello world!" в координатах (450, 50) от левого
                                                                    # верхнего угла, цвет - синий, шрифт Times New Roman 30-го размера.
                                                                    #
                                                                    # Если размер указан положительный, то размер будет в пунктах. Чтобы сделать
X_TEXT = 450             # Расположение на холсте.                  # размер в пикселях, нужно писать минус. Например, -50 - размер 50 пикселей.
Y_TEXT = 50                                                         #
TEXT = "Hello world!"    # Сам текст.                               # Также, меняйте шрифт на точное название того, который есть у вас в C:/Windows/Fonts,
COLOR = 'blue'           # Цвет текста. По умолчанию чёрный.        # по умолчанию, если шрифта нет, ставится Helvetica.
FONT = "Times New Roman" # Шрифт текста. По умолчанию "Helvetica".  #
SIZE = 30                # Размер текста.                           # Вот все виды цвета, который можно подставить в переменную COLOR:
                                                                    # 'red', 'orange', 'yellow', 'green', 'lime', 'blue', 'cyan', 'gray',
                                                                    # 'pink', 'light-gray', 'light-blue', 'black', 'white', 'purple'.
                                                                    # Также, в переменную можно подставить любое значение из палитры RGB вида "#991010"
                                                                    # или "#FF453D".

# Для поля ввода:
# Единственные обязательные значения - первые 2! Остальное - по желанию.

X_INPUT = 600          # Расположение на холсте.
Y_INPUT = 80

WIDTH_INPUT = 25       # Размер (почему-то не в пикселях,
                       #   фиг его знает)
RELIEF_INPUT = FLAT  # Тип границы, по умолчанию FLAT.
FONT_INPUT = "Courier" # Шрифт текста.
SIZE_INPUT = 20        # Размер текста.
STATE_INPUT = "normal" # Состояние строки ввода. Введите "disabled", чтобы
                       #   в неё нельзя было писать, "active" или "normal".
# Для этих переменных пишите None, чтобы вернуть к начальным значениям.
INPUT_COLOR = 'purple' # Цвет текста ввода. По умолчанию чёрный.
FBG_INPUT = None       # Фоновый цвет выделенного текста.
FG_INPUT = None        # Цвет выделенного текста.
BG_INPUT = None        # Фоновый цвет.
BD_INPUT = None        # Толщина границы.
CURSOR_INPUT = None    # Курсор указателя мыши при наведении на текстовое поле.

# Для кнопки вывода текста:
# Единственные обязательные значения - первые 3! Остальное - по желанию.

X_BTN = 600           # Расположение на холсте.
Y_BTN = 120
TEXT_BTN = "Вывести текст" # Текст кнопки.

ABG_BTN = None         # Фоновый цвет, когда кнопка нажата.         # Все переменные цвета, опять же,
AFG_BTN = None         # Цвет текста, когда кнопка нажата.          # поддерживают строковые цвета, такие 
BD_BTN = 2             # Толщина границы (по умолчанию 2)           # как "red", "blue", "yellow", а также
BG_BTN = None          # Фоновый цвет.                              # работают с RGB-кодами, такими как 
FG_BTN = None          # Цвет текста.                               # "#ea5c71", "#b7932c", "#452ac6" и т.п.
WIDTH_BTN = 15         # Ширина и высота кнопки (не в пикселях,
HEIGHT_BTN = 1         # опять же, фиг знает, почему).
FONT_BTN = None        # Шрифт текста.
SIZE_BTN = 12          # Размер текста.
HIGHLIGHT_BTN = "blue" # Цвет кнопки, когда она в фокусе.
JUSTIFY_BTN = LEFT     # Выравнивание текста. Значения LEFT, CENTER, RIGHT.
PADX_BTN = 0.5         # Отступ от границ кнопки до ее текста справа и слева.
PADY_BTN = 0.5         # Отступ от границ кнопки до ее текста сверху и снизу.
RELIEF_BTN = RAISED    # Тип границы кнопки. Есть 5 значений:
                       #   SUNKEN, RAISED, GROOVE, RIDGE, None
STATE_BTN = NORMAL     # Состояние кнопки. DISABLED, ACTIVE или NORMAL по умолчанию.
UNDERL_BTN = -1        # Номер символа в тексте кнопки, который подчёркивается.
                       #   По умолчанию -1, то есть никакой.
WRAPLENGTH_BTN = -1    # При положительном значении, строки текста будут
                       #   переноситься для вмещения в пространство кнопки.

'''Здесь начинается создание функций в программу.'''

                ####  ДЕЛАЕМ ТЕСТОВОЕ ПОЛЕ ВВОДА  ####


def make_field():
    # Сохраняем ввод как постоянно меняющуюся переменную StringVar.
    textField = StringVar()

    # Создаём поле msg и настраиваем его параметры.
    msg = Entry(textvariable=textField, fg=INPUT_COLOR, width=WIDTH_INPUT, relief=RELIEF_INPUT,
                selectbackground=FBG_INPUT, selectforeground=FG_INPUT, cursor=CURSOR_INPUT,
                font=(FONT_INPUT, 14), bg=BG_INPUT, bd=BD_INPUT, state=STATE_INPUT)
    msg.place(x=X_INPUT, y=Y_INPUT)

# Функция вывода текста для кнопки. При нажатию на кнопку вызывается
# функция, и выводится текст. Его можно сохранять в переменную.




               ####  ДЕЛАЕМ КНОПКУ ВЫВОДА ТЕКСТА  ####



# Кнопка вывода текста. Создаём, определяем и располагаем.

def make_button_1():
    msg_button = Button(text=TEXT_BTN, command=getmsg, activebackground=ABG_BTN, activeforeground=AFG_BTN,
                        bd=BD_BTN, bg=BG_BTN, fg=FG_BTN, width=WIDTH_BTN, height=HEIGHT_BTN, font=(FONT_BTN, SIZE_BTN),
                        highlightcolor=HIGHLIGHT_BTN, justify=JUSTIFY_BTN, padx=PADX_BTN,
                        pady=PADY_BTN, relief=RELIEF_BTN, state=STATE_BTN, underline=UNDERL_BTN, wraplength=WRAPLENGTH_BTN)
    msg_button.place(x=X_BTN, y=Y_BTN)

def mktext1(canvas):
    # Определяем функцией create_text текст.
    canvas.create_text(X_TEXT, Y_TEXT, text=TEXT, fill=COLOR, font=(FONT, SIZE))


# Функция обновления кадров.
def gifupdate(ind):
    
    # Берём из списка кадров определённый кадр.
    frame = frames[ind]

    # ID кадра должен прокручиваться внутри списка, поэтому мы следим.
    ind += 1
    ind %= FRAMES

    # label - это определённый лейбл, добавляемый на холст.
    # он здесь специально для этой гифки. Лейблов может быть
    # бесконечное количество, и в них можно постоянно обновлять информацию.
    # Вот здесь мы делаем лейбл - фотографией, а именно - кадром.
    label.configure(image=frame)

    # Определяем расположение кадра.
    label.place(x=100, y=100, width=WIDTH, height=HEIGHT)

    # Функция after получает на вход функцию, и миллисекунды, через которые
    # нужно убедт её повторить. Также, она получает на вход переменную ind функции,
    # которая работает, как счётчик, позволяющий прокручивать кадры. 
    tk.after(int(1000/FPS), gifupdate, ind)


# Создаём интерфейс.
tk = Tk()

# Называем окно.
tk.title(TITLE)

# Проверка на изменяемость размеров окна.
if not RESIZABLE:
    tk.resizable(0, 0)

# Проверка на... короче, загляни в описание переменных холста.
if TOPMOST:
    tk.wm_attributes("-topmost", 1)

# Создаём холст в окне, и определяем его.
cv = Canvas(tk, width=X_SIZE, height=Y_SIZE, highlightthickness=HL_TK)


# Список, в который мы записываем каждый кадр как изображение.
frames = []

# Запись в список.
for i in range(FRAMES):

    # Вот мы получаем определённый кадр.
    _frame = PhotoImage(file=FILE, format = 'gif -index %i' %(i))

    # Уменьшаем.
    _frame = _frame.zoom(1)
    _frame = _frame.subsample(RESIZE_KOEF)

    # Добавляем.
    frames.append(_frame)


mktext1(cv)
make_field()

def getmsg():
    print("Введённый текст: "+msg.get())

make_button_1()

# Обновление настроек.
cv.pack()
tk.update()
tk.update_idletasks()

# Создаём кусочек холста.                                         # \
label = Label(tk)                                                 #  |
label.pack()                                                      #  |- Это для гифки.
                                                                  #  |
# И начинаем обновлять кадры с нулевого, и так бесконечно.        #  |
tk.after(0, gifupdate, 0)                                         # /

# Постоянное обновление холста с проверкой за закрытие окна.
while True:
    try:
        cv.pack()
        tk.update()
        tk.update_idletasks()
    except _tkinter.TclError: break
    time.sleep(0.01)
