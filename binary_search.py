def binarySearch(array, item): 
    maxPosition = len(array) - 1
    minPosition = 0

    while(minPosition <= maxPosition):
        half = (minPosition + maxPosition)//2
        trying = array[half]
        if(trying == item):
            return item
        if(trying < item):
            minPosition = half + 1
        else:
            maxPosition = half - 1
    return None