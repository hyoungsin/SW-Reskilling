#7.후위표기 (n,a, stack, cal) (1) stack.append 

def main(): 
    n = int(input())
    a = []
    stack = []

    def cal(a,b,c):
        if c == '+':
            return a+b
        if c =='-':
            return a-b

    for i in range(n):
        n = input() # 숫자+문자
        a.append(n)

    for i in a:
        if i not in ('+','-'):
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            res = cal(b,a,i)

    print(stack[0])

if __name__ == "__main__":
    main()

'''
5
1
2
+
3
+

6

첫째 줄에 입력받은 연산자, 피연산자를 이어붙여서 만든 수식을 계산한 결과를 출력합니다.
입력받은 연산자, 피연산자를 이어붙여서 만든 수식은 항상 올바른 수식입니다.
'''