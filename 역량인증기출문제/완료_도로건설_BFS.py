
#1.A,visited 구성 BFS 수행 
#2.Q 구성
#3.Q 탐색 
#4.Q 갱신
#5.조건 출력 (최종 도달 지점) 

import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque 
dr = [1,0,-1,0]
dc = [0,1,0,-1]
def bfs():
    global N,A,visited
    Q = deque([(0,0)]) # 본사 위치에서 시작 

    # print(visited)

    visited[0][0] = 0 # visited는 비용을 의미하며 (0,0) 본사 그대로 위치 비용은 0임 (방문check x)

    while len(Q) > 0 :
        r,c = Q.popleft() # r,c pop 
        # if r == N-1 and c == N-1 : #공장 도착하면 return 
        #     return 
        for i in range(4): # nr,nc 점검 
            nr = r + dr[i]
            nc = c + dc[i]
            if nr <0 or nr >= N or nc < 0 or nc >= N :
                continue

            # visited[nr][nc] = min(visited[r][c]+A[nr][nc],visited[nr][nc]) # nr,nc 최솟값 갱신

            if visited[nr][nc] > visited[r][c]+A[nr][nc]: 
                visited[nr][nc] = visited[r][c]+A[nr][nc]

                Q.append((nr,nc)) # 더 가격이 쌀때만 nr/nc 진행 (갱신대상)

def main():
    global N,A,visited
    N = int(read().rstrip())
    visited = [[1e9 for i in range(N)]for j in range(N)] # 3X3 배열 확인
    A = []
    for i in range(N):
        A.append(list(map(int,read().rstrip())))

    # print(A)
    # print(visited)

    bfs() # bfs수행 

    print(visited[N-1][N-1]) # 공장도착시 Visited값 추출 

main()






'''

3
041
253
620

8

본사(0,0)에서 공장(N-1,N-1)까지 도로건설
최소 토지구입비용 산출 (다른 경로도 검색,플로이드)
토지구입비용 표시 (0원일 경우 추가 비용없음)

'''
