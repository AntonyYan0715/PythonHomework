class Message(object):
    def __init__(self, message: str, sender: int, receiver: int) -> None:
        self.message = message
        self.sender = sender
        self.receiver = receiver

    def __str__(self) -> str:
        return self.message
    
    def __eq__(self, __o: object) -> bool:
        return self.message == __o.message

def getMaxProfit(pnl, k):
    # Write your code here
    left = 0
    max_sum = 0
    res = pnl[0]
    length = len(pnl)
    
    for right in range(length):
        element = pnl[right]
        subarray_sum = element + max_sum
        
        if right - left >= k:
            subarray_sum -= pnl[left]
            left += 1
            
        max_sum = max(element, subarray_sum)
        res = max(res, max_sum) 
        
        if max_sum == element:
            left = right
            
    res2 = sum(pnl[:k-1])
    temp = res2
    
    for i in range(k-1, length):
        temp += pnl[i] - pnl[i-k+1]
        res2 = max(res2, temp)
        
    res = max(res, res2)
    return max(res, 0)

def getMinMoves(s):
    # Write your code here
    l = len(s)
    num = [ord(i) for i in s]
    moves = []
    moves.append(abs(num[0] - num[1]))
    
    if l == 2: return moves[-1]

    temp = num[:3]
    temp.sort()
    moves.append(abs(temp[1] - temp[0]) + abs(temp[2] - temp[1]))
    
    if l == 3: return moves[-1]

    moves.append(abs(num[1] - num[0]) + abs(num[3] - num[2]))
    
    if l == 4: return moves[-1]

    for i in range(4, l):
        temp = num[i-2:i+1]
        temp.sort()
        min1 = moves[i-4] + abs(temp[1] - temp[0]) + abs(temp[2] - temp[1])
        min2 = moves[i-3] + abs(num[i] - num[i-1])
        moves.append(min(min1, min2))
    
    return moves[-1]