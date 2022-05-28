import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import utils

class PlotClass(object):
    def __init__(self, range=10, step=1.0, arrow_norm_fac=0.25, grid=False):
        self.arrow_norm_fac = arrow_norm_fac
        self.grid = grid


        points_coords = np.arange(-range, range + step, step)
        self.points = np.array(np.meshgrid(points_coords, points_coords))


        # Creating subplot to later set spines and colors
        self.fig, self.ax = plt.subplots()

        # Setting Spines
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        # Fixing proportions
        self.ax.axis('equal')


    def plot(self, x, y):
        func_x = utils.input_func(x)
        func_y = utils.input_func(y)
        vfunc_x = np.vectorize(func_x)
        vfunc_y = np.vectorize(func_y)

        # Calculating Vectors
        
        vec_x = vfunc_x(self.points[0], self.points[1])
        vec_y = vfunc_y(self.points[0], self.points[1])
        vmagnitude = np.vectorize(utils.magnitude)
        magnitude_values = vmagnitude(vec_x, vec_y)

        # Setting Colormap
        min_color = np.min(magnitude_values)
        max_color = np.max(magnitude_values)
        cmap = mpl.cm.get_cmap('plasma', 500)
        norm = mpl.colors.Normalize(min_color, max_color)

        # Control Arrow sizes
        scales = np.power(magnitude_values, self.arrow_norm_fac)/np.power(max_color, self.arrow_norm_fac)


        # Plotting Vectors
        self.ax.quiver(self.points[0], self.points[1], (vec_x*scales)/magnitude_values, (vec_y*scales)/magnitude_values, norm(magnitude_values), 
                    units='xy', scale_units='xy', 
                    scale = 1/self.step)

        # Setting Colorbar
        self.fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=self.ax)

        if self.grid == True:    
            self.ax.grid(True, which='both')
        plt.show()



if __name__ == '__main__':
    plot_instance = PlotClass()
    
    plot_instance.plot(input('Enter X function: '), input('Enter Y function: '))