from winsound import *
from time import *

def l():
    Beep(1000, 400)
def s():
    Beep(1000, 170)

def cesar(shift, letter, lang='ru'):
    if lang == 'en':
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
               'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    if lang == 'ru':
        letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И',
                   'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                   'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
                   'Э', 'Ю', 'Я']
    fl = False
    for i in range(0, len(letters)):
        if letters[i] == letter:
            fl = True
            break
    if fl == False:
        return letter
    i += shift
    try:
        tri = letters[i]
    except IndexError:
        i -= len(letters)
    return letters[i]

def azmors(sym):
    if sym == 'А' or sym == 'а' or sym == 'A' or sym == 'a':
        return '.- '
    elif sym == 'Б' or sym == 'б' or sym == 'B' or sym == 'b':
        return '-... '
    elif sym == 'В' or sym == 'в' or sym == 'W' or sym == 'w':
        return '.-- '
    elif sym == 'Г' or sym == 'г' or sym == 'G' or sym == 'g':
        return '--. '
    elif sym == 'Д' or sym == 'д' or sym == 'D' or sym == 'd':
        return '-.. '
    elif sym == 'Е' or sym == 'е' or sym == 'E' or sym == 'e' or sym == 'Ё' or sym == 'ё':
        return '. '
    elif sym == 'Ж' or sym == 'ж' or sym == 'V' or sym == 'v':
        return '...- '
    elif sym == 'З' or sym == 'з' or sym == 'Z' or sym == 'z':
        return '--.. '
    elif sym == 'И' or sym == 'и' or sym == 'I' or sym == 'i':
        return '.. '
    elif sym == 'Й' or sym == 'й' or sym == 'J' or sym == 'j':
        return '.--- '
    elif sym == 'К' or sym == 'к' or sym == 'K' or sym == 'k':
        return '-.- '
    elif sym == 'Л' or sym == 'л' or sym == 'L' or sym == 'l':
        return '.-.. '
    elif sym == 'М' or sym == 'м' or sym == 'M' or sym == 'm':
        return '-- '
    elif sym == 'Н' or sym == 'н' or sym == 'N' or sym == 'n':
        return '-. '
    elif sym == 'О' or sym == 'о' or sym == 'O' or sym == 'o':
        return '--- '
    elif sym == 'П' or sym == 'п' or sym == 'P' or sym == 'p':
        return '.--. '
    elif sym == 'Р' or sym == 'р' or sym == 'R' or sym == 'r':
        return '.-. '
    elif sym == 'С' or sym == 'с' or sym == 'S' or sym == 's':
        return '... '
    elif sym == 'Т' or sym == 'т' or sym == 'T' or sym == 't':
        return '- '
    elif sym == 'У' or sym == 'у' or sym == 'U' or sym == 'u':
        return '..- '
    elif sym == 'Ф' or sym == 'ф' or sym == 'F' or sym == 'f':
        return '..-. '
    elif sym == 'Х' or sym == 'х' or sym == 'H' or sym == 'h':
        return '.... '
    elif sym == 'Ц' or sym == 'ц' or sym == 'C' or sym == 'v':
        return '-.-. '
    elif sym == 'Ч' or sym == 'ч':
        return '---. '
    elif sym == 'Ш' or sym == 'ш':
        return '---- '
    elif sym == 'Щ' or sym == 'щ' or sym == 'Q' or sym == 'q':
        return '--.- '
    elif sym == 'Ъ' or sym == 'ъ':
        return '--.-- '
    elif sym == 'Ы' or sym == 'ы' or sym == 'Y' or sym == 'y':
        return '-.-- '
    elif sym == 'Ь' or sym == 'ь' or sym == 'X' or sym == 'x':
        return '-..- '
    elif sym == 'Э' or sym == 'э':
        return '..-.. '
    elif sym == 'Ю' or sym == 'ю':
        return '..-- '
    elif sym == 'Я' or sym == 'я':
        return '.-.- '
    elif sym == '1':
        return '.---- '
    elif sym == '2':
        return '..--- '
    elif sym == '3':
        return '...-- '
    elif sym == '4':
        return '....- '
    elif sym == '5':
        return '..... '
    elif sym == '6':
        return '-.... '
    elif sym == '7':
        return '--... '
    elif sym == '8':
        return '---.. '
    elif sym == '9':
        return '----. '
    elif sym == '0':
        return '----- '
    elif sym == '.':
        return '...... '
    elif sym == ',':
        return '.-.-.- '
    elif sym == ':':
        return '---... '
    elif sym == ';':
        return '-.-.-. '
    elif sym == '(' or sym == ')':
        return '-.--.- '
    elif sym == "'":
        return '.----. '
    elif sym == '"':
        return '.-..-. '
    elif sym == '-':
        return '-....- '
    elif sym == '/':
        return '-..-. '
    elif sym == '?':
        return '..--.. '
    elif sym == '!':
        return '--..-- '
    elif sym == '+':
        return '.-.-. '
    elif sym == ' ':
        return '-...- '
    elif sym == '@':
        return '.--.-. '
    else:
        return '........'
    

