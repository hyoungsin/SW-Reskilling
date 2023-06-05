
import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r,c): 
    global R,C,K,a,visited,r1,c1,r2,c2
    visited[r][c] = 1
    cnt = 1 
    for i in range(4): 
        nr = r + dr[i]
        nc = c + dc[i]
        
        if nr < 0 or nr >=N or nc < 0 or nc >=N or visited[nr][nc] !=0:
            continue

        if A[nr][nc] == 0:
            continue

        cnt += dfs(nr,nc)
    return cnt

def main(): 
    global N,A,visited
    N = int(read().rstrip()) #1.배열초기화
    A = []
    for i in range(N):
        A.append(list(map(int,read().rstrip())))
    visited = [[0 for i in range(N)]for j in range(N)]

    res = []
    for i in range(N):
        for j in range(N): 
            if visited[i][j] == 0 and A[i][j] == 1:
                res.append(dfs(i,j))
    res.sort()
    print(len(res))
    for i in res:
        print(i)

main()