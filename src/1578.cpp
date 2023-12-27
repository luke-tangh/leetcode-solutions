#include <algorithm>
#include <numeric>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int ret = 0;
        int last = colors[0];
        vector<int> sliced = { neededTime[0] };

        for (int i = 1; i < colors.size(); ++i) {
            if (colors[i] == last) {
                sliced.push_back(neededTime[i]);
                continue;
            }

            if (sliced.size() > 1) {
                sort(sliced.begin(), sliced.end());
                sliced.pop_back();
                ret += accumulate(sliced.begin(), sliced.end(), 0);
            }

            sliced = { neededTime[i] };
            last = colors[i];
        }

        if (sliced.size() > 1) {
            sort(sliced.begin(), sliced.end());
            sliced.pop_back();
            ret += accumulate(sliced.begin(), sliced.end(), 0);
        }

        return ret;
    }
};
