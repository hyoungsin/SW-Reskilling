
'''
1.원형으로 1번부터 N번까지 풍선이 붙어있음(시계방향)
2.1번풍선은 1번, 2번풍선은 2번, 3번풍선은 3번 
3.1번풍선을 맞춤 
4.M개를 지나침 (2번이동)
5.현재보고 있는 풍선 맞춤
6.반복 
'''
import sys
read = sys.stdin.readline


N,M = map(int,read().rstrip().split())
A = list(map(int,input().split()))
from collections import deque 
Q = deque([[i,jump]for i,jump in enumerate(A,1)])

print(Q)

res = [ ]
while len(Q) > 0 : 
    Q[0][1] -= 1 # 1번숫자 1차감 
    if Q[0][1] == 0: # 첫번째 풍선이 0이면 
        res.append(Q.popleft()[0]) #해당번호를 res에 담음 
        Q.rotate(-M)
    else:
        Q.rotate(-(M+1)) #(pop포함시 3개이므로 pop안된 상태에서 아래 로직 적용하려면 1개 먼저 이동필요)

print(*res)

'''
4 2
1 4 2 3

1 4 3 2
'''