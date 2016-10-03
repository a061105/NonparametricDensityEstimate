This module has 3 components:

<ol>

<li> Objective Approximation Module: 

<ul>
<li>goal: sampling uniformly from data domain to construct a surrogate objective.
</li>

<li>input:  (i)  data file (for getting dim and the range of each dim). <br>
	    (ii) m: number of samples for the contrastive data set.
</li>

<li>output: the "contrastive" data file that follows uniform distribution over the L-infty ball.
</li>
</ul>

</li>

<li> Random Feature Module:

<ul>
<li> goal: generate features \phi(x) for each sample x. </li>

<li> input: raw data file and its contrastive data file. </li>

<li> output: (i)  random feature files for data and contrastive data.<br>
	     (ii) number of random features (D). 
</li>
</ul>

</li>

<li> Density Estimation Module:

<ul>	
<li>goal: estimate the function f(x)=<w, \phi(x)> by solving: <br>
<pre>
	min_{w} [ln \sum_{i\in contract} exp( <w,\phi(x_i)> ) ] - [ (1/N)\sum_{i\in data} <w,\phi(x_i)> ]
	s.t.	|w_j| <= C/D
</pre>
</li>
<li>
input:  (i)  data file. <br>
	(ii) contrastive data file. <br>
	(iii) C.
<li>
<li>
output: model file (w)
</li>
</ul>

</li>

<li> (Log) Likelihood Estimation Module:

<ul>
<li>
input:	(i)   a (test) data file <br>
	(ii)  a (test) contrastive data file. <br>
	(iii) a model file.
</li>
<li>
output:	average log likelihood.
</li>
</ul>

</li>

</ol>
