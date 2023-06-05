
#5.카드짝(n,a,stack,pop 3) (1) stack과 a를 비교 
def main(): 
    n = int(input())
    a = input()
    stack = []

    for i in a: 
        if len(stack) == 0 :
            stack.append(i)
        elif stack[-1] == i: # stack과 a를 비교하는 것임
            stack.pop()
        else:
            stack.append(i)       
    print(len(stack))
    if len(stack) == 0:
        print(' ')
    else:
        for i in stack:
            print(i,end= ' ')

if __name__ == "__main__":
    main()

'''
5
ABCCB

1
A

엘리스는 N장의 카드를 한 장씩 위에 쌓으며 정리하고 있습니다. 각 카드에는 
A부터 Z까지의 알파벳 중 하나가 쓰여있습니다.
카드가 가지는 성질은 바로 카드를 쌓을 때 새로 추가한 카드의 알파벳이 바로 밑의 카드의 알파벳과 같다면 두 카드가 사라져버린다는 것입니다.

예를 들어, 엘리스가 A,B,C,C,B 순서대로 카드를 쌓는다면 4번째 카드를 쌓을 때 두 개의 C가 쓰여있는 카드가 사라지고, 
5번째 카드를 쌓을 때 두 개의 B가 쓰여있는 카드가 사라집니다

엘리스가 가지고 있는 카드에 적힌 알파벳이 카드를 쌓는 순서대로 주어질 때, 
카드를 모두 쌓은 뒤 남은 카드의 알파벳을 먼저 쌓은 카드부터 차례대로 출력해주세요!
1≤N≤100,000

'''