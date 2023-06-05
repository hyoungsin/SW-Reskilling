# import sys 
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# from collections import deque

# dr = [0,1,0,-1] 
# dc = [1,0,-1,0]
# def bfs(): 
#     global C,R,A,visited,cnt,day

#     #3.Q설정 (감염쥐), 감염쥐가 아니면 정상쥐 cnt증가 

#     cnt = 0 
#     for i in range(R):
#         for j in range(C):
#                 if A[i][j] == 1: 
#                     Q = deque([(i,j,0)])
#                     visited[i][j] = 1
#                 else: 
#                      cnt += 1
    
#     #.Q 탐색 (제약조건내), Day 증가 정상cnt 감소  

#     while len(Q) > 0 : 
#         r,c,d = Q.popleft()

#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr < 0 or nr >=R or nc < 0 or nc >=C or visited[nr][nc] != 0 or A[nr][nc] == 1: 
#                 continue
#             day = d+1 
#             Q.append((nr,nc,day))
#             A[nr][nc] = 1 #감염쥐로 변경 
#             visited[nr][nc] = 1 
#             cnt -= 1

#             #5.return 조건 완성

#             if cnt == 0:
#                 return day
        
# def main():
#     global C,R,A,visited,res

#     #1. A, visited 구성 

#     C,R = map(int,read().rstrip().split())
#     A = []
#     for i in range(R):
#             A.append(list(map(int,read().rstrip().split())))

#     visited = [[0 for i in range(C)] for j in range(R)]

#     # print(C,R,A,visited)

#     #2. bfs 수행 (else조건추가) 

#     res = bfs()
#     if res:
#          print(day) # day : 전역 변수
#     else:
#          print(-1) # return조건 안맞으면 -1 출력

# main()

# 코드구현
#1. A, visited 구성
#2. bfs 수행 (else조건추가)
#3.Q설정 (감염쥐), 감염쥐가 아니면 정상쥐 cnt증가
#4.Q 탐색 (제약조건내), Day 증가 정상cnt 감소
#5.return 조건 완성


import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs():
    global C,R,A,visited,day
    cnt = 0 
    for i in range(R):
        for j in range(C):
            if A[i][j] == 1 : 
                visited[i][j]= 1
                Q = deque([(i,j,0)])
            else:
                cnt += 1

    while len(Q) > 0 :
        r,c,d = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr <0 or nr >=R or nc <0 or nc >=C or visited[nr][nc] != 0 or A[nr][nc] == 1: 
                continue
            visited[nr][nc] = 1
            cnt -= 1
            day = d+ 1 
            Q.append((nr,nc,day))

            if cnt == 0:
                return day 


def main():
    global C,R, A , visited
    C,R = map(int,read().rstrip().split())
    visited = [[0 for i in range(C)]for j in range(R)]
    A = []
    for i in range(R):
       A.append(list(map(int,read().rstrip().split())))

    res = bfs()
    if res : 
        print(day)
    else:
        print(-1)

main()


      

'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

8

[문제 요약]
감염쥐 : 1 
미감염쥐 : 0 
미감염쥐개수 : cnt = 0 (추가/삭제)
출력 : 미감염쥐 0이 모두 1로 변하는데 걸린 날짜 
       모두 1로 안변한다면 -1 

'''