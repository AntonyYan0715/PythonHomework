import math

def countPowerNumbers(l, r):
    # Write your code here
    powers = [0, 1]
    
    for i in range(2, int(math.sqrt(r)) + 1):
        limit = int(math.log(r, i)) + 1
        
        for j in range(2, limit):
            powers.append(i ** j)
    
    powers = list(set(powers))
    
    isPowerNum = []
    
    for a in powers:
        for b in powers:
            num = a + b
            if num >= l and num <= r:
                isPowerNum.append(num)
    
    isPowerNum = set(isPowerNum)
    return len(isPowerNum)

