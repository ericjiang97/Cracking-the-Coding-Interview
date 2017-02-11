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

Well, lets be honest we can improve this further, instead of checking at the end (which would make the complexity `O(n)`, we can instead check it as we go making it say No, once it finds a repeared letter. which makes it smaller than `O(n)`, but not considerably.
```
def isUnique(string):
    charStore = []
    for i in string:
        if(i.lower() not in charStore):
            charStore.append(i.lower())
        else:
            return False
    return True
```

---
Now say we cant use data-structures, the obvious way to do it is to compare character by character, through 2-loops, which makes the complexity `O(n^2)`. For example
```
def isUnique(string):
    for i in range(0, len(string)):
        for j in range(1, len(string)):
            if(j!= i and string[i]==string[j]):
                return False
    return True
```
