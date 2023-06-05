# 각 좌표에서 필터 적용해서 최댓값 산출 
#1.배열초기화(A(좌표)) : 70점 
#2.해당좌표에서 시작하여 필터 적용 
#3.좌표가 필터에 들어오면 cnt 
#4.max값 산출

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy

def check(r1,c1,r2,c2):
	cnt = 0 
	for r,c in A:
		if r1 <= r <= r2 and c1 <= c <= c2:
			cnt +=1 
	return cnt

def main():
	global N,M,K,A
	N,M,K = map(int,read().rstrip().split())
	A = [] # [[2, 2], [4, 6], [5, 2], [6, 4], [2, 4], [3, 3]]
	for i in range(K):
		A.append(list(map(int,read().rstrip().split())))

	res = 0 
	for r,c in A: # 2,2에서 필터 시작 
		for h in range(1,M//2): # 높이는 4를 넘을수 없음(1,2,3,4) (1,4),(4,1),(2,3),(3,2)
			x = M//2-h # 넓이는 5에서 높이를 뺀숫자 (4,3,2,1)
			for w in range(1,x+1):
				res = max(res,check(r,c,r+h,c+w)) #필터많큼 범위 지정
				print('r,c,r+h,c+w:',r,c,r+h,c+w)

	print(res)

main()	





'''
6 10 6
2 2
4 6
5 2
6 4
2 4
3 3

4

필터전체크기 : 6
살균LED 둘레길이 : 10 (3x2, 2x3, 1x4,4x1, r 차이 + c차이 * 2 = 10)
살균대상 : 6개 

'''