import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,read().rstrip().split())
key = []
lock = []

def rotate(key):
    # 키를 시계 방향으로 90도 회전시키는 함수
    n = len(key)
    new_key = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_key[j][n-i-1] = key[i][j]
    return new_key

def check(lock):
    # 자물쇠의 중간 부분이 모두 1인지 확인하는 함수
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True

def main(key, lock):
    n = int(input())
    m = int(input())
    # 자물쇠의 크기를 3배로 만들어서 가운데에 두고 시작
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 4번 회전시키면서 확인
    for _ in range(4):
        key = rotate(key)
        for i in range(n*2):
            for j in range(n*2):
                # 열쇠를 자물쇠에 삽입
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]
                # 자물쇠의 중앙 부분이 모두 1이면 True 반환
                if check(new_lock):
                    return True
                # 열쇠를 다시 빼기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
    # 모든 경우를 다 확인한 후에도 자물쇠를 열 수 없으면 False 반환
    return False

main()

'''
3
0 0 0
1 0 0
0 1 1
3
1 1 1
1 1 0 
1 0 1

true

key를 시계 방향으로 90도 회전하고, 오른쪽으로 한 칸, 아래로 한 칸 이동하면 lock의 홈 부분을 정확히 모두 채울 수 있습니다.

고고학자인 "튜브"는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 
런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 
푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 
열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 
돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 
열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 
정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 
열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.


key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.

'''