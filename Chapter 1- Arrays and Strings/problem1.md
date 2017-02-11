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



