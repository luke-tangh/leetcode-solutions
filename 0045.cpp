#include <vector>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size() - 1, i = 0;
        int jumps = 0, max_idx = 0, last_jump = 0;
        while(last_jump < n) {
            max_idx = max(max_idx, i + nums[i]);
            if(i == last_jump) {
                last_jump = max_idx;
                jumps++;
            }
            i++;
        }
        return jumps;
    }
};
