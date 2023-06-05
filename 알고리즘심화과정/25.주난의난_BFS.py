
import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]
def bfs(): 
    global R,C,R1,C1,R2,C2,A,visited

    #3. Q 구성 (나로부터)

    Q = deque([(R1-1,C1-1)]) #좌표 차이 반영 
    visited[R1][C1] = 1 
    cnt = 0 
    
    #4. 이중 Q (Q2구성)

    while True: 
        cnt += 1
        Q2 = deque()

    #5. Q 수행 (미로찾기)

        while len(Q) > 0 : 
            r,c = Q.popleft()
            if r == R2 -1 and c == C2-1: #좌표 차이 반영 
                return cnt 
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 :
                    continue
                if A[nr][nc] == '1':
                    Q2.append((nr,nc))
                
                else:
                    Q.append((nr,nc))
                
                visited[nr][nc] = 1

        Q = Q2 # Q2라는 새로운 Q를 재수행


def main():
    global R,C,R1,C1,R2,C2,A,visited 

    #1.A,visited, R1/C1, R2/C2 구성 

    R,C = map(int,read().rstrip().split())
    R1,C1,R2,C2 = map(int,read().rstrip().split())
    visited = [[0 for i in range(C)]for j in range(R)]
    A = []
    for i in range(R):
        A.append(list(read().rstrip()))

    print(R1,C1,R2,C2,A)

    #2.bfs 수행 및 출력 

    print(bfs())

main()

'''
5 7
3 4 1 2
1#10111
1101001
001*111
1101111
0011001

3

주난이는 점프의 파동으로 주변의 모든 친구들을 쓰러뜨리고(?) 누군가 훔쳐간 초코바를 찾으려고 한다. 
주난이는 N×M크기의 학교 교실 어딘가에서 뛰기 시작했다. 
주난이의 파동은 상하좌우 4방향으로 친구들을 쓰러뜨릴때 까지 계속해서 퍼져나간다. (쓰러지면 1번 파동 끝남)
한 번의 점프는 한 겹의 친구들을 쓰러뜨린다

입력
첫째 줄에 주난이가 위치한 교실의 크기 N, M이 주어진다. (1 ≤ N, M ≤ 300)
둘째 줄에 주난이의 위치 x1, y1과 범인의 위치 x2, y2가 주어진다. (1 ≤ x1, x2 ≤ N, 1 ≤ y1, y2 ≤ M)
이후 N×M 크기의 교실 정보가 주어진다. 0은 빈 공간, 1은 친구, *는 주난, #는 범인을 뜻한다.

출력
주난이가 범인을 잡기 위해 최소 몇 번의 점프를 해야 하는지 출력한다.

'''