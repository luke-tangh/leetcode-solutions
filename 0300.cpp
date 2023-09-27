#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int size = 0;
        vector<int> tails(nums.size(), 0);
        for(int k = 0; k < nums.size(); ++k) {
            int i = 0, j = size, x = nums[k];
            while(i != j) {
                int m = (i+j) / 2;
                if(tails[m] < x) {
                    i = m + 1;
                }else {
                    j = m;
                }
            }
            tails[i] = x;
            if(i == size) {
                ++size;
            }
        }
        return size;
    }
};