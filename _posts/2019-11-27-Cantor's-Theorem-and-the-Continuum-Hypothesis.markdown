---
layout: post
title:  "Cantor's theorem and the Continuum Hypothesis"
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

My first post! This will be a simple and short exposition; hopefully future posts will be more detailed.

Here is a theorem I learned in my course on real analysis which is an extraordinary result that has an equally extraordinary proof. I remember my professor telling our class that this proof would make our heads spin, but I believe there is just unfortunate notation which makes it confusing at a first glance. I will also talk about some implications of this theorem.

**Theorem (Cantor's theorem):** *Consider a set A and its power set $$\mathcal{P}(A)$$. There is no surjection $$f:A \rightarrow \mathcal{P}(A) $$.*

*Proof.* To prove this, let us construct a set S = $$\{x \in A : x \notin f(x)\}$$ and assume that f is surjective. If this is the case, then there exists x $$\in$$ A such that f(x) = S. The main cause of confusion in understanding this proof is the failure in remembering that f(x) is a set and not a single number as usual, and that we have f(x) $$\in \mathcal{P}(A)$$.

If it is in fact the case that f(x) = S for any x then we would require that x $$\in f(x) \Rightarrow x \in S$$ which further implies x $$\notin$$ f(x) by the clever choice of S; a contradiction that x $\in f(x)$. Conversely, it is possible that x $$\notin$$ f(x). Then x $$\notin S$$, but by our construction of S, this means that x $$\in$$ f(x); a contradiction of x $$\notin$$ f(x). Thus, in either case, we have $$f(x) \notin S$$ and $$f(x) \in S$$, which is absurd, meaning such a function f could not exist. $\blacksquare$

The reason this proof is so revolutionary is the clever choice of a set outside the range of any function from a set to its power set. This is a great illustration of a *diagonal argument* which is often used for showing the cardinality of one set to be greater than another, and is even used in the proof of Russell's Paradox. This is also a great example of the machiavellian nature of mathematics; you must be willing to construct any object so long as it proves your point.

This proof also implies that larger and larger sets can now be created. Every math student has seen the proof that the cardinality of the reals is greater than that of the integers, but a question that seldom comes up (at least in the undergraduate years) is whether or not there are cardinalities between $$\vert \mathbb{R} \vert$$ and $$\vert \mathbb{N} \vert$$, which is a problem known as the *Continuum Hypothesis*.

Stating this problem mathematically, let $$\beth_0$$ represent the cardinality of a countably infinite set. Now we recursively define $$\mathcal{P}(\beth_\alpha) = \beth_{\alpha + 1}$$ (where $$\alpha$$ is an ordinal), where we now know that $$\beth_{\alpha + 1}$$ is greater than $$\beth_{\alpha}$$ by Cantor's theorem. Another way of creating bigger sets is by defining the cardinal $$\aleph_0$$ which is the cardinality of the union of all finite well-ordered sets, and then $$\aleph_1$$ which is of the cardinality of the union of ordinals of cardinality $$\aleph_0$$ (thus creating an uncountable set), and we create $$\aleph_2$$ similarly and so on. Each $$\aleph_\alpha$$ ranges over all infinite cardinals while $\beth_\alpha$ only ranges over cardinalities of successive power sets of the initial $$\beth_0$$; the big question is whether or not $$\aleph_1 = \beth_1$$. This is the Continuum Hypothesis and amazingly enough, it has been shown to be impossible to decide whether or not this is true in ZFC ([Reference](https://en.wikipedia.org/wiki/Continuum_hypothesis)).
