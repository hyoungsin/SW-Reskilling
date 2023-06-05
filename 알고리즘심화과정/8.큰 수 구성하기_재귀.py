# https://www.acmicpc.net/problem/18511

###
#방법1 : itertools (product,repeat)

# import sys
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# from itertools import *

# n,m = map(int,read().rstrip().split())
# a = list(map(int,read().rstrip().split()))

# # print(a)

# res = -1e9 
# for k in range(len(str(n))-1,len(str(n))+1): #에지 막기위해 2자리 3자리 모두 봄 100 일경우 75가 답임 
    
#     # print('k',k)
    
#     perm = list(product(a,repeat = k)) # 중복순열 적용 (223 , 322)

#     # print('perm:',perm)
    
#     for i in perm:
#         s = ''
#         for j in i:
          
#             # print(i)
          
#             s += str(j) 
#         sum = int(s)

#         # print(sum)

#         if sum <= n :
#             res =max(res,sum)
# print(res)

###
#방법2.재귀

# import sys
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# global a, res, N, K

# def recursive(x):
#     global a, res, N, K
#     if N < x:   # N 보다 작거나 같은 자연수 중 가장 큰 수를 찾는 것이 목적. x가 더 크면 위배 예) 1111 (탈출)
#         return
#     # N을 넘는 경우는 이제 없음. 지금까지 나온 수 중 가장 큰 수로 res 갱신
#     res = max(res, x) # 0,1, 11, 111,네자리수탈출, 115,117,네자리수탈출,15,151,157, 17.... 
#     # print(x)
#     for i in a: # [1,5,7]
#         recursive(x * 10 + i)   # 1의 자리에 a 원소 하나 넣어서 위의 작업 반복

# def main():
#     global a, res, N, K
#     N, K = map(int, read().rstrip().split())
#     a = list(map(int, read().rstrip().split()))
#     res = -1e9    # 최댓값 구하는 문제. 자연수 구하는 문제이므로 -1보다는 무조건 큼

#     recursive(0) #0에서 시작 (한자리수 생성)
#     # print(res)

# main()

import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def recursive(x):
    global N,M,A,res
    if x > N :
        return 
    res = max(res,x)

    for i in A: 
        recursive(x*10+i)

def main():
    global N,M,A,res
    N,M = map(int,read().rstrip().split())
    A = list(map(int,read().rstrip().split()))
    A.sort()
    
    print(N,M,A)

    res = -1e9
    recursive(0)

    print(res)

main()

'''
657 3
1 5 7

577

Edge

1000 3
1 5 7



문제
N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오. K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.

예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.

입력
첫째 줄에 N, K의 원소의 개수가 공백을 기준으로 구분되어 자연수로 주어진다. (10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3) 둘째 줄에 K의 원소들이 공백을 기준으로 구분되어 주어진다. 각 원소는 1부터 9까지의 자연수다.

단, 항상 K의 원소로만 구성된 N보다 작거나 같은 자연수를 만들 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.'''