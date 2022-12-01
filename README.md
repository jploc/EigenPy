# EigenPy
A simple implementation of finding eigenvalues for an adjacency matrix.

iterate() takes an adjacency matrix and the number of desired iterations.  
converge() takes an adjacency matrix and the decimal precision to converge on, and optionally a "True" to truncate output to that precision.  
Both equations return a list of eigenvalues. Values are normalized at each step so the whole list adds to 1 (or 0.999...).

Does not include a method of data input. You can change the adjacency matrix in the code; any size square matrix should work.
