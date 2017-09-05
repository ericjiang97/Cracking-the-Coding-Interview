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