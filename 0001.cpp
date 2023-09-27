#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> idict;
        for(int i = 0; i < nums.size(); ++i) {
            int n = nums[i];
            if(idict.count(target-n) != 0) {
                return { idict[target-n], i };
            }else {
                idict[n] = i;
            }
        }
        return {};
    }
};
