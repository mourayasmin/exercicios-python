#input: 2 3 4
#output: 9

def simpleArraySum(ar):
    result = 0
    for i in range(len(ar)):
        result += ar[i]
    return result

if __name__ == '__main__':
    ar = [int(x) for x in input(). split()]
    result = simpleArraySum(ar)
    print(result)