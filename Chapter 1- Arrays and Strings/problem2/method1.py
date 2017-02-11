def permutation(stringA, stringB):
    listA = list(stringA)
    listB = list(stringB)
    listA.sort()
    listB.sort()
    if(listA != listB):
        return False
    else:
        return True
