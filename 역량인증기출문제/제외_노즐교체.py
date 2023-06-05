
############################
#1.2차원 배열 초기화 (N,A)
#2.행기준일때 각 열에 대해 짝수교체와 홀수 교체 CASE 합중 최댓값 산출 
#3.열기준일때 각 행에 대해 짝수교체와 홀수 교체 CASE 합중 최댓값 산출  
#4.행기준과 열기준중 최댓값 산출

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy

N = int(read().rstrip())
A = [] 
for i in range(N):
	A.append(list(map(int,read().rstrip().split()))) #1.2차원 배열 초기화 (N,A)

r_sum = 0 #2.행기준일때 각 열에 대해 짝수교체와 홀수 교체 CASE 합중 최댓값 산출 
for r in range(N):
	c_even = 0 
	c_odd = 0 
	for c in range(N):
		if c % 2 == 0 : 
			c_even += A[r][c]

			# print('r,c,A[r][c]',r,c,A[r][c])


		else:
			c_odd += A[r][c] 

			# print('r,c,A[r][c]',r,c,A[r][c])

	r_max = max(c_even,c_odd)
	r_sum += r_max

	# print('r,max(c_even,c_odd),r_max,r_sum',r,max(c_even,c_odd),r_max,r_sum)

# print('r_sum:',r_sum)


c_sum = 0 #3.열기준일때 각 행에 대해 짝수교체와 홀수 교체 CASE 합중 최댓값 산출  
for c in range(N):
	c_even = 0 
	c_odd = 0 
	for r in range(N):
		if r % 2 == 0 : 
			c_even += A[r][c]

			# print('r,c,A[r][c]',r,c,A[r][c])
			# print('c_even:',c_even)

		else:
			c_odd += A[r][c] 

			# print('r,c,A[r][c]',r,c,A[r][c])
			# print('c_odd:',c_odd)

	c_max = max(c_even,c_odd)
	c_sum += c_max

# print('c_sum:',c_sum)
print(max(c_sum,r_sum)) #4.행기준과 열기준중 최댓값 산출


'''
4
3 3 1 2 
1 1 3 1 
3 3 1 1 
1 1 3 3 

22

NXN 배열 
오염도 최대값 산출 



'''

