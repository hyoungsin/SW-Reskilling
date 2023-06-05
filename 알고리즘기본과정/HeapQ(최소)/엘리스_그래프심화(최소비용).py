#접근)

from heapq import *
global V, E, graph, distance
INF = int(1e9)

def main():
    global V, E, graph, distance
    V = int(input())
    E = int(input())
    graph = [[] for i in range(V + 1)]
    distance = [INF for i in range(V + 1)]
    for i in range(E):
        from_edge, to_edge, cost = map(int,input().split())
        graph[from_edge].append((to_edge, cost))
    start, end = map(int,input().split())
    dijkstra(start, end)
    print(distance[end])

def dijkstra(start, end):# 다익스트라 그대로 사용
    global V, E, graph, distance
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0
    while len(pq) != 0:
        dist, cur = heappop(pq)
        if dist > distance[cur]:
            continue
        for vertex, distance_to_cur in graph[cur]:
            cost = dist + distance_to_cur
            if cost < distance[vertex]:
                heappush(pq, (cost, vertex))
                distance[vertex] = cost

if __name__ == '__main__':
    main()
'''

5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

4

문제
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

입력
N : 도시의 개수 N (1 ≤ N ≤ 1,000)
M : 버스의 개수 (1 ≤ M ≤ 100,000)
a : 버스정보(M개) 출발도시, 도착도시, 버스비용  (0보다 크고 100,000보다 작은 정수)

출력
출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
'''
