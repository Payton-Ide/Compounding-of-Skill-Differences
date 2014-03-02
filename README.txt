1. Use of this program and scipy
	Scipy is needed to run the solution program. Go to http://www.scipy.org/install.html for installation instructions.
2. The binomial module
	For information on the function of binom in scipy.stats, go to http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
3. Explanation of binomial module use
	The binomial cdf from some x value to n is equal to 1 minus the binomial cdf from 0 to x. This function is built into the binom module as binom.sf, and is said to provide greater precision, hence it is used here.		