#접근 : 

from itertools import *
res = 1e9 #최소값반환
def cal():
    start = []
    link = []
    for i in range(1, N + 1): # 계산 편하게 하기 위해 팀원들 list로 나눔
        if visited[i]:# visited 표시 된 애들은 start 팀 아니면 link 팀
            start.append(i)
        else:
            link.append(i)
    start_stat = 0 # 능력치 산출변수 
    link_stat = 0

    for i in range(N // 2): #한팀당 3명 
        for j in range(N // 2):
            start_stat += stat[start[i]][start[j]]
            link_stat += stat[link[i]][link[j]]
    return abs(start_stat - link_stat)

def main():
    global N, stat, visited, res
    N = int(input())
    stat = [[]]  # 인덱스 1번부터 사용하기 위해 행 하나 껴넣음
    for i in range(N):
        temp = [0] + list(map(int,input().split())) # 인덱스 0번부터 사용하기 위해 0 하나 껴넣음
        stat.append(temp)
    comb = list(combinations(range(1, N + 1), N // 2))# itertools 사용해서 조합 구현
    for i in comb: # visited 다시 원복 시키기 어려워서 계속 새로 선언
        visited = [False for i in range(N + 1)]
        for j in i: # 조합에 선택된 애들 표시
            visited[j] = True
        res = min(cal(), res)
    print(res)

if __name__ == "__main__":
    main()

'''
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

2

오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.
BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다. (N=4이고, S가 아래와 같은 경우를 살펴보자.)

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 

예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.
스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

입력
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
'''