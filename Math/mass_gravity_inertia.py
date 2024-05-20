import math
g = 15.87

def moment(T):
    global g
    M = (2*g*(T**2)) / (4 * (math.pi**2))
    print(round(M, 3))

time = [5.12, 6.37, 7.56, 5.07, 6.76, 7.61, 5.05, 6.64, 7.43]
weight = []
for x in time:
    moment(x/5)
