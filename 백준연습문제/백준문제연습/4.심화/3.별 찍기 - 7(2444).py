
# 심화 (역행렬)
# n = int(input())
# for i in range(n):
#     print(' '*(n-i-1) + '*'*(2*i+1))

# for i in range(n-1,0,-1):
#     print(' '*(n-i) + '*'*(2*i-1))

#이중포문

n = int(input())
for i in range(n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i*2-1):
        print("*", end='')
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i*2-1):
        print("*", end='')
    print()


'''
5

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2xN-1번째 줄까지 차례대로 별을 출력한다.
'''