
# r/c는 방향이 일치해야 함(상/하/좌/우), nr/nc의 방향은 반대어야 이동가능 
# 1.방향,pipe정보,이동조건 (이동후 cnt) 세팅
# 2.배열 초기화
# 3.dfs 통해 조건 맞으면 cnt 추가
# 4.전체 배열에서 파이프 없는 값 차감= 삭제파이프개수 (0제외)

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy

dr = [-1,1,0,0] #이동 방향(상-하-좌-우) #1.방향,pipe정보,이동조건 (이동후 cnt) 세팅
dc = [0,0,-1,1]
pipe = { #파이프모양 (1일때 이동가능)
	0 : [0,0,0,0], # 이동불가 
	1 : [0,0,1,1], # 좌/우
	2 : [1,1,0,0], # 상/하 
	3 : [0,1,0,1], # 하/우
	4 : [0,1,1,0],
	5 : [1,0,1,0],
	6 : [1,0,0,1],
	7 : [1,1,0,1],
	8 : [0,1,1,1],
	9 : [1,1,1,0],
	'A' : [1,0,1,1],
	'B' : [1,1,1,1]
}
match = [1,0,3,2] # r/c와 nr/nc의 조건

def dfs(r,c):
	global N,sr,sc,A,visited,cnt 
	visited[r][c] = 1 
	cnt = 1 
	for i in range(4):
		nr = r + dr[i]
		nc = c + dc[i]
		if nr < 0 or nr >= N or nc <0 or nc >=N or visited[nr][nc] != 0 or A[nr][nc] == 0:
			continue
		if pipe[A[r][c]][i] == 1 and pipe[A[nr][nc]][connect[i]] == 1: #3.dfs 통해 조건 맞으면 cnt 추가
			cnt += dfs(nr,nc)
	return cnt

def main():
	global N,sr,sc,A,visited,cnt
	N = int(read().rstrip())
	sr,sc = map(int,read().rstrip().split())
	A = []
	visited = [[0 for i in range(N)]for j in range(N)]
	for i in range(N):
		A.append(list(map(int,read().rstrip()))) #2.배열 초기화

	dfs(sr,sc)

	cnt_zero = 0 
	for i in range(N):
		for j in range(N):
			if A[i][j] == 0:
				cnt_zero += 1
	print(N**2 - cnt_zero - cnt) #4.전체 배열에서 파이프 없는 값 차감= 삭제파이프개수 (0제외)
main()






'''
4
0 0
2799
7439
0652
2172

5

4 : 배열 n x n 
0 0 : 시작위치
파이프 모양 

'''

	
	