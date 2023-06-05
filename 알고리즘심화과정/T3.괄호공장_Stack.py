
# case.2 (stack , index로 접근)

input()
stack = [-1]
res = 0

for i, bracket in enumerate(input()): # i 와 괄호 
    if bracket == "(": # 열리는 괄호일 경우append 
        stack.append(i)
    else:
        stack.pop() # 닫히는 괄호일 경우 기존 index pop (최초 못닫는 경우 대비 -1 입력)
        if stack: #stack에 index가 있으면 현재 index에서 최종 index를 빼줌 
            res = max(res, i - stack[-1])
        else: #stack이 비어있으면 index추가 
            stack.append(i)
print(res)

##################################################
# case.1 (stack value로 접근)
# import sys 
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n = int(read().rstrip())
# a = list(read().rstrip())
# # print(n,a)
# stack = []

# # cnt =0 # 전체길이 
# res = -1e9
# cnt= 0 
# for i in range(len(a)):
#     if len(stack) == 0:
#         stack.append(a[i])
        
#     elif stack[-1] == '(' and a[i] == ')' :
#         stack.pop()
#         cnt +=2
# 
#     else: 
#         stack.append(a[i])

# print(cnt)






'''

4
))()

2

1234567890123

13
()((((())()()

8

14
(((((())))))()

14

10
(()())())))

8

6
)()()(

4

6
(((())

4
'''