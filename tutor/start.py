'''
1. 입력
a = input("숫자를 입력하세요: ")
a, b = input().split()

string (str): "f", "asdfasd" 
integer (int): 2, 3 
boolean (bool): True, False 
list: []

a = int(a)

2. 출력
print(123, end="")

a = 23
b = 4
print(f"{a} 곱하기 {b} 는 {a*b} 입니다")

3. 조건문
and, or, not
결국 if문 안에는 True False 둘중 하나로 바뀜

if, elif, else --> else에는 조건없음

4. 반복문
for, while
break

이중 반복문

for a in range(6, 1, -1):
    for b in range(a-1, 0, -1):
        print("*", end="")
    print()

5. 배열 (리스트)
a = [1, 2, 3, 4]
a.append(5)
a.pop(1) --> 1은 인덱스 번호
print(a[2])

6. 함수

a = 2
def add(a, b):
    print(a+b)

x = 10

def add(a, b, c):
    print(a+b+c)
    print(x) --> 마법상자 바깥 (오류 생김)

add(3, 5, x)
add(3, 5, 10)

a = 7
b = 6

def add(x, y):
    return (x + y)


print("juwon's age is : " + str(add(a, b)))
'''

# a = []
# max_num = 0
# max_i = 0

# for i in range(1,10):
#     x = int(input())
#     if x > max_num:
#         max_num = x
#         max_i = i
# print(max_num)
# print(max_i)


# 1 1 2 3 5 8 13 21 34 55.. 

def fib(n):
    b = [1, 1]
    for a in range(1, n-1):
        b.append(b[-1] + b[-2])
    print(b)
    return b[-1]
    
def newfib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return newfib(n-1) + newfib(n-2)

a = [[2, 55, 62, 5, 12, 56],
     [23, 67, 1, 21, 654, -12],
     [5, 34, 23, 123, 12, 743],
     [23, 243, 56, 786, 22, 1]]

# a배열에서 가장 큰수를 찾고, 그 수의 인덱스 번호 찾기

c = 0
ind = [0, 0]

for b in range(len(a)):
    for d in range(len(a[0])):
        if c < a[b][d]:
            c = a[b][d]
            ind = [b,d]

print(c)
print(ind)