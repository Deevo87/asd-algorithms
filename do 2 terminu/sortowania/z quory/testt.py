from math import ceil
from math import log

#print(ceil(log(20, 2)))
m = 7
k = 2
S = (((2*k) + (m-1))//2)*m
last = int((2*S/m)-k)
print(S, last)