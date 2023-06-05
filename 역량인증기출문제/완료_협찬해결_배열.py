import sys

def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	A = list(map(int, readl().split()))
	return N, A

# 입력받는 부분
N, A = input_data()

# 여기서부터 작성
def solve():
	sol = -1e9
	res = 0
	for i in A:
		if res >= 0: # 누적값이 0보다 크면 
			res += i # 누적값에 추가 해주고 
			
		elif res < 0: #누적값이 0보다 작으면 
			res = i # (-3,-3),(1,1),(2,3),(3,6)

		sol = max(sol,res) # 최댓값 산출 
		print('i,res',i,res)
		
	return sol
					
sol = solve()

'''
5
3 1 -2 5 -3

7

4
-3 1 2 3

6

기존 : 3개연속합으로 최대 금액 산출
변경 : 갯수제한없이 최대 금액 산출 
5 : 협찬물품갯수
3 1 -2 5 -3 : 협찬 금액 (누적합이 양수면 계속 누적, 음수면 0으로 하지 않고 최종 마이너스값과 이번값중 max)

'''