# 1.배열 초기화
# 2.Stack 초기화
# 3.pop 조건 적용 (While)
# 4.stack append 

import sys
read = sys.stdin.readline

N = int(read().rstrip()) 
A = []
for i in range(N):
	A.append(int(read().rstrip())) #1.배열 초기화
	
res = 0 
for i in range(1,N):
	stack = [] # 2.Stack 초기화 (Append)
	stack.append(A[i]) # 2번째부터 Stack에 담음 (i[1])
	cnt = 1
	while i+cnt < N: # stack에 append하는 index가 5까지만 가능 (N = 6) 탈출조건 설정
	
		if stack[-1] >= A[i-1]: ## 3.pop 조건 (Stack[-1] 첫번째보다 크거나 같으면 pop)

			stack.pop() # pop해 버리고 while을 중단 종료 
			break
			
		stack.append(A[i+cnt]) # 다음 stack에 3번째것 담음 (i[2]) append list담지말고 숫자로
		cnt += 1

	res += len(stack)

print(res)


'''
6
5
2
4
2
6
1

5
'''


# import sys

# def InputData():
# 	readl = sys.stdin.readline
# 	N = int(readl())
# 	H = [ int(readl()) for i in range(N) ]
# 	return N, H


# 입력
# N: 건물 수
# H: 건물 높이
# N, H = InputData()
# ans = 0


# stack = []
# for i in range(N):
# 	while len(stack)>0:

# 		if H[i] < stack[-1]:
# 			break

# 		stack.pop()
# 		# print('stack_after:',stack)

# 	# print('res_Stack:',stack)

# 	ans += len(stack)
# 	print(len(stack), stack)
# 	stack.append(H[i])
	
	
# print(ans)



# 1.배열 초기화
# 2.Stack 초기화 
# 3.조건 적용 (이중포문)
# 4.stack append 

import sys
read = sys.stdin.readline

N = int(read().rstrip())
A = []
for i in range(N):
    A.append(int(read().rstrip()))

res = 0 
for i in range(N):
	stack = [ ]
	for j in range(i+1,N):
		if len(stack) == 0:
			stack.append(A[j])

		elif stack[-1] > A[i]:
			stack.pop()
			break

		else:
			stack.append(A[j])

	# print(stack)

	res += len(stack)

print(res)
		

'''
6
5
2
4
2
6
1

5

N : 건물수 (6) 8만개
A : 건물높이 [5,2,4,2,6,1] 10억높이 

5 -> 2,4,2
2 --> 0
4 --> 2
2 --> 0 
6 -> 1


'''
