class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        vector<int> c;
        
        int atFull = 0;
        int diff;
        
        for (int i = 0; i < capacity.size(); i++) {
            diff = capacity[i] - rocks[i];
            if (diff == 0) {
                ++atFull;
                continue;
            }
            
            c.push_back(diff);
        }
        
        sort(c.begin(), c.end());
        
        for(int i = 0; i < c.size(); i++) {
            additionalRocks -= c[i];
            if (additionalRocks < 0) {
                return atFull;
            } else if (additionalRocks > 0) {
                ++atFull;
                continue;
            }
            ++atFull;
            break;
        }
        return atFull;
    }
};