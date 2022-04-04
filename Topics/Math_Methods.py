# The math module has a set of methods and constants.
#
# math.acos()
from gettext import npgettext
import matplotlib.pyplot as plt
import numpy as np
import math
#print (math.acosh(7))
#print (math.acosh(56))
#print (math.acosh(2.45))
# print (math.acosh(1))
plt.style.use('_mpl-gallery')
x = np.linspace (0, 90, 5)
y = np.cos(x)

#plot
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()