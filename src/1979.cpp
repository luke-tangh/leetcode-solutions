#include <vector>

using namespace std;

class Solution {
public:
    int findGCD(vector<int>& nums) {
        int max = 0, min = 1001;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] > max) {
                max = nums[i];
            }
            if(nums[i] < min){
                min = nums[i];
            }
        }
        for(int i = max; i > 0; --i) {
            if(max % i == 0 and min % i == 0) {
                return i;
            }
        }
        return 1;
    }
};