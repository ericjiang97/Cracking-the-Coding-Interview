# Problem 4

_**Palindrome Permutation**: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase
that is the same forwards or backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary 
words_

---
# Thinking About the Problem
Let's be honest, we seriously can't really generator random permutations and try adnd work it out from there. There are several clues within the problem:
- a word or phrase that is the same forwards or backward
- A permutation is a rearrangement of letters

So these two hints give us a clue, so a palindrome must be the same backwards and forwards as well as permutation of the string A, must be a permutation of another string which is a permutation of string A. That being said, we can work it out. So, a palindrome must be the same backwards and forwards meaning they are symmetrical, or have the same number of letters/characters, or on the case of being odd, there must only be a letter with a odd number of characters. For example, ata (has 2 a's and 1 t's) and atta (has 2as and 2ts), the are both palindromes.
- have the same number of letters/characters

So the two conditions are:
- if the length of the string is **odd**
  - they must be 1 character with a odd number of characters (since tatat is also a palindrome)
  - every other character/letter must be even
- if the length of the string is **even**
  - every character/letter must be even
