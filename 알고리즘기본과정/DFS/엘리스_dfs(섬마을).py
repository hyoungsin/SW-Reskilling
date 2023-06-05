
# 접근) C,R,K,a,visited,res,dfs(i,j),dfs(nc,nr)(10) and, = 




dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c):
    global C,R,K,a,visited,res
    visited[r][c] = 1 # visited는 r/c에 따라 계속 변경 
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr <0 or nr >=R or nc < 0 or nc >=C or visited[nr][nc] != 0 or a[nr][nc] == 0:
            continue
        dfs(nr,nc)

res = 0 
def main():
    global C,R,K,a,visited,res
    res = 0 
    C,R,K = map(int,input().split())
    visited = [[0 for i in range(C)]for j in range(R)]
    a = [[0 for i in range(C)]for j in range(R)]
    for i in range(K):
        c,r = map(int,input().split())
        a[r][c] = 1
    for i in range(R):
        for j in range(C): 
            if visited[i][j] == 0 and a[i][j] == 1: # 두조건 모두 맞을 경우에만 dfs 섬 탐험 
                dfs(i,j)
                res += 1
    print(res)



if __name__ == '__main__':
    main()

'''
6 5 7
0 0
1 0
1 1
4 2
4 3
2 4
3 4

3

'''