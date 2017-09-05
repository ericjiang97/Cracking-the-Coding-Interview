def numberOfWays(steps):
    if(steps <= 0):
        return 0
    elif(steps == 1):
        return 1
    else:
        return numberOfWays(steps-1)+numberOfWays(steps-2)+numberOfWays(steps-3)