#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.size() < 1) {
            return {-1, -1};
        }
        bool found = false, failed = false;
        int first = 0, mid = 0;
        int last = nums.size() - 1;
        while(!found && !failed) {
            mid = (first + last) / 2;
            if(nums[mid] == target) {
                found = true;
            }else {
                if(first >= last) {
                    failed = true;
                }else {
                    if(nums[mid] > target) {
                        last = mid - 1;
                    }else {
                        first = mid + 1;
                    }
                }
            }
        }
        if(found) {
            int left = mid, right = mid;
            while(left >= 0 && nums[left] == target) {
                left--;
            }
            while(right < nums.size() && nums[right] == target) {
                right++;
            }
            return {++left, --right};
        }
        return {-1, -1};
    }
};
