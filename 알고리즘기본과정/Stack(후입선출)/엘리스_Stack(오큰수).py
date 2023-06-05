
# Stack활용
# 1.배열초기화(stack)
# 2.미반환 값 초기화 (-1배열)
# 3.역순으로 접근 (N-1,-1,-1)
# 4.조건값 반환 / 아니면 pop후 while탐색
# 5.stack append 

# import sys
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# from collections import deque
# import copy
# from itertools import *

# def main():
#     N = int(read().rstrip())
#     A = list(map(int,read().rstrip().split()))
#     res = [-1 for i in range(N)] #값이 없는 건을 -1로 처리 도구 

#     stack = []
#     for i in range(N-1,-1,-1): # 배열은 역순으로 탐색 
#         while stack: # stack에 숫자가 있으면 
#             if A[i] < stack[-1]:# A[i]보다 숫자가 크면(오큰수)
#                 res[i] = stack[-1]
#                 break
#             else: #오큰수가 아니면 빼고 전에 입력숫자 확인 
#                 stack.pop()

#         stack.append(A[i]) #해당 index 다음숫자부터만 검토대상

#     print(*res)

# main()                    

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy
from itertools import *

def main():
    N = int(read().rstrip())
    A = list(map(int,read().rstrip().split()))
    res = [-1 for i in range(N)] #값이 없는 건을 -1로 처리배열
    
    for i in range(N): # 0,1,2,3 
        stack = [] # idx 완료 되면 stack초기화 
        cnt = 0 # while돌때마다 cnt update 
        while cnt < N-i-1: #i : 0,1,2,3 , cnt : 3(3번),2(2번),1(1번),0(0번)
            stack.append(A[cnt+1]) # 1,2,3
            if A[i] < stack[-1]:# A[i]보다 숫자가 크면(오큰수) update
                res[i] = stack[-1]
                break

            else: #오큰수가 아니면 pop하고 cnt추가 
                stack.pop()
                cnt += 1

    print(*res)

main()    


'''
4
3 5 2 7

5 7 7 -1

4
9 5 4 8

-1 8 8 -1

문제
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 
수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 
그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

출력
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

'''