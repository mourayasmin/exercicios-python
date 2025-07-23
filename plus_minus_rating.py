def plusMinusRating(array, n):
    pos = 0
    neg = 0 
    zero = 0
    for i in range(len(array)):
        if(array[i] > 0):
            pos += 1
        elif(array[i] < 0):
            neg += 1
        elif(array == 0):
            zero += 1
    result = [f"{pos/n:.6f}", f"{neg/n:.6f}", f"{zero/n:.6f}"]
    for x in range(len(result)):
        print(result[x])

if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]

    plusMinusRating(array, n)