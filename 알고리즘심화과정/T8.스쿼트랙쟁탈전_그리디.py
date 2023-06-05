#1.배열구성
#2.끝나는 시간 기준 정렬 
#3.i[1]으로 update 후 cnt 

import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(read().rstrip())
A = []
for i in range(N):
    A.append(list(map(int,read().rstrip().split())))

# print(A)

A = sorted(A,key = lambda x : (x[1],x[0]), reverse=False)

# print(A)

res = -1e9 
cnt = 0 
for i in A: 
    if i[0] >= res: 
        res = max(res,i[1])
        cnt += 1

print(cnt)

