import random

while True:
    x = random.randint(1, 1000)
    while True:
        a = int(input("숫자를 맞춰보세요: "))
        if a < x:
            print("정해진 숫자는 {}보다 큽니다".format(a))
        elif a > x:
            print("정해진 숫자는 {}보다 작습니다".format(a))
        else:
            print("맞습니다")
            break
