#접근 : rotate,cal,res
def rotate(a):
    left = a[1:]
    right = a[:1]
    return left + right 

def cal(a,b):
    sum = 0 
    for i in range(n):
        sum += (a[i]-b[i])**2
    return sum 

def main():
    global res, n
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    res = int(1e9)
    for i in range(n):
        a = rotate(a)
        print(a)
        s = cal(a,b)
        if s < res:
            res = s
    print(res)

if __name__ == '__main__':
    main()

'''
3
1 2 3
4 3 2

5

차이값 계산 : A=(1,2,3),B=(4,3,2)일 때 (1-4)² + (2-3)²  + (3-2)²  = 11
배열이의 변경 : (1,2,3)→(2,3,1)→(3,1,2)→(1,2,3)→...

'''