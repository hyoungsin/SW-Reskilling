#그래프심화
def main():
    global R, C, a, visited, res, flag
    R, C = map(int, input().split())
    a = []
    for i in range(R):
        a.append(list(map(int,input().split())))
    visited = [[0 for i in range(C)] for j in range(R)]
    res = 0
    for i in range(R):
        for j in range(C):
            if visited[i][j] == 1:
                continue
            flag = True #visited가 아닌경우 flag True로 처리 
            dfs(i, j)
            if flag: # flag True이면 res 증가 
                res += 1
    print(res)

dr = [-1, 1, 0, 0, -1, -1, 1, 1]    # 8방향
dc = [0, 0, -1, 1, -1, 1, -1, 1]
def dfs(r, c):
    global R, C, a, visited, res, flag
    visited[r][c] = 1
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        # 범위 체크
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if a[nr][nc] > a[r][c]: # 새로 방문한 곳이 기존보다 크면 false 
            flag = False
        if visited[nr][nc] != 0:
            continue
        # 값 다르면 무시. 같은 값인 그룹만 확인해야 됨
        if a[nr][nc] != a[r][c]:
            continue
        dfs(nr, nc)

if __name__ == "__main__":
    main()

'''
8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0

3

[문제이해]
농장 :  NxM 배열 
농장에 산봉우리가 총몇개인지
산봉우리의 정의: 같은 숫자로 인접한 집합 (가로/세로 대각선 포함) 산봉우리인접격자는 더 작음 (예) 13 222 13)) 
배열내 산봉우리 개수 출력

[입력]
N : 가로(1 < N ≤ 100), 
M : 세로(1 < M ≤ 70)
a  :높이 (0 < M ≤ 500)

[출력]
산봉우리개수 

'''