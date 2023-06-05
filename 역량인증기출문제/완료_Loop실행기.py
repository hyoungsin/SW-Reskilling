
#1. S[1] 는 반복회수 (cnt)
#2. S[2] 부터는 문자 >, < 나올때까지 문자 추가 
#3. < 나오면 재귀수행 > 나오면 재귀함수의 처음으로 가서 반복  재귀끝나는 index(p) 부터 다시 본함수 시작 
#4. > 나오면 함수의 처음부터 재 반복 (cnt 0될때까지)

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def input_data():
	loop = read().strip()
	return loop #3.loop값 출력 

def anlysis_loop(loop, s): #look 최초 입력값 <2A<3B>CE>, 0 
	p = s
	cnt = int(loop[s+1]) # 반복회수 (3회)
	while cnt:
		cnt -= 1 # 3 --> 2 --> 1 --> 0 (탈출)
		p = s+2 # loop[2]부터 문자열 
		while loop[p] != '>': #해당위치가 닫히는 괄호가 아닐 경우, 
			if loop[p] == '<': # 그 안에서 또 열릴 경우 
				p = anlysis_loop(loop, p) #재귀한번더 
				# print('p:',p) #재귀의 끝 3에서 시작 6에서 완료(5 3번반복) 7부터시작 

			else: # 닫는 괄호가 오기전까지 계속 출력 (7 ~ 8)
				print(loop[p], end='') #문자열이어서 출력 (ABC)

			p+=1 # 닫는 괄호가 오면 while문 탈출 cnt개수줌

			# print('p:',p)

	return p

loop = input_data() #1.input data수행후 loop에 update

anlysis_loop(loop, 0) #2.analysis loop 실행 


'''
<3ABC>

ABCABCABC

<2A<3B>CE>

ABBBCEABBBCE


문자열길이 : 3 ~ 100
Depth : 1 ~ 10
Loop실행결과 출력

'''