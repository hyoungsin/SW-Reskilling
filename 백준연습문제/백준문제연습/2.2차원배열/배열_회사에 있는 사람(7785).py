
# 배열 (dict) 시간복잡도 개선
#1.배열초기화(dict) (key/value로 update)
#2.leave면 dict에서 제외 (key로제거)
#3.출력 (key로 출력됨)

import sys
read = sys.stdin.readline
N = int(read().rstrip())
A = {}
for i in range(N):
    p,q = read().rstrip().split() 
    A[p] = q
    if q == 'leave':
        del A[p] #key를 삭제하면 전체 삭제
# for key,value in A.items(): # key,value 동시 출력 
#     print(key,value)
key,value = A.items()
print(key,value)

res = [ ]
for i in A:
    res.append(i) # 반복문 반환값은 key만 반환 , update는 A[key] = value 

res.sort(reverse=True)
for i in res:
    print(i)

'''
4
Baha enter
Askar enter
Baha leave
Artem enter

Askar
Artem
첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106) 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 
각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.
회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.
현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.
'''