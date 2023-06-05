
# 접근) 
global V, E, edges, gender, parent
INF = int(1e9)
def main():
    global V, E, edges, gender, parent
    V, E = map(int,input().split())
    edges = []
    parent = [i for i in range(V + 1)]
    gender = [0] + input().split() # 성별 받을 리스트 추가

    for _ in range(E):
        from_node, to_node, cost = map(int,input().split())
        edges.append((cost, from_node, to_node))

    edges.sort()
    res = 0
    cnt = 0  # 경로의 길이가 V - 1개 만큼 나와야 됨

    for edge in edges:
        cost, from_node, to_node = edge
        if find_parent(from_node) != find_parent(to_node) and gender[from_node] != gender[to_node]:# 성별 같으면 안되므로 조건 추가
            union_parent(from_node, to_node)
            res += cost
            cnt += 1

    if cnt == V - 1:
        print(res)
    else:
        print(-1)

def find_parent(a):
    global V, E, edges, gender, parent
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a, b):
    global V, E, edges, gender, parent
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    main()
'''
5 7
M W W W M
1 2 12
1 3 10
4 2 5
5 2 5
2 5 10
3 4 3
5 4 7

34

사심경로
1.남초 대학교와 여초 대학교들을 연결하는 도로로만 이루어져 있다.
2.모든 대학교 연결되어 있음 
3.시간을 낭비하지 않고 미팅할 수 있도록 이 경로의 길이는 최단 거리 산출

입력
입력의 첫째 줄에 학교의 수 N와 학교를 연결하는 도로의 개수 M이 주어진다. (2 ≤ N ≤ 1,000) (1 ≤ M ≤ 10,000)
M : 남초 대학교, W : 여초 대학교
u,v,d : from, to , 거리 (1 ≤ u, v ≤ N) , (1 ≤ d ≤ 1,000)

출력
깽미가 만든 앱의 경로 길이를 출력한다. (모든 학교를 연결하는 경로가 없을 경우 -1을 출력한다. --> 연결이되어 있지 않은 대학교의 경우)
'''