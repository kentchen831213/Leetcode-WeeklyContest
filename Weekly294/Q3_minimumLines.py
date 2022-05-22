class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        
        if len(stockPrices) == 1: return 0
        if len(stockPrices) == 2: return 1
        
        stockPrices.sort()
        res = 1
        changex = stockPrices[1][0]-stockPrices[0][0]
        changey = stockPrices[1][1]-stockPrices[0][1]


        for i in range(2, len(stockPrices)):
            curx = stockPrices[i][0]-stockPrices[i-1][0]
            cury = stockPrices[i][1]-stockPrices[i-1][1]
            
            if curx * changey == cury * changex:
                continue
            else:
                res+=1
                changex = curx
                changey = cury
        return res