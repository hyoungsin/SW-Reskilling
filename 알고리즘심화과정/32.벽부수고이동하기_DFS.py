#1. 배열 초기화 / 3차원 visited 생성 
#2. Q 초기화(3차원, nr/nc 기준, cnt = 1)
#3. Q 탐색 / return
#4. Q 조건정의 (벽이 아닌경우, 벽인경우)
#5. Q.append (nr,nc,cnt-1)

from collections import deque
import sys
read = sys.stdin.readline

global R, C, a, visited
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global R, C, A, visited
    Q = deque([(0, 0, 1)])  # 행, 열, 남은 벽 부수기 횟수 (CNT 1부터 줄여나감)
    visited[0][0][1] = 1

    while len(Q) > 0:
        r, c, cnt = Q.popleft()
        if r == R - 1 and c == C - 1:
            
            # print('r,c,cnt',r,c,cnt,visited[r][c][cnt]) # cnt 0 (1개 부수고) 도달 15개 

            return visited[r][c][cnt]  # 시작 칸과 도착 칸도 포함해서 세야 함

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue

            if A[nr][nc] == 0 and visited[nr][nc][cnt] == 0: # 방문안했고 벽이 아니면 append
                Q.append((nr, nc, cnt))
                visited[nr][nc][cnt] = visited[r][c][cnt] + 1

            # 벽인데 아직 벽 부수기 사용 안한 경우
            elif A[nr][nc] == 1 and cnt != 0 and visited[nr][nc][cnt - 1] ==0 : # 벽인데 cnt남아있고 기존 방문없을때 
                Q.append((nr, nc, cnt - 1)) # cnt소모한 nr,nc append 
                visited[nr][nc][cnt - 1] = visited[r][c][cnt] + 1 # cnt 소모한 nr nc는 cnt소모전 visited보다 1증가 

    # bfs 끝날 때 까지 return 안했으면 못가는 경우
    return -1


def main():
    global R, C, A, visited
    R, C = map(int, read().rstrip().split())
    visited = [[[0 for _ in range(2)] for _ in range(C)] for _ in range(R)] # [행][열][남은 벽 부수기 횟수]
    A = []

    for _ in range(R):
        c = list(map(int, read().rstrip()))
        A.append(c)

    print(bfs())


main()



'''
6 4
0100
1110
1000
0000
0111
0000

15

6 4
0000
1110
1000
0000
0111
0000

9

문제
N X M 의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.'''