# Problem 2
_Given two strings, write a method to decide if one is a permutation of the other._

```
def permutation(stringA, stringB):
    listA = list(stringA)
    listB = list(stringB)
    listA.sort()
    listB.sort()
    if(listA != listB):
        return False
    else:
        return True

```
