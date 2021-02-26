import requests, requests.exceptions
while True:
    i = input("Название статьи: ").replace(" ", "_")
    url = "https://ru.wikipedia.org/wiki/"+i
    try:
        send = requests.get(url) ###
    except requests.exceptions.ConnectionError:
        print("CONNECTION FAILED: FATAL ERROR. BAD FILE. CONTINUE.") # Сообщение кратенькое.
        continue
    if str(send)!="<Response [404]>":
        for P in send.text.split("<p>"):
            for p in P.split("</p>"):
                if p.find("<!DOCTYPE html>")==0 or len(p.split("\n"))>=60 or p.find("<div")!=-1 or p.find("<a href=\"/wiki/")==0:
                    pass
                else:
                    #print(p)
                    pes = []
                    _p = ""
                    for _ in p.split("<a "):
                        for __ in _.split("/a>"):
                            pes.append(__)
                    #print(pes)
                    for ps in range(0, len(pes)):
                        if pes[ps].find("href=")==0:
                            _p+=pes[ps].split("\"")[-1][1:-1]
                        else:
                            _p+=pes[ps]
                    __p = ""
                    for _ in _p.split("<i>"):
                        for __ in _.split("</i>"):
                            for ___ in __.split("<b>"):
                                for ____ in ___.split("</b>"):
                                    __p+=____
                    __p.replace("&#160;", " ")
                    while __p.find("<sup")!=-1:
                        start = __p.find("<sup")
                        end = __p.find("</sup>")+6
                        __p = __p[0:start]+__p[end:-1]
                    print(__p) #_p #pes
        
#.replace("=", "%").encode('utf8')
