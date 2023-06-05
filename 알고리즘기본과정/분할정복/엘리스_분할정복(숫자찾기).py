# 접근) n,a,  mid, len조건(n vs mid), [:mid],[mid+1:] 디버깅) binarySearch(a[:mid],n), len()//2 , return No 

def binarySearch(data, m) :
    mid = len(data)//2 
    if len(data) == 0 : 
        return 'No'
    elif data[mid] == m:
        return 'Yes'
    elif data[mid] > m: 
        return binarySearch(data[:mid],m)

    else:
        return binarySearch(data[mid+1:],m)

def main():
    a = list(map(int,input().split()))
    M= int(input())
    print(binarySearch(a,M))

if __name__ == '__main__':
    main()

'''
1 4 6 7 10 14 16
7

Yes

1≤n≤100,000 n개의 수 중에서, 
m이 존재하면 “Yes”, 존재하지 않으면 “No”를 반환하는 프로그램을 작성하세요.
'''