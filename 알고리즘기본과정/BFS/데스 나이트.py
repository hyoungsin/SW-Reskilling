
#bfs : start ~ end까지 이동 회수 visited[er][ec] - 1 
#1.배열 초기화 (global N,A,visited,sr,sc,cnt)
#2.bfs수행 (좌표는 4가지)
#3.er/ec에 도착하면 종료 (없으면 -1 출력) 

import sys
read = sys.stdin.readline
from collections import deque

dr = [-2,-2,0,0,2,2]
dc = [-1,1,-2,2,-1,1]
def bfs():
    global N,A,visited,sr,sc,er,ec,cnt  
    Q = deque([(sr,sc)])
    visited[sr][sc] = 1 
    cnt = 0 
    while len(Q) > 0:
        r,c = Q.popleft()
        # print('r,c,er,ec:',r,c,er,ec)
        if r == er and c == ec:
            # print(visited[er][ec] -1)   
            return visited[er][ec] -1
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >=N or nc <0 or nc >= N or visited[nr][nc] !=0:
                continue
            visited[nr][nc] = visited[r][c]+1
            # print('r,c,er,ec:',r,c,er,ec)
            # print('visited[nr][nc]',visited[nr][nc])
            # print('visited[er][ec]',visited[er][ec])

            Q.append((nr,nc))

def main():
    global N,A,visited,sr,sc,er,ec,cnt  
    N = int(read().rstrip())
    sr,sc,er,ec = map(int,read().rstrip().split())
    A = [[0 for i in range(N)]for j in range(N)]
    visited = [[0 for i in range(N)]for j in range(N)]

    res = bfs() # 이런 문법을 사용할 경우 반드시 return값을 정의해저야함 
    print(res)

    if res:
        print(visited[er][ec] -1)

    else:
        print(-1)

main()

'''
7
6 6 0 1

4

6
5 1 0 5

-1

문제
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 
데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.

크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 
체스판의 행과 열은 0번부터 시작한다.

데스 나이트는 체스판 밖으로 벗어날 수 없다.

입력
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r1, c1, r2, c2가 주어진다.

출력
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.
'''