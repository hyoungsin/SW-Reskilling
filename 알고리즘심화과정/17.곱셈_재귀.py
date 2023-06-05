# https://www.acmicpc.net/problem/1629

import sys
sys.setrecursionlimit(10**6)

n,m,k = map(int,input().split())

def recursion(n,m):
    if m == 0: 
        return 1

    elif m % 2 == 0:
        res = recursion(n,m//2)
        return res **2 % k

    else : 
        res = recursion(n,(m-1)//2)
        return n*res**2 % k

# recursion(n,m)
print(recursion(n,m))
# print((10**11)%k)

'''
10 11 12

4

문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
'''