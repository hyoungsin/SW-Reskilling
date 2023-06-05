import sys
read = sys.stdin.readline
INF = 1e9


def main():
    V, E = map(int, read().rstrip().split())    # V가 정점, E가 간선
    # 모든 정점에 대해 무한으로 초기화. graph[i][j] = x는 i에서 j까지 가는데 x만큼 걸린다는 것을 의미
    graph = [[INF for _ in range(V + 1)] for _ in range(V + 1)]

    # 자기 자신까지 도달하는데 필요한 거리는 0
    for i in range(V + 1):
        graph[i][i] = 0

    for _ in range(E):
        start, end, dist = map(int, read().rstrip().split())
        # start부터 end까지 가는데 dist 만큼 걸림
        graph[start][end] = dist

    # 다이나믹 프로그래밍
    # i에서 j까지 가는데 원래 경로와 k를 거쳐서 가는 경로 중 짧은 경로를 저장
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, V + 1):
        for j in range(1, V + 1):
            print(graph[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()


'''
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''