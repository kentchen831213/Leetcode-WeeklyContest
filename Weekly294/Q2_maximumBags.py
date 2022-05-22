class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        remain = []
        res = 0
        
        for i in range(len(capacity)):
            remain.append(capacity[i]-rocks[i])
            
        remain.sort()
        
        for i in range(len(remain)):
            if remain[i] == 0:
                res+=1
            elif additionalRocks >= remain[i]:
                additionalRocks -= remain[i]
                res += 1
            elif additionalRocks < remain[i]:
                break
        return res