#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> num_count;
        for(int i = 0; i < nums.size(); ++i) {
            if(num_count.count(nums[i])) {
                num_count[nums[i]] += 1;
            }else {
                num_count[nums[i]] = 1;
            }
        }
        int key = 0, maxval = 0;
        for(pair<const int, int> & kv:num_count) {
            if(kv.second > maxval) {
                maxval = kv.second;
                key = kv.first;
            }
        }
        return key;
    }
};