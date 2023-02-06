# EigenPy
A simple implementation of finding feature centrality for an adjacency matrix.  
Calculation taken from [DOI: 10.1016/S0364-0213(99)80039-1](https://doi.org/10.1016/S0364-0213(99)80039-1)

iterate() takes an adjacency matrix and the number of desired iterations.  
converge() takes an adjacency matrix and the desired decimal precision to converge on, and optionally a "True" to truncate output to that precision.  
Both equations return a list of centrality values. Values are normalized at each step so the whole list sums to 1 (or 0.999...).

Does not include a method of data input. You can change the adjacency matrix in the code; any size square matrix should work.
