
####
#아이디어 : box를 많이 사용하려면 많이 들어가는 box 사용을 최소화해야함
#1.배열초기화(누적합,출력변수)
#2.i-1 index 누적합 부족할때만 box 사용 (차감)

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy

N = int(read().rstrip())
box_size = [0]+[1,5,10,50,100,500,1000,3000,6000,12000]
box_cnt = [0]+ list(map(int,read().rstrip().split()))
box_used = [0 for i in range(11)]

su = []
for i in range(11):
	su.append(box_size[i]*box_cnt[i])
	
psum = []
psum_n = 0 
for i in su:
	psum_n += i
	psum.append(psum_n)

for i in range(10,0,-1):
	while psum[i-1] < N and box_cnt[i] > 0:
		N -= box_size[i]		
		box_cnt[i] -= 1
		box_used[i] += 1

print(sum(box_used))
for i in box_used[1:]:
	print(i,end = ' ')


'''
7
3 3 3 3 3 3 3 3 3 3

3
2 1 0 0 0 0 0 0 0 0 

물품총개수 : 7개
[0,1,5,10,50,100,500,1000,3000,6000,12000] 를 담을수 있는 box 개수 각 3개 
box개수를 최대로 (큰 box를 보내지 않음)
box종류별 개수 (총개수) 출력

'''


