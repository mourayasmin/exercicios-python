def aVeryBigSum(ar):
    result = 0
    for i in range(len(ar)):
        result += ar[i]
    
    return result


if __name__ == '__main__':
    n = int(input())
    ar = [int(x) for x in input().split()]
    print(n)
    result = aVeryBigSum(ar)

    print(result)