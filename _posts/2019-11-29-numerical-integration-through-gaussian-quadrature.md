---
layout: post
title:  "Numerical integration using Gaussian quadrature"
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


 It's been quite a while since I've seen Gaussian Quadrature, but it is an important result in numerical analysis with a very elegant proof incorporating many mathematical ideas. It can also be very useful, giving us a technique to numerically integrate polynomials *exactly* so long as they are of a certain degree (precision also will depend on your computer). Here I will explain the proof that gives Gaussian Quadrature its power, and we will see an application with some short Python code.

# Theoretical underpinnings

First we need to introduce what Legendre polynomials are.
Define the following inner product for two polynomials $P_n$ and $P_m$ of degrees $m$ and $n$:

$$(P_n,P_m) = \int_{-1}^{1} P_n(x)P_m(x) dx$$

If we take  $\{1,x,x^2,...,x^n\}$ as a basis for polynomials and apply Gram-Schmidt orthogonalization using this inner product (which I will not do here), we obtain the first n *Legendre polynomials*, which form an basis for polynomials on [-1,1]. It should be noted that the *n*th polynomial has degree n and will have n real roots.

Let's introduce one more theoretical tool, known as a **Lagrange polynomial** (French people enjoy having similar-sounding names). It is often used to create a polynomial which interpolates some number of data points, which is easy to see from its definition: (One can learn more about their various uses [here](https://en.wikipedia.org/wiki/Lagrange_polynomial)):

**Definition:** *Suppose we are given k data points $(x_1,y_1,) \ldots (x_k,y_k)$ Define the* **Lagrange polynomial** *to be:*

$$\mathcal{L}(x) = \sum_{j=0}^k y_j l_j(x)$$

*Where* $$l_j(x) = \prod_{m \neq j}^{k} \frac{x-x_0}{x_j - x_0} \cdots \frac{x-x_k}{x_j - x_k}$$

*The functions $l_j$ are often known as* **Lagrange basis polynomials**.

This definition requires a bit of thought, but it shouldn't be too hard to see how we chose $l_j(x)$. Suppose we want an interpolating polynomial for the two points $(x_0,y_0),(x_1,y_1)=(1/2,4),(3/4,5)$. Then our Lagrange polynomial looks like:

$$L(x) = 4 \cdot \frac{x-3/4}{1/2-3/4} + 5 \cdot \frac{x-1/2}{3/4-1/2}$$

Note that $L(x_0) = y_0 = 4$ but $L(x_1) = y_1 = 5$. Plotting this gives:


<img src="/assets/graph.jpg" width="450" />

A linear function that indeed runs through the two points.

Now we remark a useful property of polynomials using the definition of the Legendre polynomial:

**Remark:** Suppose we have a polynomial $p(x)$ such that $deg(p) \leq n-1$. Then we can say that $p(x)$ satisfies an interpolation of $n$ points $(x_i,p(x_i))$ such that:

 $$\sum_{i=1}^n p(x_i) l_i(x_i)$$

 Where $l_i$ are the Lagrange basis polynomials. Integrating yields:

 $$\int_{-1}^{1} p(x) dx = \int_{-1}^{1} \left( \sum_{i=1}^n p(x_i) l_i(x_i) \right) dx = \sum_{i=1}^n \left( p(x_i) \int_{-1}^{1} l_i(x_i) dx \right)$$

 For future purposes, let's define $w_i := \int_{-1}^{1} l_i(x_i) dx$.

 Now for the main event! We will now prove that on

**Theorem:** *Let x$_0$,x$_1$,...$x_n$ be the roots of the nth Legendre polynomial and $\mathcal{L}_i(x)$ be the $ith$ Lagrange polynomial. Let f be a polynomial of degree 2n - 1. Then the approximation,*

$$\int_{-1}^{1} f(x) dx \approx \sum_{i=0}^{n} w_if(x_i)$$

*is exact.*

*Proof.* We first rewrite f(x) in terms of our new orthogonal basis. Dividing by the nth Legendre polynomial we see that $f(x) = q(x)P_n(x) + r(x)$ where $ deg(q),deg(r) \leq n-1$ (by polynomial division), for some remainder polynomial r(x). Now, we integrate both sides of this equation to obtain:

$$\int_{-1}^{1} f(x) dx = \int_{-1}^{1} P_n(x)q(x)dx  + \int_{-1}^{1}r(x)dx$$

Since q(x) has degree $\leq n-1$ and $P_n(x)$ has degree n and, these two polynomials are orthogonal and the second integral cancels (the inner product chosen now seems much less random).


Now we notice that: $$r(x) = \sum_{i=0}^{n} w_i\mathcal{L}(x_i)$$

Only if r is a polynomial of degree $$\leq n-1$$

# An application


We will now apply Gaussian quadrature for $n=3$, which allows us to integrate polynomials of degree less than $5$. The value for the third Legendre polynomial was simply from [Wikipedia](https://en.wikipedia.org/wiki/Legendre_polynomials), although it could be easily computed using Graham-Schmidt orthogonalization.

Here's our schema:

1. Find the roots of the Legendre polynomial.

2. Create a system of three equations in terms of the three weights.

3. Solve the linear system to find the weights and apply the rule.

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

```

The below code block uses exactly the same technique to integrate the polynomial $x^{11} + x^{10}$, but since it's degree is greater than 8, we get a bad approximation.

```python

#our new function
def g(x):
    return pow(x,11)+pow(x,10)

integrate(g,weights,roots)

```
