# 2차원배열 덧셈 
#1.배열초기화
#2.A[i][j]활용

import sys
read = sys.stdin.readline
N,M = map(int,read().rstrip().split())

A1 = []
for i in range(N):
    A1.append(list(map(int,read().rstrip().split())))

A2 = []
for j in range(N):
    A2.append(list(map(int,read().rstrip().split())))

# print(A1,A2)

res = [[0 for i in range(M)]for j in range(N)]
for i in range(N):
    for j in range(M):
        res[i][j]= A1[i][j] + A2[i][j]

print(res)


'''

3X3 배열 2개의 합 구하기 (출력 : 3X3)

3 3
1 1 1 
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

4 4 4
6 6 6
5 6 100

3 4
1 1 1 1
2 2 2 1
0 1 0 1
3 3 3 1
4 4 4 1
5 5 100 1

문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
'''