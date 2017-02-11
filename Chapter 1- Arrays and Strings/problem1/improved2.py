def isUnique(string):
    charStore = []
    for i in string:
        if(i.lower() not in charStore):
            charStore.append(i.lower())
        else:
            return False
    return True
