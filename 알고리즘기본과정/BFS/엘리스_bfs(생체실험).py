# 접근: 

from collections import deque

dr = [-1, 1, 0, 0] # 상하좌우 
dc = [0, 0, -1, 1]
res = 0 # 날짜 경과

def bfs():
    global cnt,res
    Q = deque()
    cnt = 0 # 감염되지 않은 생쥐 
    for i in range(R):
        c = list(map(int,input().split()))
        a.append(c) # 4행을 빈리스트에 update함
        for j in range(C):
            if a[i][j] == 1: #감염되어있는경우 (시작할때부터)
                Q.append((i, j, 0)) # 0일차 (최초 세팅)
                visited[i][j] = 1
            elif a[i][j] == 0:#감염이되지 않았다면 
                cnt += 1 #감염되지 않은생쥐 추가 
    while len(Q) > 0:
        r, c, d = Q.popleft() # 시작위치 선언 필요없음 (행,열,시간(0에서 시작))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 or a[nr][nc] != 0: 
                continue    # 맵 범위 벗어나거나, 방문 했거나 , 정상 생쥐 아닌 경우
            Q.append((nr, nc, d + 1)) # Q에 새로운 행 열 (nr, nc),d+1 삽입 한칸이동 날짜 1일 추가
            visited[nr][nc] = 1 # visited에 1 표시
            a[nr][nc] = 1 # array에 감염 표시 
            cnt -= 1 # 생쥐를 감염시키는 행위
            if cnt == 0:
                res = d + 1
                return
                
def main():
    global R, C, visited, a, cnt
    C, R = map(int,input().split())
    a = []
    visited = [[0 for c in range(C)] for r in range(R)]
    bfs()
    if cnt == 0:
        print(res)
    else:
        print(-1)

if __name__ == '__main__':
    main()

'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

8
'''