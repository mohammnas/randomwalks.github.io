import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

#The following computes the roots in decimal form
d = np.sqrt(70)
e1 = 35 + 2*d
e2 = 35 -2*d
f = np.sqrt(e1/63)
g = np.sqrt(e2/63)
gn = np.negative(g)
fn = np.negative(f)

#arrays which will be our matrix's rows
ones = np.ones(5)
roots = ([fn,gn,0,g,f])
roots_2 = np.float_power(roots,2)
roots_3 = np.float_power(roots,3)
roots_4 = np.float_power(roots,4)

#A is a matrix containing as rows the roots
A = np.array([ones,roots,roots_2,roots_3,roots_4])
b = np.array([[2],[0],[2/3],[0],[2/5]])
weights = linalg.solve(A,b)

#the function which applies the rule
def integrate(function,weights,roots):
    integral = 0
    for i in range(5):
        integral += weights[i] * f(roots[i])
    print(integral)

#the function to integrate
def f(x):
    return pow(x,8)+42*pow(x,7)

integrate(f,weights,roots)

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
