
from itertools import *
n,m = map(int,input().split())
comb = combinations(range(1,n+1),m)
for i in comb:
    for j in i: 
        print(j, end= ' ')
    print()


'''

3 2

1 2
1 3
2 3
'''