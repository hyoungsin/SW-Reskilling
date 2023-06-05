# https://www.acmicpc.net/problem/1018 (start지점 => b시작/w시작고려 => 8x8배열생성 => b으로 칠할위치/w으로 칠할위치)

n,m = map(int,input().split())
a = []
res = []
for i in range(n):
    a.append(list(input()))

for sr in range(n-7): # sr가 1개일경우 2개중 min값, sr x sc = 6일 경우 6*2 = 12건중 min값
    for sc in range(m-7):
        case1 = 0 # 시작점(0,0)이 black인 경우 
        case2 = 0 # 시작점(0,0)이 white인 경우

        for i in range(sr,sr+8): #8x8 map생성 
            for j in range(sc,sc+8):
                if (i+j) % 2 == 0: # 시작점 (0,0), (1,1)....시작점이 짝수인 경우 black으로 시작
                    if a[i][j] != 'B': # 시작점 black이 아닌경우 case.1 덧칠 추가
                        case1+= 1 
                    else:  # 시작점 white가 아니 경우 case.2 덧칠 추가
                        case2+=1

                else: # 시작점 (0,1)...시작점이 홀수인 경우로 시작 (짝수다음순서)  
                    if a[i][j] != 'W' :  # 다음순서가 White가 아닌경우 case.1 덧칠 추가
                        case1+=1 
                    else:  # 다음순서가 Black이 아닌경우 case.1 덧칠 추가
                        case2+=1 # 
        res.append(case1)
        res.append(case2)
print(min(res))
                        
'''
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

12

문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
'''