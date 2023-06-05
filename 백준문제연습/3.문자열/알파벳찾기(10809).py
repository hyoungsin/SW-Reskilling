#아스키 변환

import sys 
read = sys.stdin.readline

A = list(read().rstrip())
visited = [-1 for i in range(26)]

for i in range(len(A)):
    # print(i)
    if visited[ord(A[i]) -ord('a')] == -1: # b idx가 -1이아니면, a idx가 -1이 아니면 (한번도 update안됨) 
       visited[ord(A[i]) -ord('a')] = i # b idx에 0번을 입력, a idx에 1을 넣음 

for i in visited:
    print(i,end = ' ')


'''
baekjoon

1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
'''