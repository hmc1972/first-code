from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
#
#create 3d axes
fig = plt.figure()
ax = plt.axes(projection='3d')
# function for Z Values
def f(x, y): 
    return np.cos(np.sqrt(x ** 2 + y ** 2))
# x and y values
x = np.linspace(1, 10, 10)
y = np.linspace(1, 10, 10) 
#
x, y = np.meshgrid(x, y)
z = f(x, y)
ax = plt.axes(projection = '3d')
ax.plot_wireframe(x, y, z, color = 'red')
# ax.set_title('Learning about 3D plots') 
plt.show()