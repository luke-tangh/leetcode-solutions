#include <vector>

class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int front = 0, tail = nums.size() - 1, count = 0;
        sort(nums.begin(), nums.end());
        while(tail > front) {
            if(nums[front] + nums[tail] < target) {
                count += tail - front;
                front++;
            }else {
                tail--;
            }
        }
        return count;
    }
};
