
# https://www.acmicpc.net/problem/10808 (count sorting)

#방법1(탐욕적기법)

a = input()
d = []
for i in range(ord('a'), ord('z')+1):
    d.append(chr(i))
res = []

for i in d: 
    cnt = 0
    for j in a: # a.count(i) 방법사용하면 일중포문 
        if j == i:
            cnt += 1
    res.append(cnt)

for i in res:
    print(i,end=' ')

#방법2(count sort)

# a = input()
# d = [0 for i in range(26)]
# for i in a:
#     d[ord(i)-ord('a')]+=1

# for i in d:
#     print(i,end=' ')



'''
baekjoon

1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0

문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력
단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.
'''