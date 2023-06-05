#그래프심화_5.뮤탈리스크(bfs)

from collections import deque
def main():
    global n, power, visited
    n = int(input())
    power = list(map(int, input().split()))
    for i in range(3 - len(power)):
        power.append(0)
    visited = [[[0 for i in range(61)] for j in range(61)] for k in range(61)]
    print(bfs())
    
damage = [
    [9, 3, 1],
    [9, 1, 3],
    [3, 9, 1],
    [3, 1, 9],
    [1, 9, 3],
    [1, 3, 9]
]
def bfs():
    Q = deque([(power[0], power[1], power[2])])
    visited[power[0]][power[1]][power[2]] = 1
    while len(Q) > 0:
        a, b, c = Q.popleft()
        if a == 0 and b == 0 and c == 0:
            break
        for i in range(6): # 한개라도 살아있으면 for문을 돌린다. 
            na = max(0, a - damage[i][0])
            nb = max(0, b - damage[i][1])
            nc = max(0, c - damage[i][2])
            if visited[na][nb][nc] != 0:
                continue
            Q.append((na, nb, nc))
            visited[na][nb][nc] = visited[a][b][c] + 1
    return visited[0][0][0] - 1

if __name__ == "__main__":
    main()

'''
3
12 10 4

2


[문제이해]

스타게임중 수빈 : 뮤탈리스크 1개, 강호: SCV N개 남음
각각의 SCV는 남아있는 체력이 주어져있으며,뮤탈리스크를 공격할 수는 없다. (수빈 Win)
뮤탈리스크가 공격을 할 때, 한 번에 세 개의 SCV를 공격할 수 있다.

1번째 공격 : SCV는 체력 -9감소
2번째 공격 : SCV는 체력 -3감소
3번째 공격 : SCV는 체력 -1감소 
 --> SCV 0에 도달하면 파괴 
동일 SCV 여러번 공격 불가 
1개 scv당 60개 이하자연수 

남아있는 SCV의 체력이 주어졌을 때, 
모든 SCV를 파괴하기 위해 공격해야 하는 횟수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 SCV의 수 N (1 ≤ N ≤ 3)이 주어진다. 둘째 줄에는 SCV N개의 체력이 주어진다. 체력은 60보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 SCV를 파괴하기 위한 공격 횟수의 최솟값을 출력한다.

'''