
# 접근) res.append(dfs(i,j)), cnt+=dfs(nr,nc) 에러) list/split,visited대괄호, 0/1, 부등호부등호, cnt = 1(2), dfr, viisited , visited[i]

def main():
    global n,a,visited,res,cnt 
    n = int(input())
    a = []
    res = []
    for i in range(n):
        a.append(list(map(int,input())))
    visited = [[0 for i in range(n)]for j in range(n)]
  
    for i in range(n):
        for j in range(n): 
            if visited[i][j] == 0 and a[i][j] == 1 : 
                res.append(dfs(i,j))
    res.sort()
    print(len(res))
    for i in res:
        print(i)


dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c):
    visited[r][c] = 1 
    cnt = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr <0 or nr >= n or nc <0 or nc>=n or visited[nr][nc] !=0 or a[nr][nc] == 0:
            continue
        cnt += dfs(nr,nc)
    return cnt 

if __name__ == "__main__":
    main()

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
7
8
9

같은반끼리 식사함, 각반에 몇명인지 확인
숫자가 1인 경우 (섬) cnt 1을 추가함 
각섬에 몇명이 있는지 출력 (오름차순)

[입력]
첫째 줄에는 지도의 크기 n이 주어져요. 지도는 항상 정사각형이예요.
두 번째 줄부터 지도의 정보가 주어져요. 1은 해당 자리에 학생이 있다는 뜻이고, 0은 없다는 뜻이랍니다.

[출력]
첫 번째 줄에는 반의 전체 개수를 출력해요.
두 번째 줄부터 각 반에 속한 학생의 수를 오름차순으로 정렬한 결과를 출력해요.


'''
