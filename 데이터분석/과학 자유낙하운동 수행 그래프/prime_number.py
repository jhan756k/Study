x = 2
listprime = []
flag = None
import time

for n in range(1000):

    for i in range(2,x):  
           if (x % i) == 0:  
               break
    
    else:
        print(x)
        listprime.append(x)

    x += 1

while True:
    ask = int(input())
    print("The "+str(ask)+ " prime number is " +str(listprime[ask - 1]))
