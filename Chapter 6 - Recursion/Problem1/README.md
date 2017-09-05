# Problem 1
A child is running up a staircase with `n` steps and can hop 1, 2 or 3 steps at a time. Implement a method that can calculate how many ways the child can climb up the staircase.

## Finding a Solution
The first step is to find a basic recursive (or iterative) solution, then expand and improve it's complexity.

There are two base cases: When (n<=0) and (n=1), so when n <= 0, we should return 0. and when n=1, we should return 1.

```python
def numberOfWays(steps):
    if(steps <= 0):
        return 0
    elif(steps == 1):
        return 1
    else:
        return numberOfWays(steps-1)+numberOfWays(steps-2)+numberOfWays(steps-3)
```

## Optimising it through Dynamic Programming
Well, we can dramatically improve it through DP. So we need a memorisation table.

```python
def countNumOfWays(steps, memo):
    if(steps <= 0):
        return 0
    elif(steps == 1):
        return 1
    elif(memo[steps] != -1):
        return memo[steps]       #retrieval step, if value was already calculated get previous value
    else:
        memo[steps] = numberOfWays(steps-1)+numberOfWays(steps-2)+numberOfWays(steps-3)
        return memo[steps]

def numberOfWays(steps):
    # build memo table
    memo = [-1 for x in range(steps)]
    return countNumOfWays(steps, memo)[-1] # record is at the end of the array
```