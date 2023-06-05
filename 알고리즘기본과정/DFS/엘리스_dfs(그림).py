#6.그래프심화

global R, C, a, visited, res, cnt
cnt = 0
res = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    visited[r][c] = 1 
    csum = 1 
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 or a[nr][nc] == 0: #그림이 없으면 탈출 
            continue
        csum += dfs(nr, nc) 
    return csum

def main():
    global R, C, a, visited, res, cnt
    R, C = map(int,input().split())
    a = []
    for i in range(R):
        a.append(list(map(int,input().split())))
    visited = [[0 for i in range(C)] for j in range(R)]
    #dfs진입조건설정
    for i in range(R):
        for j in range(C):
            if visited[i][j] == 0 and a[i][j] == 1:
                cnt += 1 
                res = max(res, dfs(i, j))
    print(cnt)
    print(res)

if __name__ == "__main__":
    main()

'''
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

4
9

[그림]

문제
도화지내 그림의 개수와, 넓이가 가장큰 그림의 넓이 출력하기. (가로/세로만 1로 연결되어야만 그림, 대각선 제외)
그림의 넓이 : 1의 개수

입력
세로 크기 n(1 ≤ n ≤ 500)
가로 크기 m(1 ≤ m ≤ 500)
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. 
(단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 
둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력
그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

4
9
'''
