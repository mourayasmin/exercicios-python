#input: 1 2 3
#       2 3 1
#output: (1, 2)

def compareTriplets(a, b):
    aPoints = 0
    bPoints = 0
    for i in range(3):
        if(a[i] > b[i]):
            aPoints += 1
        if(a[i] < b[i]):
            bPoints += 1

    return aPoints, bPoints

if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    result = compareTriplets(a, b)

    print(result)