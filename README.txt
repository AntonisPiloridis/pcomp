A simple library that calculates all possible permutations (with repetition) from an iterator and a length.

Example(hex to binnary)

import pcomp

print (pcomp.area(range(2),4))

#it returns: 16

print (pcomp.pc(range(2),4))

#it returns: [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]

#[0]=0,[1]=1 .... [15]=f