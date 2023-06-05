
#1.배열초기화
#2.순회결과출력변수설정
#3.BFS순회 

import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [0,1,0,-1]
dc = [1,0,-1,0]
def dfs_1(r,c):
    global N,A,visited
    visited[r][c] = 1 #visited 방문체크 필수 (visited[][] 주의)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        # print('nr,nc :',nr,nc)

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] !=0 :
            continue

        # print('nr,nc :',nr,nc)

        if A[nr][nc] != A[r][c]:
            continue 

        dfs_1(nr,nc)

def dfs_2(r,c):
    global N,A,visited
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]!=0 :
            continue

        if A[nr][nc] != A[r][c]:
            continue 

        visited[nr][nc] = 1 

        dfs_2(nr,nc)


def main():
    global N,A,visited
    N = int(read().rstrip())

    visited = [[0 for i in range(N)]for j in range(N)]
    A = []
    for i in range(N):
        A.append(list(read().rstrip()))

    # print(A)

    res1 = 0 # 3팀일 경우 구역누적값 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 :

                # print(i,j)
                
                dfs_1(i,j)
                res1 += 1  

    for i in range(N): #2팀으로 update
        for j in range(N):
            if A[i][j] == 'G':
                A[i][j] = 'R'

    res2 = 0 # 2팀일 경우 구역누적값
    visited = [[0 for i in range(N)]for j in range(N)] # visited초기화 필수 
    for i in range(N):
        for j in range(N):

            # print(i,j)

            if visited[i][j] == 0  : 
                dfs_2(i,j)
                res2 += 1  

    print(res1,res2)

main()

#############################
#1.배열초기화
#2.순회결과출력변수설정
#3.BFS순회 





'''

5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

4 3

N X N 안에서 땅따먹기
3명 게임 
G/R/B
G(G/R) / R(B)
연합군 입장에서의 땅크기 (G/R) : 4
저항군 입자에서의 땅크기  : 3 

[코드]
1.배열 초기세팅 (A,visited)
2.dfs 조건 수립 (현준시각, 연합군시각)
3.dfs 탐색 
4.조건 출력 (dfs 수행 횟수)
'''
