# 접근 : sorted(reverse,리버스), weight/value, cur_weight/value, 디버깅 : materials[i][0]

def fKnapsack(materials, m):
    materials = sorted(materials,key = lambda x : x[1]/x[0],reverse=True)
    weight = 0
    value = 0 
    for i in materials: 
        cur_weight = i[0]
        cur_value = i[1]
        if weight + cur_weight <= m:
            weight += cur_weight
            value += cur_value
            if weight+cur_weight == m:
                return value
    else:
        value +=  (m-weight)* (cur_value/cur_weight)
        return value 

def main():
    line = list(map(int,input().split()))
    n = line[0]
    m = line[1]
    materials = []

    for i in range(n) :
        data = list(map(int,input().split()))
        materials.append( (data[0], data[1]) )
    print('{:.3f}'.format(fKnapsack(materials, m)))

if __name__ == "__main__":
    main()

'''
4 10
3 10
2 7
4 9
5 13

30.000

입력 : 돌멩이의 무게와 가치 
출력 : 배낭에 담을수 있는 최댓값

'''