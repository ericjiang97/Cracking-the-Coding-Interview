# Problem 6
_**String Compression** implement a method to perform basic string compression using the counts of repeated charactrs. For example the string ``aabcccccaa` would become `a2b1c5a3`.
If the compressed string is not smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z)_

---

# Method 1
Here's a really messy way of doing it, but since its one of the first methods of doing it. We can really do some messy code.

```
def comp(string):
    returnString = ""
    currentCharacter = string[0]
    count = 0 # reset count
    for i in range(len(string)):
        
        # aaaaaaabbbbbcccc
        # ^      ^
        # e.g. two loops
        if(string[i] == currentCharacter):
            count = count + 1
            print(count)
        else:
            print(string[i], str(count), currentCharacter)
            returnString += currentCharacter + str(count)
            currentCharacter = string[i]
            count = 1

    returnString += currentCharacter + str(count)
    if(len(returnString) < len(string)):
        return returnString
    else:
        return string
```
So the idea is to firstly, loop through and compare with the current character, say for the string `aabbbcca`

So initially we set
```
aabbbcca
^
c

Count = 1, Current Letter: 'a', returnString = ""
```
_With `c` being currentCharacter_ 
and then
```
aabbbcca
 ^
c

Count = 2, Current Letter: 'a', returnString = ""
```
following
```
aabbbcca
  ^
c

Count = 2, Current Letter: 'a', returnString = a2
```
and so on...
