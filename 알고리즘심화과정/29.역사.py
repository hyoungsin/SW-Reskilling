
import sys
read = sys.stdin.readline

def main():
    N, M = map(int, read().split()) # 노드(N),간선(K) 
    # visited = [[0 for i in range(N+1)]for j in range(N+1)] # update 편하기위해 패딩 index추가 
    visited = [[0]*(N+1) for _ in range(N+1)]

    for i in range(M): # 간선 정보 update
        x, y = map(int, read().split()) 
        
        # print('x,y:',x,y)

        visited[x][y] = 1 # 앞에 번호가 먼저 일어난 경우 1로 update (출력값 은 -1 )

    for k in range(1, N + 1): # 1 ~ 5번노드 통과 Case추가 (패딩 고려)
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                # if visited[i][k] + visited[k][j] == 2: #i와 k도 선후 관계 명확한 경우 1로 update (선/후)
                if visited[i][k] and visited[k][j]: #i와 k도 선후 관계 명확한 경우 1로 update (선/후)
                
                    # print('i,j,k:',i,j,k)
                
                    visited[i][j] = 1

    K = int(input())
    for i in range(K):
        p, q = map(int, read().split()) 
        if visited[p][q] == 1: # 만약 해당좌표가 1로 되어 있으면 선후관계 (-1 출력)
            print(-1)
        elif visited[q][p] == 1: # 만약 앞뒤를 바꿔서 선후 관계면 (1 출력)
            print(1)
        else: # 그외 정보가 없을 경우 0 
            print(0)
            
main()

'''
5 5
1 2
1 3
2 3
3 4
2 4
3
1 5
2 4
3 1

0
-1
1

문제
역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 
즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.

세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 
주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.

입력
첫째 줄에 첫 줄에 사건의 개수 n(400 이하의 자연수)과 알고 있는 사건의 전후 관계의 개수 k(50,000 이하의 자연수)가 주어진다. 
다음 k줄에는 전후 관계를 알고 있는 두 사건의 번호가 주어진다. 이는 앞에 있는 번호의 사건이 뒤에 있는 번호의 사건보다 먼저 일어났음을 의미한다. 
물론 사건의 전후 관계가 모순인 경우는 없다. 
다음에는 사건의 전후 관계를 알고 싶은 사건 쌍의 수 s(50,000 이하의 자연수)이 주어진다. 
다음 s줄에는 각각 서로 다른 두 사건의 번호가 주어진다. 사건의 번호는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
s줄에 걸쳐 물음에 답한다. 각 줄에 만일 앞에 있는 번호의 사건이 먼저 일어났으면 -1, 뒤에 있는 번호의 사건이 먼저 일어났으면 1, 
어떤지 모르면(유추할 수 없으면) 0을 출력한다.
'''