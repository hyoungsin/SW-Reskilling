#6.괄호문자열 (1.stack 조건문 2.출력조건 실행)

def main():
    n = int(input())
    a = input()
    stack = []
    for i in a: 
        if len(stack) == 0 : 
            stack.append(i)
            
        elif stack[-1] == '(' and i == ')':
            stack.pop()


        elif stack[-1] == '[' and i == ']':
            stack.pop()
        else:
            stack.append(i) 

        print(stack)

    if len(stack) == 0 :
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()


'''
6
()()[]

1

빈 문자열은 올바른 괄호 문자열입니다.
S가 올바른 괄호 문자열이라면,(S), [],[S] 도 올바른 괄호 문자열 S,T가 올바른 괄호 문자열이라면, ST도 올바른 괄호 문자열입니다.
)(()”, “([]“는 올바른 괄호 문자열이 아님 

첫째 줄에 S가 올바른 괄호 문자열이라면 1을, 아니라면 0을 출력합니다.
'''