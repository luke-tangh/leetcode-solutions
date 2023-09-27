#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int temp = 101, p = 0;
        for(int i = 0; i < nums.size(); ++i) {
            if(temp == nums[i]) {
                continue;
            }else {
                nums[p] = nums[i];
                ++p;
            }
            temp = nums[i];
        }
        return p;
    }
};
