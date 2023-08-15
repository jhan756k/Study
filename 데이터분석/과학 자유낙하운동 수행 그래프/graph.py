import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib import font_manager, rc
from scipy.interpolate import interp1d
from matplotlib.ticker import EngFormatter

font_name = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\NanumGothic.ttf").get_name()
rc('font', family=font_name)
fig, ax = plt.subplots()

x = np.array([0,1,2,3,4,5,6])
y = np.array([0,1,4,9,16,25,36])




f = interp1d(x, y, kind='quadratic')

x_new = np.linspace(x.min(), x.max(),500)
y_smooth=f(x_new)

plt.plot (x_new,y_smooth, label = "그래프", linewidth = 4, color = 'blue')

ax.plot(x, y, 'o', color = "orange" ,markersize = 10, label= "측정값", markeredgecolor = "blue")
ax.legend(loc = "upper left", fontsize = 20)
ax.grid()

ax.set_xticks(x)
#ax.set_yticks(y)



formatter1 = EngFormatter(unit='초')
formatter0 = EngFormatter(unit='m/s')
ax.xaxis.set_major_formatter(formatter1)
ax.yaxis.set_major_formatter(formatter0)


plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.rcParams['axes.unicode_minus'] = False
plt.title("시간 - 속력 그래프 (m / sec)", fontsize = 50)
plt.xlabel("시간 (sec)", fontsize = 40)
plt.ylabel("속력 (m/s)", fontsize = 40)
plt.show()
