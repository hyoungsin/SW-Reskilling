
# 접근 : pivot,len(a), left/right, a[1:] 디버깅 : sortAbs(), a[1:] (2)

def sortAbs(a):
    if len(a) <= 1: # 기저조건 , 1개이하면 정렬대상없음, 밑에조건 수행을위해서위에
        return a
    pivot = a[0] # pivot, left,right
    left = []
    right = []
    for i in a[1:]: #pivot을 제외하고 left / right 재귀함수 돌림 
        if abs(i) < abs(pivot):
            left.append(i)
        elif abs(i) == abs(pivot) and i < pivot:
            left.append(i)
        else:
            right.append(i)
    return sortAbs(left)+[pivot]+sortAbs(right) #기저함수추가   

def main():
    a = list(map(int,input().split()))
    for i in sortAbs(a):
        print(i,end= ' ')

if __name__ == "__main__":
    main()

'''
-2 1 3 9 -5 6 7 -3

1 -2 -3 3 -5 6 7 9

n개의 숫자가 주어질 때, 이를 절댓값을 기준으로 오름차순 정렬하는 Quick sort 프로그램을 작성하세요. 
(만약 두 수의 절댓값이 같다면,더 작은 숫자를 앞에 정렬)
'''
