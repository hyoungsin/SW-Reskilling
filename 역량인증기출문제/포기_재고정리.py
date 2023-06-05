from itertools import permutations

N,M = map(int,input().split())
A = list(map(int,input().split()))
num = [0]*10

psum = [[0 for _ in range(N+1)] for _ in range(M+1)] #7개 2개 누적값 

print(psum)

for i, a in enumerate(A):
    num[a] += 1 # Num Deck에 1/2 저장 
    
    for b in range(1,M+1):
        psum[b][i+1] = psum[b][i]
        if a==b:
            psum[b][i+1] += 1

total = 0
for P in permutations(range(1,M+1)):
    idx = 0
    cnt = 0
    for p in P:
        s,e = idx, idx+num[p]
        cnt += psum[p][e]-psum[p][s]
        idx = e
    total = max(total,cnt)



'''
7 2
1 2 2 2 1 2 1 

2

7 : 제품개수
2 : 제품 종류 (1,2)
1 2 2 2 1 2 1 : 제품종류별 배열 
같은 숫자가 이어지도록 배열해야 함
최소 옮겨야햐는 횟수 (빼고/넣고 각각 cnt 1 최솟값)

'''