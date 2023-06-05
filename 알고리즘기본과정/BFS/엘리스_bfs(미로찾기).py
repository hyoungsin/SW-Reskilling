# https://www.acmicpc.net/problem/2178 ()

def main(): 
    global n,a,visited
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input())))
    visited = [[0 for i in range(n)]for j in range(n)]
    bfs()
    print(visited[n-1][n-1])

from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs():
    Q = deque([(0,0)])
    visited[0][0] = 1
    while len(Q) > 0: 
        r,c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr <0 or nr >=n or nc<0 or nc>= n or  visited[nr][nc] != 0 or a[nr][nc] == 0 :
                continue
            if r == n-1 and c == n-1:
                return
            visited[nr][nc] = visited[r][c]+1
            Q.append((nr,nc))

if __name__ == '__main__':
    main()


for i in 


'''
5
10111
10101
10101
10101
11111

9
'''