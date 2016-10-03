<h2>Nonparametric Density Estimation via Random Feature</h2>

This module has 4 components:

<ol>

<li> <b>Objective Approximation Module:</b>

<ul>
<li>goal: sampling uniformly from data domain to construct a surrogate objective.
</li>

<li>input:  
<pre>
(i)  data file (for getting dim and the range of each dim). 
(ii) m: number of samples for the contrastive data set.
</pre>
</li>

<li>output: the "contrastive" data file that follows uniform distribution over the L-infty ball.
</li>
</ul>

</li>

<li> <b>Random Feature Module:</b>

<ul>
<li> goal: generate features \phi(x) for each sample x. </li>

<li> input: raw data file and its contrastive data file. </li>

<li> output: 
<pre>
(i)  random feature files for data and contrastive data.
(ii) number of random features (D). 
</pre>
</li>
</ul>

</li>

<li> <b>Density Estimation Module:</b>

<ul>	
<li>goal: estimate the function f(x)=<w, \phi(x)> by solving: <br>
<pre>
	min_{w} [ln \sum_{i\in contract} exp( <w,\phi(x_i)> ) ] - [ (1/N)\sum_{i\in data} <w,\phi(x_i)> ]
	s.t.	|w_j| <= C/D
</pre>
</li>
<li>
input:  
<pre>
(i)  data file.
(ii) contrastive data file.
(iii) C.
</pre>
<li>
output: model file (w)
</li>
</ul>

</li>

<li> <b>(Log) Likelihood Estimation Module:</b>

<ul>
<li>
input:	
<pre>
(i)   a (test) data file.
(ii)  a (test) contrastive data file.
(iii) a model file.
</pre>
</li>
<li>
output:	average log likelihood.
</li>
</ul>

</li>

</ol>
