from itertools import product
from itertools import combinations_with_replacement
n,m = map(int,input().split())
re_permu = list(combinations_with_replacement(range(1,n+1), m))

re_permu = list(product(range(1,n+1), repeat = m))

for i in re_permu:
    for j in i: 
        print(j, end= ' ')
    print()


'''

3 2

1 2
1 3
2 3
'''