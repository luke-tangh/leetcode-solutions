#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ret;
        int n = nums.size();
        int i, j, k;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n-2; ++i) {
            if(i && nums[i] == nums[i-1]) {
                continue;
            }
            j = i + 1;
            k = n - 1;
            while(j < k) {
                int target = nums[i] + nums[j] + nums[k];
                if(target > 0) {
                    k--;
                }else if(target < 0) {
                    j++;
                }else {
                    ret.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                    while(j < k && nums[j] == nums[j-1]) {
                        j++;
                    }
                    while(j < k && nums[k] == nums[k+1]) {
                        k--;
                    }
                }
            }
        }
        return ret;
    }
};
