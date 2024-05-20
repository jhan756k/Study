import math, random

sum = 0.0
pdf = 1.0 / ((4*math.pi)/3)

for i in range(1, 10000001):
  
  rand = random.random() * ((4*math.pi)/3)
  sum += math.sin(rand) / pdf
  
  if i in [10, 100, 1000, 10000, 10000000]:
    print("n = " + str(i) + " : " + str(sum/i))