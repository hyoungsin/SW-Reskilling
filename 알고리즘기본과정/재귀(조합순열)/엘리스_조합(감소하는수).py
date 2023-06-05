# 접근 : comb, 최소값 (0), 최대값 (9876543210), 자리수 범위 (1~10)숫자범위(0~9), sort/reverse,디버깅 : 

from itertools import combinations
n = int(input())
res = [] # 모든 감소하는 수

for i in range(1, 10): #  1~10개의 조합 만들기 (0~9개니깐)
    # print(i)
    for comb in combinations([0,1,2,3,4,5,6,7,8,9], i): # 0~9로 하나씩 조합 만들기
        # print('comb',comb)
        comb = list(comb)
        comb.sort(reverse=True) # 해당 조합을 감소하는 수로 변경
        # print(comb)
        res.append(int("".join(map(str, comb))))

res.sort()   # 오름차순

try:
    print(res[n])
except:     # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)

'''

18

42

문제
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 
예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. 
N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 

0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 
만약 N번째 감소하는 수가 없다면 -1을 출력한다.

입력
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 N번째 감소하는 수를 출력한다.
'''