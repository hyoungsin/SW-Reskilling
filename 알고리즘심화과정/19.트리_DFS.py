import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

global n, a, visited, d, graph, root

def dfs(cur): # root 노드부터 시작함 
    visited[cur] = 1
    child = 0 # 자식노드 개수 산출 
    cnt = 0  # 자식이 없는 경우 (자식개수 0인경우 cnt 누적)

    for next in deck[cur]: # 해당 deck에 자식이 있을 경우 반복 (예) 0,1 부모)
        if next == d: # 해당 node가 삭제한 node이면 무시 
            continue

        if visited[next] == 1: # 방문한 노드이면 무시 
            continue

        cnt += dfs(next)     # retur값 누적 (child == 0,자식이 없는경우만)
        child += 1      # for문을 돌았다는 뜻은 자식이 있다는 의미 

    if child == 0:  # 자식이 없으면 리프노드. return 하여 cnt에 숫자 더해주기
        return 1
    return cnt      # 리프 노드가 아닌 경우 리프 노드에서 카운팅하여 가져온 숫자 부모로 전달


def main():
    global n, a, visited, d, deck, root

    n = int(read().rstrip())
    a = list(map(int, read().rstrip().split()))
    visited = [0 for i in range(n)]
    d = int(read().rstrip())
    deck = [[] for i in range(n)] # 부모 노드를 저장할 deck 지정 

    for i in range(len(a)):
        if a[i] == -1: # 부모 노드가 -1이면 root 노드이다.
            root = i # 루트노드는 0번 노드이다.
            continue # 루트노드는 dfs 돌릴필요 없다. 
        deck[a[i]].append(i) # 부모노드(Deck)에 자식노드 추가 (예) 0번 deck에 1,2번 자식 노드 추가)

    if root == d: # 루트노드를 삭제할 경우 리프노드(자식없는 노드) 존재하지 않음 
        print(0)
        return

    print(dfs(root)) #루트노드부터 아래로 순회 

main()




'''
5
-1 0 0 1 1
2

2

문제
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 
노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

예를 들어, 다음과 같은 트리가 있다고 하자.



현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.



이제 리프 노드의 개수는 1개이다.

입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 
각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.
'''