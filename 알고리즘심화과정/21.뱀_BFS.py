# change_index, 반시계방향, nr/nc append  

import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,1,-1]
def bfs(): 
    global N,M,K,A,visited,change,res 

    #4.뱀을 Q로 설정 

    snake = deque([(0,0)])
    visited[0][0] = 1 
    dir = 0 
    change_index = 0 
    res = 0 

    #5.뱀전환기준 설정 

    for i in range(10001):
        r,c = snake[-1]
        if change_index < K and change[change_index][0] == i+1:
            if change[change_index][1] == 'D':
                dir = (dir + 1) % 4
            else:
                dir = ((4+dir)-1) % 4  

            change_index += 1 

            nr = r + dr[dir]
            nc = c + dc[dir]

            print('i',i)

            if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] != 0 : 
                res = i + 1 
                print('i,res',i,res)
                break
            visited[nr][nc] = 1
            snake.append((nr,nc))

            #6.사과기준 설정 (꼬리짜르기)
            if A[nr][nc] == 1:
                A[nr][nc] = 0 
            else:
                r_tail,c_tail = snake.popleft()
                visited[r_tail][c_tail] = 0 

def main(): 

    #1. A, visited 생성 

    global N,M,K,A,visited,change
    N = int(read().rstrip())
    M = int(read().rstrip())
    
    # print(N,M)

    A = [[0 for i in range(N)]for j in range(N)]
    visited = [[0 for i in range(N)]for j in range(N)]

    # print(A)

    for i in range(M):
        x,y = map(int,read().rstrip().split())
        A[x-1][y-1] = 1 
    
    # print(A)

    #2.change 리스트 생성

    K = int(read().rstrip())
    change = [ ]
    for i in range(K):
        p,q =  read().rstrip().split()
        change.append((int(p),q))

    # print(change)

    #3.bfs 실행 / res출력 

    bfs()

    print(res)

main()

# [코드 구현]
#1. A, visited 생성 
#2.change 리스트 생성
#3.bfs 실행 / res출력
#4.뱀을 Q로 설정
#5.뱀전환기준 설정

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

9
'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.


'''






















'''

6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

9

① 먼저 그래프(맵)을 모두 0으로 채워준다.
② 사과 위치는 모두 2로 채워준다.
③ 앞으로 뱀이 차지하고 있는 부분은 1로 채워줄 것이다.
④ 뱀이 이동할 때 마다 머리와 꼬리는 한 칸씩 전진한다. (즉, 몸의 길이는 그대로이다.)

⑤ 이동했을 때 사과를 먹으면 머리는 전진하지만 꼬리는 그대로이다. (즉, 몸의 길이가 한 칸 늘어난다.)

⑥ 방향 전환을 해야 하는 타이밍에 맞춰 L이면 왼쪽, D이면 오른쪽으로 방향전환을 한다.

문제
 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.'''


#########

# from collections import deque
# import sys
# read = sys.stdin.readline

# global N, K, a, L, rot, snake, visited, rot_idx, time, d
# dr = [-1, 0, 1, 0]  # 상 우 하 좌. 시계방향으로 잡아야 회전시키기 편함
# dc = [0, 1, 0, -1]


# def move_snake():
#     global N, K, a, L, rot, snake, visited, rot_idx, time, d

#     time = 0  # 경과한 시간
#     d = 1  # 뱀은 처음에 오른쪽을 보고 있음
#     snake = deque([(0, 0)])  # 뱀이 앞뒤로 늘어나고 잘리고 하기 때문에 덱을 사용. 0번 인덱스가 머리. 반대방향이 꼬리
#     rot_idx = 0     # 회전 정보 담아둔 리스트의 인덱스.
#     while True:
#         time += 1
#         # 뱀위 현재 머리 위치
#         r = snake[0][0]
#         c = snake[0][1]

#         # 현재 위치로부터 이동할 좌표
#         nr = r + dr[d]
#         nc = c + dc[d]

#         # 벽에 부딪히거나 자기 몸통에 닿게 되는지 확인
#         if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] != 0:
#             break

#         # 이상 없으므로 이동
#         snake.appendleft((nr, nc))
#         visited[nr][nc] = 1

#         # 사과 있는지 확인
#         if a[nr][nc] == 1:
#             a[nr][nc] = 0

#         # 사과 없는 경우. 꼬리 제거하고 visited 0으로 변경
#         else:
#             tail_r, tail_c = snake.pop()
#             visited[tail_r][tail_c] = 0

#         # 해당 시간이 됐을때 회전
#         # 길이 체크 안해주면 마지막 회전 이후 다음번에 인덱스 에러 발생
#         if rot_idx < len(rot) and time == rot[rot_idx][0]:
#             d = (d + rot[rot_idx][1]) % 4
#             rot_idx += 1    # rot_idx를 한번 사용했기 때문에 다음 인덱스를 바라보게 설정

#     return time


# def main():
#     global N, K, a, L, rot, snake, visited, rot_idx, time, d
#     N = int(read().rstrip())
#     K = int(read().rstrip())
#     a = [[0 for _ in range(N)] for _ in range(N)]   # 사과 표시할 지도
#     visited = [[0 for _ in range(N)] for _ in range(N)]     # 뱀이 걸치고 있는 영역 표시할 지도

#     for _ in range(K):
#         r, c = map(int, read().rstrip().split())
#         a[r - 1][c - 1] = 1     # 입력 받은 위치에 사과 표시. 시작 지점을 (0, 0)으로 바꾸기 위해 1을 빼줌

#     L = int(read().rstrip())
#     rot = []
#     for _ in range(L):
#         x, c = read().rstrip().split()

#         # dr, dc의 인덱스롤 1증가 시키면 오른쪽 방향, 3증가 시키고 4로 나눈 나머지는 왼쪽 방향이 됨
#         if c == 'L':    # 왼쪽인 경우 -1로 변경
#             rot.append((int(x), 3))     # x를 문자로 받았기 때문에 숫자로 변환
#         else:
#             rot.append((int(x), 1))

#     print(move_snake())


# if __name__ == '__main__':
#     main()