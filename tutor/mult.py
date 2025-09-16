import random

a = "asdf"

while a != "exit":
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    while True:
        a = input("{} X {} = ".format(x,y))
        if a == "exit":
            break
        elif int(a) == x*y:
            print("True")
            break
        elif int(a) != x*y:
            print("False")