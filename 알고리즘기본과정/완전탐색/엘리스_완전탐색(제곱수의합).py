# 접근) cnt, i&j, break 디버깅) (1,n), (i,n) 

def main():
    n = int(input())
    cnt = 0
    for i in range(1,n):
        for j in range(i,n):
            if i**2 + j**2 > 50:
                break
            if i**2 + j**2 == 50:
                cnt+=1
    print(cnt)
    
if __name__ == "__main__":
    main()

'''
50

2
'''