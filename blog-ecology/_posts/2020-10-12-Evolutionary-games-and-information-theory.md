---
layout: post
title:  "Evolutionary games and information theory"
category: ecology
header-includes:
   - \usepackage{tikz}
output:
   pdf_document
toc: true
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

<link href="https://fonts.googleapis.com/css2?family=Amiri&display=swap" rel="stylesheet">

**Contents**
- TOC
{:toc}


In this post, I'd like to elucidate a particularly interesting relationship between two seemingly unrelated fields. This post draws a lot from a paper [1] by John Baez.

## Introduction to information theory
Lately, I've been doing some reading [2] on evolutionary games, while simultaneously taking a course in information theory. To my surprise, there appears to be some overlap between the two fields in the context of ecology and evolutionary biology. This post will explain a few of the most important concepts from information theory before getting into the main topic.

### Shannon entropy

Information theory is all about how certainty can facilitate the acquisition of information. Perhaps the most important idea in information theory is the idea of *entropy*, which was ingeniously defined by Claude Shannon in the 1940's for a probability mass function $p(x)$ as:

$$H(X) = -\sum_{x \in X}log_{2}(x) p(x)$$

There's a definition for continuous distributions, but we needn't worry about that. Now, why is the logarithm base 2? Well, it actually doesn't need to be, but Claude Shannon decided that this would be the best definition for computing the entropy of a message sent using a binary alphabet (which was the [motivation](https://en.wikipedia.org/wiki/Information_theory#Entropy_of_an_information_source) behind information theory). We measure entropy in units of bits under the $\log_2$ definition.

To really appreciate the beauty of this definition, consider the following example. Suppose we are receiving a message that is read in an alphabet of three letters ${A,B,C}$. Now suppose that for sending messages translated from two different spoken languages, the frequency that we receive the letters follow either of two distributions, $p$ and $q$. Define $p$ uniformly such that $p(x)=\frac{1}{3}$ for all $x$, and $q(x)$ such that $q(A) = q(C) = 1/8$ and $q(B)= \frac{6}{8}$ (See Figure 1):


<p align="center">
    <img src="https://raw.githubusercontent.com/mohammnas/randomwalks/master/Images/EGTInfo/fig1.JPG" width="550" />
</p>
*<center> Figure 1: The uniformly distributed (left) and non-uniformly distributed (right) signals. </center>*

Let's compute the entropy of the signal in both languages. For the uniform signal:

$$H(p) = 3 \cdot -\frac{1}{3} \log_2(\frac{1}{3}) \approx 1.58$$

For the other signal:

$$H(q) = -2 \cdot \frac{1}{8} \log_2(\frac{1}{8}) - \frac{6}{8}\log_2(\frac{6}{8}) \approx 1.06$$

Clearly, the nonuniform distribution is lower in entropy. We should expect this, since it is more likely to receive the letter $B$ in the second distribution. For the first distribution, we are extremely uncertain as to what letter we will receive. Thus, as advertised, Shannon's entropy function is measuring the uncertainty in a random variable's outcomes.

### Relative entropy
Now, let's look at an equally important definition, known as *relative entropy*, which is defined for two distributions $p(x)$ and $q(x)$:

$$D(p||q) = \sum_{x\in X} p(x) \log_2(\frac{p(x)}{q(x)})$$

Now, let's see how this definition works by applying it to the previous example. The relative entropy of $X_1$ and $X_2$ is:

$$D(p || q) = \frac{1}{3} \log_2(\frac{8}{3}) + \frac{1}{3} \log_2(\frac{8}{3}) + \frac{1}{3} \log_2(\frac{8}{18}) \approx 0.553$$

What this is actually measuring is how different the two distributions are. Let's suppose we change q such that now $q(A)=q(B)=\frac{1}{10}$ and $q(C) = \frac{8}{10}$. Then
$D(p||q) \approx 0.737$, which makes sense, since the distribution has become "more different" (see Figure 2).


Note that $D(p \vert \vert q) \neq D(q \vert \vert p)$, which means that the relative entropy operator is not a metric.

Also note that relative entropy is sometimes known as the [Kullback-Liebler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence).


<p align="center">
    <img src="https://raw.githubusercontent.com/mohammnas/randomwalks/master/Images/EGTInfo/fig2.JPG" width="550" />
</p>
*<center> Figure 2: The relative entropy measures how different or similar two distributions are. </center>*





## Sources
[1] Baez, John C., and Blake S. Pollard. "Relative entropy in biological systems." Entropy 18.2 (2016): 46.

[2] Friedman, Daniel, and Barry Sinervo. Evolutionary games in natural, social, and virtual worlds. Oxford University Press, 2016.
