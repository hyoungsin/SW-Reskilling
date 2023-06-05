
#1.배열 초기화
#2.단어자리수 sum
#3.내림차순
#4.높은수부터 곱하기 

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    N = int(read().rstrip())
    A = []
    for i in range(N):
        A.append(list(read().rstrip()))

    # print(A)

    visited = [0 for i in range(26)] # 이중 리스트 되지 않음 

    # print(visited)

    for word in A:
        digit = 1 # 단어마다 digit단위가 10배씩 증가
        for i in range(len(word)-1,-1,-1): # 단어에서 맨뒤가 1단위 (1,0 / 1,0) 
            
            # print('i:',i)
            # print('loc:',ord(word[i]) - ord('A'))
            # print(visited)

            visited[ord(word[i]) - ord('A')] += digit #해당 알파벳위치에 1단위/10단위 각각 sum 누적 
            digit *= 10 

    visited = sorted(visited,reverse = True)

    ma = 9
    res = 0 
    for i in visited:
        res += i * ma # res에 9부터 줄여나간수 차례대로 곱하여 출력 (9,8,.....0)
        ma -= 1 

    print(res)

main()




######################
#1.배열 초기화
#2.단어자리수 sum
#3.내림차순
#4.높은수부터 곱하기 






'''
2
AB
BA

187

최대 단어의 길이는 8

문제
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 
이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 
같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
두 수의 합은 99437이 되어서 최대가 될 것이다.

N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 
단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 
서로 다른 문자는 서로 다른 숫자를 나타낸다.

출력
첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.
'''