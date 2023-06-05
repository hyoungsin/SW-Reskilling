import sys

def InputData():
	readl = sys.stdin.readline
	B, S, D = readl().strip().split()
	return int(B), S, D


def convert_to_decimal(B, str_nums): # 10진수로 변환
	mark = 1
	res = 0
	if str_nums[0] == '-':
		mark = -1
		str_nums = str_nums[1:]
		
	for i in range(len(str_nums)-1, -1, -1):
		res += nums.index(str_nums[i]) * B**(len(str_nums) - 1 - i)

	return res * mark

def convert_to_B(B, n): #B진수로 변환
	if n == 0:
		return str(n)
	
	mark = ""
	if n < 0 :
		mark = "-"
		n = n* -1
		
	res = ""
	while n != 0:
		left = n % B
		n = n // B
		res += nums[left]
	
	res = res[::-1]
	return mark+res
	
# 입력
nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# N : 테스트 케이스 수
# B : 진법
# S : 첫 번째 정수
# D : 두 번째 정수
N = int(input())
for _ in range(N):
	B, S, D = InputData() # 
	ans = ""
	# 코드를 작성 하세요
	temp1 = convert_to_decimal(B, S) #10진법으로 숫자 변환
	temp2 = convert_to_decimal(B, D) #10진법으로 숫자 변환	
	ans = convert_to_B(B, temp1 * temp2) #B진법으로 변환
	
	# 출력
	print(ans)


'''
5
10 789 456
16 CBA FED
10 -123 56
10 -3214 -987
10 -12345 0


359784
CAAE32
-6888
3172218
0
'''