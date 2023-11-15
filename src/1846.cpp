#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int prev = 0;
        for (int i = 0; i < arr.size(); ++i) {
            if (arr[i] > prev) {
                arr[i] = prev + 1;
            }
            prev = arr[i];
        }
        return arr.back();
    }
};
