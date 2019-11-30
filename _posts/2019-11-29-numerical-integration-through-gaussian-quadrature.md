---
layout: post
title:  "Numerical integration through Gaussian quadrature"
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
  }
});
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

**UNFINISHED**

Here is some Python code which computes the integral $$\int_{-1}^{1} x^{8} + 42x^{7} dx$$ using
Gaussian quadrature. The value for the fifth Legendre polynomial was simply from [Wikipedia](https://en.wikipedia.org/wiki/Legendre_polynomials), although it could be easily computed using Graham-Schmidt orthogonalization (I don't have enough time on my hands to write it all out!)

We import the library Numpy and the "linalg" sub-package from the Scipy library; the latter of which
is very useful for solving linear systems.

```python

import numpy as np
from scipy import linalg

```
First we compute the roots of the fifth Legendre polynomial, since we are integrating
a polynomial of degree 8 (we are only allowed to integrate polynomials of degree $$\leq 2n - 1$$)

```python
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

#the function for part c)
def f(x):
    return pow(x,8)+42*pow(x,7)

#the function for part d)
def g(x):
    return pow(x,11)+pow(x,10)

#computes the integral using gaussian quadrature
def integrate(f,a,b):
    integral = 0
    for i in range(5):
        integral += a[i] * f(b[i])
    print(integral)

integrate(f,weights,roots)
integrate(g,weights,roots)

print(roots)
```
