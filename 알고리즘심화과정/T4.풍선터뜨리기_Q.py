# rotate

from collections import deque

n,m = map(int, input().split())
li = []
for i, baloon in enumerate(map(int, input().split()), 1):
    li.append([i,baloon])

Q = deque(li)

# Q = deque([i, baloon] for i, baloon in enumerate(map(int, input().split()), 1)) # index 1부터 [1,1],[2,4],[3,2],[4,3]
print(Q)

res = []
while len(Q) > 0 : # Q에숫자(리스트)가 있을때까지 

    Q[0][1] -= 1 # 1번숫자 1차감 
    if Q[0][1] == 0: # 첫번째 풍선이 0이면 
        res.append(Q.popleft()[0]) #해당번호를 res에 담음 
    else:
        Q.rotate(-1) #(pop포함시 3개이므로 pop안된 상태에서 아래 로직 적용하려면 1개 먼저 이동필요)
        # print(Q)
    Q.rotate(-m) #Q 를 왼쪽으로 돌려서 3번째 요소를 접근 (m=2) pop 제외하고 2칸임 (pop 포함시 3개)

print(*res)