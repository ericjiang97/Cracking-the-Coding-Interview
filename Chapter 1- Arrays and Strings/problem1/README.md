# Problem 1
_Is Unique - Implement an algorithm to determine if a string has all unique characters. What if you cant use additional data structures?_

Well, python has a `set()` function, if using that you can do something like:
```
def isUnique(string):
  if(len(set(string)) == len(string):
    return True
  else:
    return False
```
The problem with the above one is that in the case of where the problem specifies for Upper Case = Lower Case, then it doesn't work. So we need to construct a dictionary (or an array):

```
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
```

