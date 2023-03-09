# Q1
def removeNodes(listHead, x):
    # Write your code here
    temp = listHead
    prev = None
    
    while (temp != None) and (temp.data > x):
        prev = temp
        temp = temp.next
    
    listHead = temp
    
    if temp != None:
        
        while (temp.next != None):
            if temp.data > x:
                prev.next = temp.next
                temp = temp.next
            
            else:
                prev = temp
                temp = temp.next
        
        if temp.data > x:
            prev.next = None
        
    return listHead


# Q2
'''
def shortestSubstring(givenString):
    # Write your code here
    result = len(givenString)
    character_set = set(givenString)
    
    for i in range(len(givenString)):
        character_list = []
        character_list.append(givenString[i])
        
        for j in range(i+1, len(givenString)):
            if set(character_list) == character_set:
                if len(character_list) < result:
                    result = len(character_list)
            else:
                character_list.append(givenString[j])
        
        if set(character_list) == character_set:
            if len(character_list) < result:
                result = len(character_list)
    
    return result
'''

def shortestSubstring(givenString):
    n = len(givenString)
    size = len(set(givenString))
    result = n
    
    for i in range(n):
        count = 0
        visit = [0 for _ in range(256)]
        sub_str = ''
        
        for j in range(i, n):
            if visit[ord(givenString[j])] == 0:
                count += 1
                visit[ord(givenString[j])] = 1
            
            sub_str += givenString[j]

            if count == size:
                if len(sub_str) < result:
                    result = len(sub_str)
                break
    
    return result


# Q3
def efficientJanitor(weight):
    # Write your code here
    weight.sort(reverse = True)
    heavy = 0
    light = len(weight) - 1
    trip = 0
    
    while heavy < light:
        trip += 1
        if weight[heavy] + weight[light] <= 3:
            light -= 1
        heavy += 1
    
    if heavy == light:
        trip += 1
    
    return trip


# Q4
def pthFactor(n, p):
    # Write your code here
    factors = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n/i)
    
    factors = sorted(list(set(factors)))
    print(factors)
    if p > len(factors):
        return 0
    else:
        return int(factors[p - 1])


# Q5
def maxXor(lo, hi, k):
    # Write your code here
    result = []
    
    for i in range(lo, hi):
        curr = i
        
        for j in range(curr+1, hi+1):
            temp = i^j
            if temp <= k:
                result.append(temp)
    
    return max(result)


# Q6
def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here
    price_dict = {}
    errors = 0
    
    for i in range(len(products)):
        price_dict[products[i]] = productPrices[i]
    
    for j in range(len(productSold)):
        name = productSold[j]
        price = soldPrice[j]
        
        if price_dict[name] != price:
            errors += 1
    
    return errors