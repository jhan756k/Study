import random, math, matplotlib.pyplot as plt

def expsample(m):
    temp = random.random()
    return -1 * math.log(temp) / m

# graph the exponential distribution
def graph(m, numpoints):
    data = []
    for i in range(numpoints):
        data.append(expsample(m))
    plt.hist(data, bins=100)
    plt.show()

graph(5.0, 1000000)
