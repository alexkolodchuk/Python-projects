from winsound import *
from time import *
from random import *

for i in range(0, 100):
    Beep(randint(60, 6000), 40)

kolvo = int(input("Кол-во элементов: "))
a = []
for k in range(0, kolvo):
    f = float(input("Элемент №"+str(k)+": "))
    a.append(f)
print("Приготовьтесь...")
sleep(2)
print("Начинаю визуализацию...")
print("\n", end="")
for i in range(0, kolvo-1):
    for j in range(kolvo-2, i, -1):
        if a[j]<a[j+1]:
            c=a[j+1]
            a[j+1]=a[j]
            a[j]=c
            Beep(j*100, 40)
            Beep((j+1)*100, 40)
            #print(j, end=" ")
print(a)
#Beep(1000, 150)
