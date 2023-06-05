import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(input())
	P = [int(x) for x in input().split()]
	return N, P

# 입력 받는 부분
N, P = Input_Data()

# 여기서 부터 작성
sum = P[0]
for i in range(1,N):
	if P[i-1] < P[i]:
		sum = sum - P[i-1] + P[i]

# 출력하는 부분
print(sum)