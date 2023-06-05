
# 정렬 
#1.sort하면 순서바뀐거 상관없음
#2.각 idx에 첫번째 idx빼면 

import sys
read = sys.stdin.readline
N,M = map(int,read().rstrip().split())
A1 = list(map(int,read().rstrip().split()))
A2 = list(map(int,read().rstrip().split()))

A2.sort()
res_A2 = list(map(lambda x : x - A2[0],A2))
# print(res_A2)

cnt = 0 
for i in range(N-M+1):
    res_A1 = A1[i:i+M]
    res_A1.sort()
    # print(res_A1)
    res_A1 = list(map(lambda x: x- res_A1[0], res_A1))
    # print(res_A1)
    if res_A2 == res_A1:
        cnt +=1

print(cnt)


'''
12 3
2 4 8 5 8 4 8 5 9 6 3 2
4 8 5

5
'''
