
# Rotate Q 활용해서 jump많큼 pop한다 (부분점수)
#1.배열초기화(list)
#2.Q생성 
#3.Q실행 
#4.조건출력 

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import copy
from itertools import *

N,M,K = map(int,read().rstrip().split())
Q = deque([i+1 for i in range(N)])
# Q = deque([2,1,3,4,5])
# print(Q)

# while True: 
# 	if Q[0] != M :
# 		Q.rotate(-1) 
# 	else:
# 		break
Q.rotate(-(M-1))

# print(Q)

res = []
while len(Q) > 0 : 
	Q.rotate(-(K-1))
	res.append(Q.popleft())
	# print('Q',Q)

print(*res)

		

'''
7 1 4

4 1 6 5 7 3 2 

7 : 학생수 N
1 : 시작변호 M
4 : jump 단위 K
4 1 6 5 7 3 2 : 학생번호 

'''