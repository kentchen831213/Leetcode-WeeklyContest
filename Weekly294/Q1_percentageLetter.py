class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        num = 0
        for c in s:
            if c == letter:
                num+=1
        res = num/len(s)
        res = res*100
        return int(res)