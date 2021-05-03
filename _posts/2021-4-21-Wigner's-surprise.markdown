---
layout: post
title:  "Wigner's surprise"
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

Now that I'm headed to grad school, it would be apt to spend some of my time learning about things applicable my area of expertise. Therefore, I've been spending some time learning about random matrix theory (RMT), which made a strong mark on ecology back in the 70s with Robert May's seminal paper showing that a random community would become unstable as it grew past a certain threshold [1]. However, this post will not be about ecology, but rather about a very interesting question that originated in physics.

## Introduction
Our story begins when a young-ish Eugene Wigner was thinking about the statistical properties of energy levels of large nuclei [2]. Basically, neutrons scattering from say, a uranium atom, would produce an energy diagram with lots of peaks. An interesting feature of these peaks, however, is that the probability that they are near each other is very low. In other words, they exhibit a sort of *repulsion*.

In order to model this interesting feature, Wigner posited that we should use statistical methods rather than deterministic ones (a revolution for physics in itself), and represent these energy levels in a matrix where the entries are drawn from a Gaussian distribution. However, to enforce the eigenvalues being real-valued, he decided to symmetrize these matrices. And thus the Gaussian Orthogonal Ensemble (GOE) of matrices was born!

## A derivation

Now, how do we derive a distribution that exhibits these features? Well, apparently Wigner guessed it correctly in front of a crowd [3], but for mere mortals like most of us we need to begin the derivation by asking a fundamental question: for a $2x2$ matrix in the GOE, what is the distribution of the distance between the eigenvalues?



## Sources
[1] May, R. Will a Large Complex System be Stable?. Nature 238, 413–414 (1972). https://doi.org/10.1038/238413a0

[2] Deift, Percy. "Universality for mathematical and physical systems." arXiv preprint math-ph/0603038 (2006).

[3] Livan, G., Novaes, M., & Vivo, P. (2018). Introduction to random matrices: theory and practice (Vol. 26). Berlin: Springer.
