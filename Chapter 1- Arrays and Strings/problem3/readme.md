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
