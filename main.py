from calendar import c
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def magnitude(x, y):
    return np.sqrt(x**2 + y**2)

#Plot Functions
def test_func(x, y):
    if(x == 0 and y ==0):
        return 0
    return -y/(x**2 +y**2)
    #return x*y

def test_func2(x, y):
    if(x == 0 and y ==0):
        return 0
    return x/(x**2 +y**2)
    #return x**2

func_x = np.vectorize(test_func)
func_y = np.vectorize(test_func2)


#Values to compute
range = 2.5
step = 0.5
size = np.arange(-range, range + step, step)

#Creating subplot to later set spines and colors
fig, ax = plt.subplots()


#!Setting Colormap
min_color = 0
max_color = 5

cmap = mpl.cm.get_cmap('plasma', 50000)
norm = mpl.colors.Normalize(min_color, max_color)


#PLotting Vectors

points = np.array(np.meshgrid(size, size))
print(points)

for x in size:
    for y in size:
        vec_x = func_x(x, y)
        vec_y = func_y(x, y)
        norm_mag = norm(magnitude(vec_x, vec_y))
        ax.quiver(x, y, vec_x, vec_y, units='xy',scale_units='xy', scale=5, color=cmap(norm_mag))


#Setting Spines
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)


#Fixing proportions
ax.axis('equal')

#ax.grid(True, which='both')


plt.show()
