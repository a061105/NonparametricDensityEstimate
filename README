This module has 3 components:

1. Objective Approximation Module: 

goal: sampling uniformly from data domain to construct a surrogate objective.

input:  (i)  data file (for getting dim and the range of each dim).
	(ii) m: number of samples for the contrastive data set.

output: the "contrastive" data file that follows uniform distribution over the L_{\infty} ball.

2. Random Feature Module:

goal: generate features \phi(x) for each sample x.

input: raw data file and its contrastive data file.

output: (i)  random feature files for data and contrastive data.
	(ii) number of random features (D).

3. Density Estimation Module:
	
goal: estimate the function f(x)=<w, \phi(x)> by solving:

	min_{w} [ln \sum_{i\in contract} exp( <w,\phi(x_i)> ) ] - [ (1/N)\sum_{i\in data} <w,\phi(x_i)> ]
	s.t.	|w_j| <= C/D

input:  (i)  data file.
	(ii) contrastive data file.
	(iii) C.

output: model file (w)

4. (Log) Likelihood Estimation Module:

input:	(i)   a (test) data file
	(ii)  a (test) contrastive data file.
	(iii) a model file.

output:	average log likelihood.
