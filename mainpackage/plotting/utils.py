import numpy as np

# Creates a function based on the input
#// TODO Change function to receive a value after creating the UI
def input_func(function):
    try:
        return eval('lambda x, y: ' + function)
    except:
        if(function != None):
            print("Error: ")
            print(function)
            print(" not valid")
        else:
            print("Error")
        return -1


# Calculates the magnitude of 2D Vectors
def magnitude(x, y):
    return np.sqrt(x**2 + y**2)