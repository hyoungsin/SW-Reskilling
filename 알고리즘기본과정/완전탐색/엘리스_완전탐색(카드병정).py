# 접근) main() : itertools, combinations, i&j , 디버깅) 

from itertools import * 
def main():
    n,m = map(int,input().split())
    comb = combinations(range(1,n+1),m)
    for i in comb:
        for j in i: 
            print(j, end = ' ')
        print()

if __name__ == "__main__":
    main()

'''
4 2

1 2
1 3
1 4
2 3
2 4
3 4
'''