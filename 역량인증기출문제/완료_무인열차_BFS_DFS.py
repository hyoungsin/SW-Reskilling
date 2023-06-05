#######################
#1.배열초기화
#2.bd정보갱신(DFS)
#3.Q초기화 (BFS)
#4.Q탐색
#5.조건출력

import sys
sys.setrecursionlimit(10**6)
from collections import deque 

def main():
	global R,C,a,visited
	R,C = map(int,input().split())
	a = []
	for i in range(R):
		a.append(list(map(int,input().split())))
	visited = [[0 for i in range(C)]for j in range(R)]
	bd = 0 
	for i in range(R):
		for j in range(C):
			if a[i][j] == 1 and visited[i][j] == 0: 
				bd +=1 
				dfs(i,j,bd)

	print(bfs())
	
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c,bd):
	visited[r][c] = 1
	a[r][c] = bd
	for i in range(4):
		nr = r + dr[i]
		nc = c + dc[i]
		if nr < 0 or nr >=R or nc <0 or nc >=C or visited[nr][nc] !=0 or a[nr][nc] == 0 : 
			continue 
		dfs(nr,nc,bd)
		
def bfs(): 
	global R,C,a,visited
	Q = deque()
	visited = [[0 for i in range(C)]for j in range(R)]
	for i in range(R):
		for j in range(C): 
			if a[i][j] == 1: 
				visited[i][j] = 1
				Q.append((i,j))
	while len(Q) > 0 : 
		r,c = Q.popleft()
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if nr < 0 or nr >=R or nc <0 or nc >=C or visited[nr][nc] !=0 or a[nr][nc] == 1 : 
				continue 
			if a[nr][nc] == 2:
				return visited[r][c] - 1
			visited[nr][nc] = visited[r][c]+1
			Q.append((nr,nc))
			
main()

'''
6 16
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 1 1 1 1 0 0 0 0 1 1 1 0 0 0 
0 0 0 1 1 1 1 0 0 0 0 1 1 0 0 0 
0 1 1 1 1 1 0 0 0 0 0 1 1 1 0 0 
0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 
0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 

4
'''

