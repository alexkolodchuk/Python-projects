# Это почтовый мультиклиент (ПМК v0). / This is a mail multiclient (MMC v0).                       !!! РУССКИЙ ЯЗЫК - ПО УМОЛЧАНИЮ / RUSSIAN - BY DEFAULT !!!
import imaplib, smtplib, email, socket, base64, urllib.parse; from email.mime.text import MIMEText; from email.header import Header # Импорт необходимых модулей. / Import the required modules.
imap = ['imap.yandex.ru','imap.gmail.com','imap.mail.yahoo.com','Outlook.Office365.com'] # Сохраняем все imap/smtp сервера.
smtp = ['smtp.yandex.ru','smtp.gmail.com','smtp.mail.yahoo.com','Outlook.office365.com'] # Keep all the imap/smtp servers.
while True: # Главный цикл. / Main loop.
    try: # Я добавил сохранение в файл значений почтового ящика. Он называется "p.txt". / I added saving to a file the values of the mailbox. It's called "p.txt".                ###########################################
        f = open(file='p.txt', encoding='utf-16-le', mode='r') # Сначала пытаемся прочитать из файла значение. / Firstly trying to read preferences from a file.                  # Внимание! При открытии почтового ящика  #
        m = f.read().split("\n")[1].split(", ") # Ок, получили. Теперь берём то, что нам нужно. / OK, we got it. Now we take what we need.                                        # все письма автоматически ПРОЧИТЫВАЮТСЯ! #
        print(m)                                                                                                                                                                  # 
        isrus = (m[3] == 'rus') # А здесь переменная, отвечающая за язык. (Все выражения пройдут через цикл if isrus - else.) / And here is the variable responsible
                                                                                    #for the language. (All expressions will pass through the if isrus - else loop.)
        try: # Здесь попытка подключения по протоколу SMTP (отправка писем). / Here is an attempt to connect via SMTP (sending emails).
            Smtp = smtplib.SMTP(smtp[int(m[0])], 587); Smtp.starttls(); Smtp.login(m[1], m[2])
        except (socket.gaierror, NameError, smtplib.SMTPAuthenticationError, IndexError, ValueError) as authErrors: # Различные ошибки, связанные с неправильным подключением. /
                                                                                    # / Various errors related to incorrect connection.
            if isrus: print("Invalid input/No Internet connection. Try again\nFor help type \"help\".")
            else: print("Неверный ввод/Нет подключения к Интернету. Попробуйте снова. Для получения справки введите \"help\".")
            continue
        else: Smtp.quit() # При успешном подключении выходим из текущей сессии SMTP. / If the connection is successful, we exit the current SMTP session.
        f.close() # Закрываем файл. / Closing the file.
    except (FileNotFoundError, KeyError) as fileErrors: # Если файл с настройками ещё не создан... / If the settings file hasn't been created yet...
        try:
            m = input("\nЧерез запятую 4 значения: Yandex[0]/Gmail[1]/Outlook[2]/Yahoo[3], почта, пароль: ").split(", ") # Ввод значений. / To enter values.
            m.append('rus') # Язык. / Language.
            Smtp = smtplib.SMTP(smtp[int(m[0])], 587); Smtp.starttls(); Smtp.login(m[1], m[2]) # Те же действия, что и в 12-й строке. / The same actions as in line 12.
        except (socket.gaierror, NameError, smtplib.SMTPAuthenticationError, IndexError, ValueError) as authErrors:
            if isrus: print("Invalid input/No Internet connection. Try again\nFor help type \"help\".")
            else: print("Неверный ввод/Нет подключения к Интернету. Попробуйте снова. Для получения справки введите \"help\".")
            continue
        else: Smtp.quit()
        f = open(file='p.txt', encoding='utf-16-le', mode='w') # Создание файла и запись в него значений. / Creating a file and writing values to it.
        f.write("# -*- coding: utf-16-le -*- ☭\n"+m[0]+", "+m[1]+", "+m[2]+", "+m[3])
        f.close()
    def send(msg, hd, mail, mailers): # Функция send посылает текстовое сообщение msg с заголовком hd с почты mail на список почт mailers. / The send function sends an 'msg'
                                                                                    # text message with the 'hd' header from 'mail' mail to the 'mailers' mail list.
        msg = MIMEText(msg, 'plain', 'utf-8')
        msg['Subject'] = Header(hd, 'utf-8'); msg['From'] = m[1]; msg['To'] = mail2                                                                               ### !!!!!! ДОДЕЛАТЬ !!!!!! ###
        Smtp = smtplib.SMTP(smtp[int(m[0])], 587)
        try: Smtp.starttls(); Smtp.login(m[1], m[2]); Smtp.sendmail(m[1], mailers, msg.as_string())                                                               ### !!!!!! ДОДЕЛАТЬ !!!!!! ###
        finally: Smtp.quit()
    def read(msg, mailbox): # Функция read читает сообщение msg-ое по списку из почтового ящика mailbox. Возвращает словарь. / The read function reads the 'msg' message
                                                                                    # in the list from the mailbox 'mailbox'. Returns the dictionary.
        mail = imaplib.IMAP4_SSL(imap[int(m[0])]) # Подключение по протоколу SMTP (чтение почтовых ящиков).
        mail.login(m[1], m[2])
        mail.list()
        mail.select(mailbox) # Выбираем нужный ящик. Это могут быть Избранные, Входящие, Спам, Отправленные и другие.
        result, data = mail.uid('search', None, 'ALL') 
        result, data = mail.uid('fetch', data[0].split()[msg], '(RFC822)') # Танцы с бубнами в многомерных списках.
        letter = email.message_from_string(data[0][1].decode('koi8-r'))
        _mail = dict.fromkeys(['Message', 'To', 'From', 'Date', 'Subject', 'Message-Id']) # Создаём главный словарь.
        _mail['Message'] = [] # Это - тело письма. ЗДесь может быть лишь текст (одна часть), а может быть и HTML-документ, и гиперссылка, и текст.
        if letter.is_multipart(): # Если тело из нескольких частей, берём каждую.
            for payload in letter.get_payload():
                if payload.get_payload(decode=True) != None:
                    body = payload.get_payload(decode=True).decode('koi8-r')
                    _mail['Message'].append(body)
        else: # Если одна часть.
            body = letter.get_payload(decode=True).decode('koi8-r')
            _mail['Message'].append(body)
        #print(_mail['Message'])
        _mail['To'] = letter['To'] # Сохранение остальных данных - Кому, От Кого, Дата, Заголовок, Кодовый Номер Письма.
        fromi = email.utils.parseaddr(letter['From'])[0]
        if fromi[0:10] == "=?utf-8?b?" or fromi[0:10] == "=?UTF-8?B?" or fromi[0:10] == "=?UTF-8?b?" or fromi[0:10] == "=?utf-8?B?":
            sbjs = fromi.split(" ")
            _fromi = ""
            for sbj in sbjs:
                _fromi += base64.b64decode(str(sbj[10:]).encode("UTF-8")).decode("UTF-8")
        elif fromi[0:10] == "=?UTF-8?Q?" or fromi[0:10] == "=?utf-8?Q?":
            sbjs = fromi.split(" ")
            _fromi = ""
            for sbj in sbjs:
                if sbj[-4:-1] == '\r\n':
                    _sbj = sbj[10:-8].replace("=", "%").encode('utf8')
                else:
                    _sbj = sbj[10:-4].replace("=", "%").encode('utf8')
                _fromi += urllib.parse.unquote(bytes.decode(_sbj))
        else:
            _fromi = fromi
        _mail['From'] = [_fromi, email.utils.parseaddr(letter['From'])[1]]
        _mail['Date'] = letter['Date']
        if letter['Subject'][0:10] == "=?utf-8?b?" or letter['Subject'][0:10] == "=?UTF-8?B?" or letter['Subject'][0:10] == "=?UTF-8?b?" or letter['Subject'][0:10] == "=?utf-8?B?":
            sbjs = letter['Subject'].split(" ")
            _sbjs = []
            for sbj in sbjs:
                ssbj = sbj.split("\t")
                for ss in ssbj:
                    _sbjs.append(ss)
            sbjs = _sbjs
            _mail['Subject'] = ""
            for sbj in sbjs:
                try: _mail['Subject'] += base64.b64decode(str(sbj[10:]).encode("UTF-8")).decode("UTF-8")
                except UnicodeDecodeError: print(sbjs)
        elif letter['Subject'][0:10] == "=?UTF-8?Q?" or letter['Subject'][0:10] == "=?utf-8?Q?" or letter['Subject'][0:10] == "=?UTF-8?q?":
            sbjs = letter['Subject'].split(" ")
            _mail['Subject'] = ""
            for sbj in sbjs:
                if sbj[-4:-1] == '\r\n':
                    _sbj = sbj[10:-8].replace("=", "%").encode('utf8')
                else:
                    _sbj = sbj[10:-4].replace("=", "%").encode('utf8')
                _mail['Subject'] += urllib.parse.unquote(bytes.decode(_sbj))
        else:
            _mail['Subject'] = letter['Subject']
        _mail['Message-Id'] = letter['Message-Id']
        return _mail # Возвращаем словарь, как и обещали.
    def read_all(start, end, mailbox): # Функция read_all - читает несколько писем от start-ого до end-ого из почтового ящика mailbox. Возвращает список со словарями. /
                                                           # / Read_all function-reads several emails from start to end from the mailbox. Returns a list with dictionaries.
        mail = imaplib.IMAP4_SSL(imap[int(m[0])])
        mail.login(m[1], m[2])
        mail.list()             # Те же функции, что и в read.
        mail.select(mailbox)
        mails = [] # Создаём главный список.
        if start == 'all' and end == 'all': # Если в функции start и end указаны как 'all', это знак к тому, чтобы сохранить ВСЕ ПИСЬМА.
            result, data = mail.uid('search', None, 'ALL')
            for mail_num in range(0, len(data[0].split())): # Наш любимый range.
                _mail = read(mail_num, mailbox) # Используем прошлую функцию read.
                mails.append(_mail)
        else: # Если всё так, как и надо.
            for mail_num in range(start, end+1):
                _mail = read(mail_num, mailbox)
                mails.append(_mail)
        return mails # Возвращаем список.
    try: # Так, наконец-то идём вперёд! Кончились функции.
        print("Вы зашли под почтой "+m[1]+"\n") # Так себе приветствие, но сойдёт.
    except IndexError: # Такая вот непредвиденная защита от дурака.
        print("Вы там чего-то сделали в файле. Удалите файл p.txt.")
        break
    for msg in range(-1, -60, -1):
        Bool = False
        mseeg = read(msg, 'INBOX')
        print("===============================================================================================================================================================================")
        #prstring
        print("["+mseeg['From'][0]+"]: "+mseeg['Subject'])
        msgui = ""
        for mss in mseeg['Message']:
            try:
                mss.index("html")
                Bool = (mss[:3] != "http")
                print(mss[:3])
            except ValueError: pass
            msgui += mss+" "
        #if Bool:
        #    print("HTML-документ. Чтобы скачать его, перейдите к письму.", str(Bool))
        #if not Bool:
        if True:
            if len(msgui) >= 133:
                print(msgui[:132]+"...")
            else:
                print(msgui)
        
    break
