#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](auto &left, auto &right) {
            return left[0] < right[0];
        });
        int diff = 0;
        for (int i = 1; i < points.size(); ++i) {
            diff = max(diff, points[i][0] - points[i - 1][0]);
        }
        return diff;
    }
};
