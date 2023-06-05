import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c):
    global R,C,K,a,visited
    visited[r][c] = 1 
    cnt = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # print(nr,nc)
        if nr < 0 or nr >= R or nc <0 or nc >=C or visited[nr][nc] != 0 or a[nr][nc] == 0 : 
            continue

        cnt = cnt + dfs(nr,nc)

    return cnt 

        
def main():
    global R,C,K,a,visited
    R,C,K = map(int,read().rstrip().split())
    a = [[0 for i in range(C)]for j in range(R)]
    visited =[[0 for i in range(C)]for j in range(R)]
    for i in range(K):
        r,c = map(int,read().rstrip().split())
        r = r-1 
        c = c-1
        a[r][c] = 1
    
    # print(visited)

    res = []
    for i in range(R):
        for j in range(C):
            # print(visited[i][j])
            if visited[i][j] != 1 and a[i][j] == 1 : 
                res.append(dfs(i,j))

    print(max(res))


main()

'''
3 4 5
3 2
2 2
3 1
2 3
1 1

4
'''