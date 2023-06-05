# 접근 : 

from collections import deque
def bfs():
    Q = deque([N])
    visited[N] = 1
    while len(Q)>0:
        cur = Q.popleft()
        if cur == K:
            return visited[cur] -1 # 출력값 
        for i in [cur+1,cur-1,cur*3]:
            if i > 100000 or i <0 or visited[i] !=0:
                continue
            Q.append(i)
            visited[i] = visited[cur] +1
def main():
    global N, K, visited
    N, K = map(int, input().split())
    visited = [0 for i in range(100004)]
    print(bfs())

if __name__ == "__main__":
    main()

'''
5 17

3
'''