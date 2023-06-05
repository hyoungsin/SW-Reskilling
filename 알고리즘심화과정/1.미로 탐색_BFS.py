# https://www.acmicpc.net/problem/2178 (split,nr/nc, a,visited조건,) 

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]
def bfs(): 
    global R,C,A,visited

    #3. Q 구성

    Q = deque([(0,0)])
    visited[0][0] = 1 

    #4. Q 탐색 

    while len(Q) > 0 :
        r,c = Q.popleft()
        if r == R-1 and c == C-1:
            return 
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >=C or visited[nr][nc] != 0 or A[nr][nc] == 0 :
                continue

            #5. 도착지점 거리 산출 
            
            visited[nr][nc] = visited[r][c] + 1 
            Q.append((nr,nc))

def main(): 
    global R,C,A,visited

    1. A,visited 구성 

    R,C = map(int,read().rstrip().split())
    visited = [[0 for i in range(C)]for j in range(R)]
    A = []
    for i in range(R):
        A.append(list(map(int,read().rstrip())))

    # print(A,visited)

    #2. BFS 탐색 및 최종 목적지 산출 

    bfs()
    print(visited[R-1][C-1])

main()

# 코드 구현 순서
#1. A,visited 구성 
#2. BFS 탐색 및 최종 목적지 산출 
#3. Q 구성
#4. Q 탐색
#5. 도착지점 거리 산출




'''
4 6
101111
101010
101011
111011

15

문제

(1,1)에서 시작해서 (M,N) 도착 최소시간 

NxM크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, 
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''