n1 = 1
n2 = 1
print("1 - 1")
print("2 - 1")
fibo = [1, 1]
for i in range(1, 99999):
    n3 = n1+n2
    print(i+2, "-", n3)
    fibo.append(n3)
    n1 = n2
    n2 = n3
    
