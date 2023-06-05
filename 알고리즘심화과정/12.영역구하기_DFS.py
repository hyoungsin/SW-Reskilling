# https://www.acmicpc.net/problem/2583

import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c): 
    global R,C,K,a,visited,r1,c1,r2,c2
    visited[r][c] = 1
    cnt = 1 

    for i in range(4): 
        nr = r + dr[i]
        nc = c + dc[i]
        
        if nr < 0 or nr >=R or nc < 0 or nc >=C or visited[nr][nc] !=0 or a[nr][nc] == 1:
            continue
        cnt += dfs(nr,nc)
        # print(cnt)

    return cnt


def main(): 
    global R,C,K,a,visited,r1,c1,r2,c2
    R,C,K = map(int,read().rstrip().split())
    a = [[0 for i in range(C)]for j in range(R)]
    visited = [[0 for i in range(C)]for j in range(R)]

    for i in range(K): 
        c1,r1,c2,r2 = map(int,read().rstrip().split())
        for i in range((R-r2),(R-r1)):
            for j in range(c1,c2):
                a[i][j] = 1
    # print(a)

    res = []
    for i in range(R):
        for j in range(C): 
            if visited[i][j] == 0 and a[i][j] == 0:
                res.append(dfs(i,j))
    # print(res)

    res.sort()
    print(len(res))
    for i in res:
        print(i,end=' ')

main()



'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

3
1 7 13

문제
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 
이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 
3개의 분리된 영역으로 나누어지게 된다.



<그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 
그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 
한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 
모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.'''