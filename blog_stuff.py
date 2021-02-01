import numpy as np
from scipy import linalg
from scipy.stats import entropy
from math import log2

#A is a matrix containing the linear system
A = np.array([[1,1,1],[-np.sqrt(3/5),0,np.sqrt(3/5)],[3/5,0,3/5]])
b = np.array([[2],[0],[2/3]])
weights = linalg.solve(A,b)

#Let's create an array containing the points x_i
roots = np.array([-np.sqrt(3/5),0,np.sqrt(3/5)])

#the function which applies the rule
def integrate(n,function,weights,roots):
    integral = 0
    for i in range(n):
        integral += weights[i] * function(roots[i])
    print(integral)

#the function to integrate
def f(x):
    return pow(x,4)+42*pow(x,3)

def g(x):
    return pow(x,6)+pow(x,5)


integrate(3,g,weights,roots)

#x_0 = (1/2,4), x_1 = (3/4,5)

def lagrange(x):
    L_0 = (x-3/4)/(1/2-3/4)
    L_1 = (x-1/2)/(3/4-1/2)
    return 4*L_0 + 5*L_1

x=np.arange(0,1.2,0.25)
plt.plot(x,lagrange(x))
plt.plot(1/2,4,'.',label=r'$x_0$')
plt.plot(3/4,5,'.',label=r'$x_1$')
plt.xlabel('x')
plt.ylabel('L(x)')
plt.legend()
plt.show()

entropy([1/3,1/3,1/3],[1/10,1/10,8/10],base=2)

1/3*log2(8/3)+1/3*log2(8/3)+1/3*log2(8/18)
