#Name: Bibaswan Roy
#Link: https://github.com/Darkos19/Hacktoberfest2021-3.git



import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 1000)
y = np.sin(x)



ax = plt.axes()  #object

#making axes
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.plot(x, y)
plt.show()

plt.savefig('Example.png')