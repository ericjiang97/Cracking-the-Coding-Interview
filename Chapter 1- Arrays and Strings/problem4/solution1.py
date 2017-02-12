def linearSearch(array, target, position):
    for i in range(len(array)):
        if array[i][position] == target:
            return i
    return -1


def palinChk(string):
    strippedString = string.replace(' ', '')
    array=list(strippedString)
    tempArray = []
    for i in range(len(array)):
        search = linearSearch(tempArray,array[i],0)
        if search == -1:
            tempArray.append([array[i],1])
        else:
            tempArray[search][1] += 1

    if(len(string) % 2 == 0):
        #it is even, expect there to be no odd numbers
        for i in range(len(tempArray)):
            if(tempArray[i][1] % 2 == 1):
                return False
        return True
    else:
        #expect only 1 character to be even
        oddnumCount = 0
        for i in range(len(tempArray)):
            if(tempArray[i][1] % 2 == 1):
                if oddnumCount == 0:
                    oddnumCount += 1
                else:
                    return False
