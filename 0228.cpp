#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        if(nums.size() == 0) {
            return ans;
        }
        int start = nums[0], end = nums[0];
        for(int i = 1; i < nums.size(); ++i){
            if(nums[i] == end+1) {
                end += 1;
                continue;
            }else {
                if(start == end) {
                    ans.push_back(to_string(start));
                }else {
                    ans.push_back(to_string(start) + "->" + to_string(end));
                }
                start = nums[i];
                end = nums[i];
            }
        }
        if(nums[nums.size()-1] == end and start != end) {
            ans.push_back(to_string(start) + "->" + to_string(end));
        }else {
            ans.push_back(to_string(nums[nums.size()-1]));
        }
        return ans;
    }
};