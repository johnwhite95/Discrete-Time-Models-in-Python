# import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

""" 
a few example models
"""
# malthusian model
def malthus(F, d, x): return((1 + F - d) * x)

# discrete predator-prey
def predator_prey(K, r, s, u, v, p, q): return([p * (1 + r * (1 - p / K)) - s * p * q, (1 - u) * q + v * p * q])

# discrete SIR model
def sir(alpha, gamma, s, i, r): return([s - alpha*s*i, i + alpha*s*i - gamma*i, r + gamma*i])

"""
Classes for analysis of finite-difference methods:
FDM - for single systems
FDM2 - for double systems
FDM3 - for triple systems
"""
class FDM:

    def __init__(self, x0, func, *variables):

        self.x, self.func, *self.variables = x0, func, *variables
        
    def update(self):

        self.x = self.func(*self.variables, self.x)
        
    def generate(self, n, plot = 0):

        sequence = []
        for i in range(n):
            sequence.append(self.x)
            self.update()
        if (plot == "plots:true"):
            fig, ax, = plt.subplots()
            ax.plot(range(n), sequence, 'go--', alpha = 0.5)
            plt.show()
        return (np.array(sequence))

class FDM2:
    
    def __init__(self, x0, y0, func, *variables):
        
        self.x, self.y, self.func, *self.variables = x0, y0, func, *variables
        
    def update(self):
        self.x, self.y = self.func(*self.variables, self.x, self.y)
        
    def generate(self, n, *arguments):
        
        sequence = []
        
        for i in range(n):
            sequence.append([self.x, self.y])
            self.update()
        if ("plot" in arguments):
            fig, ax, = plt.subplots()
            ax.plot(range(n), sequence, 'go--', alpha = 0.5)
            plt.show()
            
        sequence = np.array(sequence)
        if ("phase" in arguments):
            xp = sequence[0:len(sequence), 0:1]
            yp = sequence[0:len(sequence), 1:2]
            plt.plot(xp, yp, 'go--', alpha = 0.5)
            plt.show()
        
        return(sequence)

class FDM3:
    
    def __init__(self, x0, y0, z0, func, *variables):
        
        self.x, self.y, self.z, self.func, *self.variables = x0, y0, z0, func, *variables
        self.x2, self.y2, self.z2, self.func2, *self.variables2 = x0, y0, z0, func, *variables
            
    def update(self):
        self.x, self.y, self.z = self.func(*self.variables, self.x, self.y, self.z)
        self.x2, self.y2, self.z2 = self.func(*self.variables, self.x2, self.y2, self.z2)
        
    def generate(self, n, *arguments):
        
        sequence = []
        
        for cnt in range(n):
            sequence.append([self.x, self.y, self.z])
            self.update()
        if ("plot" in arguments):
            fig, ax, = plt.subplots()
            ax.plot(range(n), sequence, 'go--', alpha = 0.5)
            plt.show()
            
        sequence = np.array(sequence)
        
        if ("phase" in arguments):
            xp = sequence[0:len(sequence), 0:1]
            yp = sequence[0:len(sequence), 1:2]
            zp = sequence[0:len(sequence), 2:3]
            plt.plot(xp, yp, 'go--', alpha = 0.5)
            plt.show()
            plt.plot(yp, zp, 'go--', alpha = 0.5)
            plt.show()
            plt.plot(xp, zp, 'go--', alpha = 0.5)
            plt.show()
            
        return(sequence)

pred_prey = FDM2(1.1, 0.4, predator_prey, 1, 1.3, 0.5, 0.7, 1.6)
print(pred_prey.generate(80, "plot", "phase"))
