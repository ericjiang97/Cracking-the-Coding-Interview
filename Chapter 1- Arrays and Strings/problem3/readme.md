# Problem 3

```
def URLify(string):
    arrayStore = string.split()
    url = ""
    for i in range(len(arrayStore)):
        url += arrayStore[i]
        if i != (len(arrayStore)-1):
            url += "%20"
    return url
```
This problem is in fact very easy, e.g. map it into a dictionary then add the string "%20" to everything excpet for the last string.
Otherwise just append. This has a `O(n)` complexity.
