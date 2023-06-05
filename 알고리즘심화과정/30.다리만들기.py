'''
요약 
1.main 배열 구성 (A,visited)
2.land (땅) 위치 지정 (1,2,3) (dfs)
3.land와 land사이 거리구하기 (최솟값) (bfs)
4.조건 맞으면 출력 (맨하튼 최단거리)
4.다음 조건 append 
'''
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]
def bfs(land): 
    global N,A,visited
    Q = deque()
    visited = [[0 for i in range(N)]for j in range(N)] # visited 초기세팅 

    for i in range(N):
        for j in range(N): 
            if A[i][j] == land: 
                visited[i][j] = 0
                Q.append((i,j))
                
    while len(Q) > 0 : 
        r,c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc <0 or nc >= N or visited[nr][nc] !=0 : 
                continue 
            if A[nr][nc] == land: 
                continue 

            if A[nr][nc] != 0: # 조건 도달하였으므로 return 
                return visited[r][c]
            
            visited[nr][nc] = visited[r][c]+1 # 조건 미도달시 next r /c visited 추가 
            
            # print('r,c',r,c,visited[r][c])

            Q.append((nr,nc))

def dfs(r,c,land):
    visited[r][c] = 1
    A[r][c] = land # 첫번째 땅은 bd 1로 표기 
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc <0 or nc >=N or visited[nr][nc] !=0 or A[nr][nc] == 0 : # 방문했거나 바다면 탈출 
            continue 
        dfs(nr,nc,land)
                    
def main():
    global N,A,visited
    N = int(read().rstrip())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split())))
    visited = [[0 for i in range(N)]for j in range(N)] # A,visited 초기세팅
    land = 0 # 땅 numbering

    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and visited[i][j] == 0:  #땅이고 방문한 적이 없는 곳은 bd 1로 표기 
                land +=1
                dfs(i,j,land)

    # print()

    for i in range(N): # land 번호 설정 
        for j in range(N):
            print(A[i][j],end= ' ')
        print()

    # res = [ ]
    # for i in range(1,land+1):
    #     res.append(bfs(i))
    
    # print(min(res))

    res = 1e9
    for i in range(1,land+1):
        res = min(bfs(i),res)
    
    print(res)      
main()

'''

10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0

3

여러 섬으로 이루어진 나라가 있다. 
한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고, 그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

이 나라는 N×N크기의 이차원 평면상에 존재한다. 이 나라는 여러 섬으로 이루어져 있으며, 섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다. 
다음은 세 개의 섬으로 이루어진 나라의 지도이다.


위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다. 이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다. 
가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다. 다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.



물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나, 위의 경우가 놓는 다리의 길이가 3으로 가장 짧다
(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).

지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.

입력
첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다. 
그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다. 항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

출력
첫째 줄에 가장 짧은 다리의 길이를 출력한다.'''