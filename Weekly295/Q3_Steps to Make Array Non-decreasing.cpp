#include <vector>

class Solution{
public:
    int totalSteps(vector<int>& nums){
        int n = nums.size(), res= 0;
        vector<int> dp(n), stack;
        for(int i = n-1;i>=0;--i){
            while(!stack.empty() && nums[i]>nums[sack.back()]){
                dp[i] =max( ++dp[i], dp[stack.back()] );
                stack.pop_back();
                res = max(res,dp[i];)
            }
            stack.push_back();
        }
        return res;
    }
    vector<int> vect{5,3,4,4,7,3,6,11,8,5,11};
    int ans = totalSteps(vect);
    cout << ans;
}