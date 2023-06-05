'''
접근 : res(-1e9), sum, i&j --> data[j], i --> data, 디버깅: sum += i 
'''
def getSubsum(data): 
    res = -1e9
    for i in range(len(data)):
        sum = 0 
        for j in range(i,len(data)):
            sum += data[j]
            res = max(res,sum)
    return res

def main():
   data = [int(x) for x in input().split()]
   print(getSubsum(data))

if __name__ == "__main__":
    main()

'''
1 2 -4 5 3 -2 9 -10

15

'''