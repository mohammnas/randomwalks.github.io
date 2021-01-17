---
layout: post
title:  "Evolutionary games and information theory"
category: ecology
header-includes:
   - \usepackage{tikz}
output:
   pdf_document
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

In this post, I'd like to elucidate a particularly interesting relationship between two seemingly unrelated fields. This post draws a lot from a paper$^1$ by John Baez

Lately, I've been doing some [reading](https://www.amazon.com/Evolutionary-Natural-Social-Virtual-Worlds-ebook/dp/B01GI5EUYC) on evolutionary games, while simultaneously taking a course in information theory. To my surprise, there appears to be some overlap between the two fields in the context of ecology and evolutionary biology. This post will explain a few of the most important concepts from information theory before getting into the main topic.

Information theory is all about how certainty can facilitate the acquisition of information. Perhaps the most important idea in information theory is the idea of *entropy*, which was ingeniously defined by Claude Shannon in the 1940's as:

$$H(X) = -\sum_{x \in X}log_{2}(x) p(x)$$

For a *discrete* random variable $X$ (there's a definition for continuous distributions, but we needn't worry about that). Now, why is the logarithm base 2? Well, it actually doesn't need to be, but Claude Shannon decided that this would be the best definition for computing the entropy of a message sent using a binary alphabet (which was the [motivation](https://en.wikipedia.org/wiki/Information_theory#Entropy_of_an_information_source) behind information theory).

To lend some intuition to this definition, consider the following example. Suppose we are receiving a message that is read in an alphabet of three letters ${A,B,C}$. Now suppose that the frequency that we receive the letters is distributed in two different ways, either uniformly or as $P(A)=P(C)= \frac{1}{8},P(B)= \frac{6}{8}$ (See Figure 1):



<p align="center">
    <img src="https://raw.githubusercontent.com/mohammnas/randomwalks/master/Images/EGTInfo/fig1.JPG" width="550" />
</p>
*<center> Figure 1: Two messages being sent using the same alphabet but with different distributions. </center>*

#### Sources
