# 접근 : 완전탐색, Debugging : 

from itertools import *
def main():
    n = int(input())
    a = list(map(int,input().split()))
    permu = list(permutations(a,n))
    li = []
    for p in permu:
        sum = 0
        for j in  range(1,n): 
            sum += abs(p[j]-p[j-1])
            li.append(sum)
    print(max(li))

if __name__ == "__main__":
    main()

'''
6
20 1 15 8 4 10

62
'''