while True:
    print("\nВыберите кодировку:")
    print("1. ASCII")
    print("2. Азбука Морзе")
    print("3. Шифр Цезаря (Русский)")
    print("4. Шифр Цезаря (Английский)")
    print("5. Выход из программы")
    choice = input()
    if choice == '1':
        # 1. ASCII
        ch = input("Дешифровка/Зашифровка? [D/Z]: ")
        if ch == 'd' or ch == 'D':
            pass
        elif ch == 'z' or ch == 'Z':
            pass

    elif choice == '2':
        ch = input("Дешифровка/Зашифровка? [D/Z]: ")
        if ch == 'd' or ch == 'D':
            code = input("Введите шифр:\n")
            words = code.split(' ')
            codee_ru = ''
            codee_en = ''
            for word in words:
                if word == '.-':
                    codee_ru += 'А'
                    codee_en += 'A'

                elif word == '-...':
                    codee_ru += 'Б'
                    codee_en += 'B'

                elif word == '.--':
                    codee_ru += 'В'
                    codee_en += 'W'

                elif word == '--.':
                    codee_ru += 'Г'
                    codee_en += 'G'

                elif word == '-..':
                    codee_ru += 'Д'
                    codee_en += 'D'

                elif word == '.':
                    codee_ru += 'Е'
                    codee_en += 'E'

                elif word == '...-':
                    codee_ru += 'Ж'
                    codee_en += 'V'

                elif word == '--..':
                    codee_ru += 'З'
                    codee_en += 'Z'

                elif word == '..':
                    codee_ru += 'И'
                    codee_en += 'I'

                elif word == '.---':
                    codee_ru += 'Й'
                    codee_en += 'J'

                elif word == '-.-':
                    codee_ru += 'К'
                    codee_en += 'K'

                elif word == '.-..':
                    codee_ru += 'Л'
                    codee_en += 'L'

                elif word == '--':
                    codee_ru += 'М'
                    codee_en += 'M'

                elif word == '-.':
                    codee_ru += 'Н'
                    codee_en += 'N'

                elif word == '---':
                    codee_ru += 'О'
                    codee_en += 'O'

                elif word == '.--.':
                    codee_ru += 'П'
                    codee_en += 'P'

                elif word == '.-.':
                    codee_ru += 'Р'
                    codee_en += 'R'

                elif word == '...':
                    codee_ru += 'С'
                    codee_en += 'S'

                elif word == '-':
                    codee_ru += 'Т'
                    codee_en += 'T'

                elif word == '..-':
                    codee_ru += 'У'
                    codee_en += 'U'

                elif word == '..-.':
                    codee_ru += 'Ф'
                    codee_en += 'F'

                elif word == '....':
                    codee_ru += 'Х'
                    codee_en += 'H'

                elif word == '-.-.':
                    codee_ru += 'Ц'
                    codee_en += 'C'

                elif word == '---.':
                    codee_ru += 'Ч'

                elif word == '----':
                    codee_ru += 'Ш'

                elif word == '--.-':
                    codee_ru += 'Щ'
                    codee_en += 'Q'

                elif word == '--.--':
                    codee_ru += 'Ъ'

                elif word == '-.--':
                    codee_ru += 'Ы'
                    codee_en += 'Y'

                elif word == '-..-':
                    codee_ru += 'Ь'
                    codee_en += 'X'

                elif word == '..-..':
                    codee_ru += 'Э'

                elif word == '..--':
                    codee_ru += 'Ю'

                elif word == '.-.-':
                    codee_ru += 'Я'

                elif word == '.----':
                    codee_ru += '1'
                    codee_en += '1'

                elif word == '..---':
                    codee_ru += '2'
                    codee_en += '2'

                elif word == '...--':
                    codee_ru += '3'
                    codee_en += '3'

                elif word == '....-':
                    codee_ru += '4'
                    codee_en += '4'

                elif word == '.....':
                    codee_ru += '5'
                    codee_en += '5'

                elif word == '-....':
                    codee_ru += '6'
                    codee_en += '6'

                elif word == '--...':
                    codee_ru += '7'
                    codee_en += '7'

                elif word == '---..':
                    codee_ru += '8'
                    codee_en += '8'

                elif word == '----.':
                    codee_ru += '9'
                    codee_en += '9'

                elif word == '-----':
                    codee_ru += '0'
                    codee_en += '0'

                elif word == '......':
                    codee_ru += '.'
                    codee_en += '.'

                elif word == '.-.-.-':
                    codee_ru += ','
                    codee_en += ','

                elif word == '-.-.-.':
                    codee_ru += ';'
                    codee_en += ';'

                elif word == '---...':
                    codee_ru += ':'
                    codee_en += ':'

                elif word == '..--..':
                    codee_ru += '?'
                    codee_en += '?'

                elif word == '--..--':
                    codee_ru += '!'
                    codee_en += '!'

                elif word == '-....-':
                    codee_ru += '-'
                    codee_en += '-'

                elif word == '.-.-.':
                    codee_ru += '+'
                    codee_en += '+'

                elif word == '.-..-.':
                    codee_ru += '"'
                    codee_en += '"'

                elif word == '.----.':
                    codee_ru += "'"
                    codee_en += "'"

                elif word == '-.--.-':
                    codee_ru += '|'
                    codee_en += '|'

                elif word == '-..-.':
                    codee_ru += '/'
                    codee_en += '/'

                elif word == '.--.-.':
                    codee_ru += '@'
                    codee_en += '@'

                elif word == '........':
                    codee_ru += ' -ERROR- '
                    codee_en += ' -ERROR- '

                elif word == '-...-':
                    codee_ru += ' '
                    codee_en += ' '

                elif word == '..-.-':
                    codee_ru += ' -END- '
                    codee_en += ' -END- '

            print("\nРусская дешифровка:\n"+codee_ru)
            print("\nАнглийская дешифровка:\n"+codee_en)
        elif ch == 'z' or ch == 'Z':
            code = input("Введите шифр:\n")
            codee = ''
            for smb in code:
                _morse = azmors(smb)
                codee += _morse
            print("\nШифр:\n"+codee)
            for smb in codee:
                if smb == '.':
                    Beep(1000, 150)
                elif smb == '-':
                    Beep(1000, 450)
                else:
                    sleep(0.45)

    elif choice == '3':
        # 4. Шифр Цезаря (Русский)
        code = input("Введите шифр большими буквами:\n")
        print("Сдвиги на любое кол-во символов: ")
        for i in range(1, 33):
            decode = ''
            for c in code:
                _letter = cesar(i, c, 'ru')
                decode += _letter
            print(str(i)+" символ: "+decode)

    elif choice == '4':
        # 5. Шифр Цезаря (Английский)
        code = input("Введите шифр большими буквами:\n")
        print("Сдвиги на любое кол-во символов: ")
        for i in range(1, 26):
            decode = ''
            for c in code:
                _letter = cesar(i, c, 'en')
                decode += _letter
            print(str(i)+" символ: "+decode)

    elif choice == '5':
        break
