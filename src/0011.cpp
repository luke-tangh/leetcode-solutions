#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = 0, front = 0, end = height.size() - 1;
        while(end > front) {
            ans = max(ans, (end-front)*min(height[front], height[end]));
            height[front] < height[end] ? front += 1 : end -= 1;
        }
        return ans;
    }
};
