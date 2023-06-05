# 접근) Q, visited, while, cur, return False 에러) 곱셈 (제곱 x), 바이러스 시작점 : 1, Q.append (2), def main, return False

from collections import deque
def checkVirus(n):
    Q = deque([1])
    visited = [0 for i in range(10005)]
    visited[1] = 1
    while len(Q) > 0 : 
        cur = Q.popleft()
        if cur == n : 
            return True
        for i in [cur*2,cur//3]:
            if i == 0 or i >10000 or visited[i] != 0 :
                continue
            visited[i] = 1
            Q.append(i)
    return False

def main():
    m = int(input())
    print(checkVirus(m))

if __name__ == "__main__":
    main()

'''

10

True

바이러스

바이러스의 개체 수는 1초가 지날때마다 변화하는데, 그 개체수 변화 (2배 or 1/3배 증가) (예) cur : 10 --> 20, 3)
예를 들어, 현재 시간에 바이러스가 10마리라면, 1초 후에는 20마리가 될 수도 있고, 3마리가 될 수도 있습니다.
바이러스 수 <= 10000 (예) 7000 *2 = 140000 불가) 


엘리스 바이러스는 초기에 그 개체 수가 1개라고 할 때, 일정 시간이 지나면 특정한 개체수 m마리 도달 여부 
예) m = 10일 경우, 엘리스 바이러스의 개체 수가 10마리가 될 수 있는지 확인
1 -> 2 -> 4 -> 8 -> 16 -> 5 -> 10 (x2, x2 x2 x2, //3, x2)
start (개수) : 1개  --> m 마리까지 도달가능 return True or False 

Input)
10 (start = 1 )
Output)
True

'''