def yaksu_num(x):
    answer = 0
    for a in range(1, x+1):
        if x % a == 0:
            answer += 1
                
    return answer

def sosu(a):
    if yaksu_num(a)==2:
        return True
    else: 
        return False

'''
소수 --> 1과 자기 자신만을 약수로 가지는 수

6 --> 완전수
1 2 3 
'''

# 최대공약수 최소공배수
a = 12
b = 16

def gcm(x, y):
    gcm1 = 0
    for a in range(1, min(x,y)):
        if x % a == 0 and y % a == 0:
            gcm1 = a
    return gcm1

def lcm(x, y):
    for a in range(max(x,y), x*y):
        if a % x == 0 and a % y == 0:
            return a


# t라는 어떤 숫자의 모든 약수를 구하는 프로그램

t = 6
ans = 0
yaksu = []

for i in range(1, t+1):
    if t % i == 0:
        ans += 1
        yaksu.append(i)

# t라는 변수는 완전수인가?

a = 0
for i in range(0, ans-1):
    a += yaksu[i]

if a == t:
    print("yes")
else:
    print("no")