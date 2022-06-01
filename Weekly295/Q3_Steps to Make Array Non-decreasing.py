class Solution:

    def totalSteps(nums)-> int:
        
        n = len(nums)
        dp = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[i]>nums[stack[-1]]:
                dp[i]=max(dp[i]+1,dp[stack.pop()])
            stack.append(i)
        return max(dp)

if __name__ == "__main__":
    
    #test1 = Solution([5,3,4,4,7,3,6,11,8,5,11])
    test1 = [5,3,4,4,7,3,6,11,8,5,11]
    test2 = [10,1,2,9,1,2,3,4]

    
    res = Solution.totalSteps(test2)
    print(res)

