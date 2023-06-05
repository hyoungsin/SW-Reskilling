######################
#1.거리 배열 초기화 (N+1(패딩), 노드, 본인 --> 본인 : 0)
#2.거리 정보 갱신 (k노드 개수많큼)

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy

def main():
    global N,M,visited
    N,M = map(int,read().rstrip().split())
    visited = [[1e9 for i in range(N+1)]for j in range(N+1)]

    for i in range(N+1):
        for j in range(N):
            visited[i][i] = 0 

    for i in range(M):
        r,c,d = map(int,read().rstrip().split())

        for j in range(M):
            visited[r][c] = d
            visited[c][r] = d # 역순도 거리동일정보 동일 (문제를 잘읽자)

    for k in range(1,N+1): # 1 ~ 5까지 
        for i in range(1,N+1):
            for j in range(1,N+1):# [i][j] = 거리, k 본인이면 0+0

                # print('i,j,k',i,j,k)
                visited[i][j]  = min(visited[i][j],visited[i][k]+visited[k][j]) 
    
                # print('i,j,k,ij,ik,kj:',i,j,k,visited[i][j],visited[i][k],visited[k][j])

    # print(visited)

    res = 1e9
    for i in range(1,N+1):
        max_row = -1e9
        for j in range(1,N+1):
            if visited[i][j] != 0:
                max_row = max(visited[i][j],max_row)
        res = min(res,max_row)
    
    print(res)

main()

'''
5 7
1 2 5
3 2 14
2 4 5
1 3 10
4 3 15
5 4 15
3 5 8

15

5 : 물류창고 개수
7 : 공장에서 물류창고까지 거리 정보 (Start (3) - End (2) - 거리(5))






'''