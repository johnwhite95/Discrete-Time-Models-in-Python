# import libraries
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

# define a class for a finite difference equation model
class Fin_diff:
    
    def __init__(self, func, seed=0, length=0):
        
        self.func = func
        self.length = length
        self.sequence = []
    
    # update the function; that is, take the previous value and run it through the function,
    # storing it as a new value
    def update(self):
        self.seed = self.func(self.seed)
    
    # generate the sequence
    def generate(self, length, seed):
        self.seed = seed
        for i in range(length):
            self.sequence.append(self.seed)
            self.update()
        return(self.sequence)
    
    # determine the equilibrium of the equation by finding the intersection with
    # y = x
    def find_equilibrium(self):
        def g(xy):
            x, y = xy
            z = np.array([y - x, y - self.func(x)])
            return(z)
        return([fsolve(g, [1, 1]), fsolve(g, [-10, -10])])
    
    # plot the sequence values
    def plot(self):
        fig, ax, = plt.subplots()
        ax.plot(np.arange(0, len(self.sequence)), self.sequence, 'go--', alpha = 0.5)
        plt.show()

# an example function
def f(x):
    return(-1*x**3)
        
# example of information provided using the equation's class
my_findiff = Fin_diff(f)
print(my_findiff.generate(10, 0.99))
print(my_findiff.find_equilibrium())
my_findiff.plot()
