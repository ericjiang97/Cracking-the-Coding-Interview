def isUnique(string):
    charStore = []
    for i in string:
        if(i not in charStore):
            charStore.append(i.lower())

    if(len(charStore) != len(string)):
        return False
        # This works since we append the non-repeated values
        # in our dictionary (charStore)
    else:
        return True
