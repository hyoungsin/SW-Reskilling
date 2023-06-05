
# 접근 :n,m,a,res,가능범위,중복여부(1) append값

n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))

res = []
for i in a:
    for j in range(1,m//i+1):
        if i*j not in res:
            res.append(i*j)


for i in a:
    for j in range(1,m//i+1):
        if i*j not in res:
            res.append(i*j)
print(len(res))

'''
첫 줄에 감기에 걸린 직원의 수 N과 김루팡이 직원들을 관찰한 시간 C(초)를 입력합니다.
1≤N≤100, 1≤C≤36,000

그 다음 N개의 줄에는 감기에 걸린 직원들이 기침하는 주기를 한 줄에 하나씩 입력합니다.
주기는 1보다 크거나 같고, C보다 작거나 같은 자연수입니다.

김루팡이 관찰하는 동안 들을 수 있는 기침 소리의 총 횟수를 출력합니다.

2 20
4
6

7
'''