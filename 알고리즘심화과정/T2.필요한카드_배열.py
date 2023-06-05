import sys 
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = []
for i in range(n): 
    a.append(int(read().rstrip()))
a.sort()

# print(a)

res = -1e9 # i 실행할때마다 reset 
for i in range(n): # 처음부터 끝까지 검토 
    c = 0 # 최초위치별 5이내 조건 cnt
    for j in range(i, i + 5): # 0 ~ 5범위 조회 
        if j < n and a[j] < a[i] + 5: # j < n 은 (0,1,2,3,4) 만 탐색(or index에러)
            c += 1 # 각위치별 누적 cnt계산 
    res = max(c,res) # 최초위치별 누적 cnt중 최대값 산출 
print(5 - res) # 이어진수가 최댓값일 경우 필요한 카드는 최솟값 

'''
5
1
2
3
10
4

1

5개 숫자가 연속되도록 하여야 할 경우 필요한 최소 카드개수 
'''