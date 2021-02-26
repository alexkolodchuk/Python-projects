from time import sleep
def collatz(n):
    k = []
    loop = True
    k.append(n)
    while loop:
    	if n%2 == 0:
    		n = n/2
    	elif n == 1:
    		loop = False
    	else:
    		n = 3*n+1
    	k.append(int(n))
    print(k)

i = 10
while True:
    print("Number: "+str(i))
    sleep(0.1)
    collatz(i)
    i*=10
