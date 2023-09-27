#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int unequalTriplets(vector<int>& nums) {
        int count = 0;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); ++i) {
            for(int j = i; j < nums.size(); ++j) {
                for(int k = j; k < nums.size(); ++k) {
                    if(nums[i] != nums[j] && nums[i] != nums[k] && nums[j] != nums[k]) {
                        count += 1;
                    }
                }
            }
        }
        return count;
    }
};
