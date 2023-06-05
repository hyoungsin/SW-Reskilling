
from itertools import *
n,m = map(int,input().split())
permu = permutations(range(1,n+1),m)
for i in permu:
    for j in i: 
        print(j, end= ' ')
    print()

'''
3 2

1 2
1 3
2 1
2 3
3 1
3 2

'''