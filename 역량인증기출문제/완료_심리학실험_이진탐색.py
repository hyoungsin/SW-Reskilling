import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy
from itertools import *

#시간복잡도 줄이기위해 이진탐색
#1.배열초기화 (리스트,오름차순)
#2.이진탐색 조건 구현
#3.조건 출력

def main():
	N = int(read().rstrip())
	A = list(map(int, read().rstrip().split())) #1.배열초기화(리스트)
	
	start = 0 # 배열의 첫 idx
	end = N-1 # 배열의 마지막 idx
	idx1 = 0 # 숫자1 담을 변수 
	idx2 = 0 # 숫자 2 담을 변수 
	res = 1e9 # 최솟값갱신
	while start < end: # 이진탐색 문법 (2개 찾는게 답)
		val = A[start] + A[end]
		if abs(val) < res:
			res = abs(val)
			idx1 = start # 가장작은 res를 만ㄷ는 p1이 변수에 담김 
			idx2 = end # 가장작은 res를 만드는 p2가 변수에 담김 
		
		if val < 0: # 오름차순 (합이음수이면 +로 올리고)
			start += 1
		else: #합이 양수이면 -로 내린다. 
			end -= 1
	
	print(idx1,idx2)
	
main()


#조합 (시간초과 2문제 부분점수)
#1.배열초기화 (리스트)
#2.조합기준(idx기준) 첫번째 제일 작었던 숫자로 update

N = int(read().rstrip())
A = list(map(int,read().rstrip().split()))

# print(A)

comb = list(combinations(A,2)) # 2개로 이뤄진 조합 만들기 
# print(comb)

res_min = 1e9 #최솟값 찾기 (변수명을 max/min으로 하면 안됨)
x = 0
y = 0 
for i in comb:
	sum = abs(i[0]+i[1]) #두개 숫자 합의 절대값
	
	if sum < res_min: #두개 숫자 합의 절대값이 더 작아지면 
		x = i[0] # x는 첫번째 숫자로 갱신 
		y = i[1] # y는 두번째 숫자로 갱신 
	
		res_min = min(res_min,sum) # 더 적어진 값으로 min갱신 

res1 = A.index(x) # x의 index위치 (동일값이면 update안됨)
res2 = A.index(y) # y의 index 위치 
print(res1,res2,end= ' ')
	


'''
5
-102 -58 59 78 101

0 4

5 : 피실험 대상수 (10*6 ,100,000)
-102 -58 59 78 101 : 부정/긍정 기질(-10**9 ~ 10**9)

'''
