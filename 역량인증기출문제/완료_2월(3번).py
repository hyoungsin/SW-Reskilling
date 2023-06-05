
#1.문자배열초기화
#2.숫자(lo)리스트 생성 (0,1,2,3,4,5,0)
#3.거리계산(dist)배열초기화 
#4.bfs수행 (최단거리 update)
#5.출력기준좌표 최단거리 update
#6.번호 순회 순서 순열로 생성 (6개) 최솟값 산출

import sys
from itertools import permutations
from collections import deque
read = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(r, c, start_num): # 숫자 좌표간 거리 계산하는 함수
    global R,C,A,dist
    Q = deque()
    visited = [[0] * C for _ in range(R)]
    Q.append((r, c, 0))
    visited[r][c] = 1

    while len(Q) >0 :
        r, c, d = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 or A[nr][nc] == '*':
                continue

            visited[nr][nc] = 1
            Q.append((nr, nc, d + 1))

            if A[nr][nc] != '.': # '.' 이아닌 경우 (숫자인경우) 도착하면 해당 좌표 1더하고 return 
                dist[start_num][A[nr][nc]] = d + 1 #5.출력기준좌표 최단거리 update

def main():
    global R,C,A,dist
    R, C = map(int, read().rstrip().split())
    A = [] #1.문자배열 초기화 
    for i in range(R):
        A.append(list(read().rstrip()))

    ma = int(-1e9) # 최댓값 산출 
    lo = [] #2.target(숫자)저장 (0,1,2,3,4,5,0)
    for r in range(R):
        for c in range(C):
            if A[r][c] == 'S': # S를 0으로 변환 
                A[r][c] = 0
                lo.append((r, c, 0)) # 0 --> start 번호 (0)

            if A[r][c] not in ['S', '.', '*']: # 문자제외후 int로 변환 
                A[r][c] = int(A[r][c])
                ma = max(ma, A[r][c]) # 숫자가 최대 9개까지 나옴 (차례대로 숫자update(어짜피순열))
                lo.append((r, c, A[r][c]))
                
    dist = [[0 for i in range(ma+1)]for j in range(ma+1)] #3.숫자간 거리계산(dist)배열초기화 

    for r, c, start_num in lo: # 숫자 좌표간 거리 구하기
        bfs(r, c, start_num) #4.bfs수행 (최단거리 update)

    permu = permutations(list(range(1, ma + 1)), ma) #6.번호 순회 순서 순열로 생성 (6개) 최솟값 산출
    mi = int(1e9) # 최솟값 산출
    for p in permu:
        path = [0] + list(p) + [0] # 가는 순서 순열에 출발점, 도착점 추가 (0 --> 1 -> 2 -->.... -->0)
        temp_dist = 0      

        print(path)

        for i in range(len(path)): # 출발점부터 도착점까지 총 거리 계산 (0,1,2,3,4 5개) 
            temp_dist += dist[path[i]][path[i - 1]] # start / end / 1,2,3,4 --> 6개 필요 
    
        mi = min(mi, temp_dist) # 최소 거리 갱신

    print(mi)

main()

'''
5 5
.S*..
..*2.
.4...
1..**
...3*

18

1) 모든 두 숫자 좌표간 거리를 2차원 배열에 저장
2) 가는 순서를 나타내는 순열을 생성하여 각 순열마다 구해지는 총거리 최솟값 산출 

1.배열초기화

OSXOO
OOX1O
OOOOO
2OOXX
OOO3O

2.Start를 0으로 변경

O0XOO
OOX1O
OOOOO
2OOXX
OOO3O

3.숫자간 거리 배열로 생성 (예) 0 --> 0, 0--> 1, 1--> 1, 1-->2....)

0 5 4 6
5 0 5 5
4 5 0 4
6 5 4 0

4.순열 (permutations) 실행후 0 -->0 case 중 최솟값 산출

A. 0 → 1 → 2 → 3 → 0 : 총 거리 20
B. 0 → 1 → 3 → 2 → 0 : 총 거리 18 --> res
C. 0 → 2 → 1 → 3 → 0 : 총 거리 20
D. 0 → 2 → 3 → 1 → 0 (B와 동일) 총거리 18
E. 0 → 3 → 1 → 2 → 0 (C와 동일) 총거리 20
F. 0 → 3 → 2 → 1 → 0 (A와 동일) 총거리 20 
'''