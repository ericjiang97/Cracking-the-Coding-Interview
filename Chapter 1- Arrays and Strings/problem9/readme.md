# Problem 9
_**String Rotation**: Assume you have a method `isSubstring` which checks if one word is substring of another. Given two strings, 
`s1` and `s2`, write code to check if `s2` is a rotation of `s1` using one call to `isSubstring` (e.g. "waterbottle" is a rotation 
of "erbottlewat"_

---
_To be honest, this algorithm took way too long for me to figure out, well I sort of knew what to do, but writing it out was fairly difficult and thanks to the beauty of Python, where I can specify `string[j:k]` to get a part of the string, I sort of am lucky, but if I was using another language such as JavaScript or Java (or C#), this would have taken way longer_

# Planning to write.
The main idea is simple set one of the strings to be your base string to compare against. In my case I used `s2` against `s1`.

for example
```
s2: |w|aterbottle => w|a|terbottle => wa|t|erbottle => wa|te|rbottle => |wa|terbottle| 
s1: |t|erbottlewa => |t|erbottlewa => |t|erbottlewa => |terbottlewa|
```
So look at s2 for example, we can bascially make `wa` + `terbottle` into something like `terbottlewa`, which is EQUAL to s1.

But we need to loop through s2, in order to make sure its unique

# Coding it Up
```
def subString(s1,s2):
    begin = s1[0]
    for j in range(len(s1)):
        if(s2[j] == begin):
            if((str(s2[j:len(s2)])+str(s2[0:j]))==str(s1)):
                return True
    return False


```
But there is some problems with this solution, first of all the length of `s1` has to equal the length of `s2`.

```
def subString(s1,s2):
    begin = s1[0]
    if(len(s1)==len(s2)):
        for j in range(len(s2)):
            print(j, s2[j])
            if(s2[j] == begin):
                if((str(s2[j:len(s2)])+str(s2[0:j]))==str(s1)):
                    return True
        return False
    else:
        return False
    
print(subString("waterbottle","ttlewaterbo"))
```
