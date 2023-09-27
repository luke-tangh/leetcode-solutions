#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        intervals.push_back(newInterval);
        return merge(intervals);
    }
    
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<int> temp = intervals[0];
        vector<vector<int>> ans;
        for(int i = 0; i < intervals.size()-1; ++i) {
            if(temp[1] >= intervals[i+1][0]) {
                temp[0] = min(temp[0], intervals[i][0]);
                temp[1] = max(temp[1], intervals[i+1][1]);
            }else {
                ans.push_back(temp);
                temp = intervals[i+1];
            }
        }
        ans.push_back(temp);
        return ans;
    }
};