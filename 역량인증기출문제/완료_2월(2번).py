
#1.배열구성
#2.행합 계산
#3.열합 계산(visited활용)
#4.before/after 차이 계산

import sys 
read = sys.stdin.readline

n = int(read().rstrip())
A = []
for i in range(n): #1.배열구성
        a.append(list(map(int,read().rstrip().split())))

r_sum = [] #2.행합 계산
for i in a: 
        r_sum.append(sum(i))

#3.열합 계산(visited활용)
visited = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
        for j in range(n):
                visited[i][j] = a[j][i]

c_sum = []
for i in visited:
        c_sum.append(sum(i))

#4.before/after 차이 계산 
before = sum(r_sum)
after = max(max(r_sum),max(c_sum)) * n
res = after - before 

print(res)

'''
3
3 4 5
4 5 6
2 3 7

15

창고정리 
최소 숫자를 더해서 행과 열의 합이 모두 동일하도록 만든다

'''

