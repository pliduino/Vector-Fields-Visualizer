from calendar import c
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Calculates the magnitude of 2D Vectors
def magnitude(x, y):
    return np.sqrt(x**2 + y**2)


#Plot Functions
def test_func(x, y):
    if(x == 0 and y == 0):
        return 0
    return -y/(x**2 +y**2)
    # return x*y

def test_func2(x, y):
    if(x == 0 and y == 0):
        return 0
    return x/(x**2 +y**2)
    # return x**2

func_x = np.vectorize(test_func)
func_y = np.vectorize(test_func2)

#Values to compute
range = 5
step = 0.25
size = np.arange(-range, range + step, step)

#Creating subplot to later set spines and colors
fig, ax = plt.subplots()


#Calculating Vectors
points = np.array(np.meshgrid(size, size))
vec_x = func_x(points[0], points[1])
vec_y = func_y(points[0], points[1])
vmagnitude = np.vectorize(magnitude)
magnitude_values = vmagnitude(vec_x, vec_y)

#Setting Colormap
min_color = np.min(magnitude_values)
max_color = np.max(magnitude_values)
cmap = mpl.cm.get_cmap('plasma', 500)
norm = mpl.colors.Normalize(min_color, max_color)


#Plotting Vectors
ax.quiver(points[0], points[1], vec_x, vec_y, norm(magnitude_values), units='xy', scale_units='xy', scale=max_color/step)


#Setting Spines
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#Setting Colorbar
fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)


#Fixing proportions
ax.axis('equal')

#ax.grid(True, which='both')


plt.show()
