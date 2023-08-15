import matplotlib.pyplot as plt
import numpy as np
import bubble

fig, ax = plt.subplots()
x = np.linspace(0, 2, 20)
x2 = np.linspace(0, 2, 100)
labx = np.random.randint(0, 50, size = 10)  
laby = np.random.randint(0, 50, size = 10)

for x in range(len(labx)):
    bubble.bubblelistsmall(labx)

for x in range(len(laby)):
    bubble.bubblelistsmall(laby)

ax.plot(labx, laby, 'black',label = "Graph")
ax.plot(labx, laby, 'ro', label = "point")
ax.legend()

plt.title("Plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()