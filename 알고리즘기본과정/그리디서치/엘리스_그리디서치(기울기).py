# 접근 : points.sort(), (y2-y1) / (x2-x1) / 디버깅 : x1,y1 = points[i-1], for i (1,n)
# 그리디서치
def maxSlope(points):
    res = 0 
    points.sort()
    for i in range(1,len(points)):
        x2,y2 = points[i]
        x1,y1 = points[i-1]
        sum = abs((y2-y1)/(x2-x1))
        res = max(sum,res)
    return res


def main():
    global n 
    n = int(input())
    points = []
    for i in range(n) :
        line = list(map(int,input().split()))
        points.append( (line[0], line[1]) ) # 튜플로 저장 
    # print("%.3lf" % maxSlope(points))
    print('{:.3f}'.format(maxSlope(points)))

if __name__ == "__main__":
    main()

# 완전탐색 : 이중 for문 O(n²) 10만 X 10만, 탐욕적기법 : O(logN) 정렬 
def maxSlope(points) :
    points.sort() # 정렬기준 (0==> 1 index순, 정렬이되어야 계산식이 맞게됨,Line Sweeping, 복잡도 줄이기위해졍렬)
    result = 0
    for i in range(1, len(points)):
        x2, y2 = points[i]
        x1, y1 = points[i - 1]
        result = max(result, abs((y2 - y1) / (x2 - x1)))
    return result
'''
4
0 3
1 1
2 2
4 1

2.000

2차원 평면에 
n개의 점이 있다. 이 점들 중에서 두 점을 선택했을 때, 그 기울기의 절댓값의 최댓값을 출력하는 프로그램을 작성하시오. 
단, 모든 점의 x좌표는 다르다고 가정한다. 또한, 두 점 (x1, y1), (x2, y2)의 기울기는 (y2 - y1) / (x2 - x1) 으로 정의된다.
예를 들어, 4개의 점이 각각 (0, 3), (1, 1), (2, 2), (4, 1) 에 위치해 있다고 하면, 기울기의 절댓값의 최댓값은 2가 된다.
이 경우 기울기 절댓값의 최댓값인 2를 출력합니다.
입력으로는 첫줄에 점의 개수가, 그 다음줄부터는 점의 x좌표와  y좌표가 입력됩니다.

'''