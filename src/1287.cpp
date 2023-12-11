#include <vector>

using namespace std;

class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int t = arr.size() / 4;
        for (int i = 0; i < arr.size() - t; ++i) {
            if (arr[i] == arr[i + t]) {
                return arr[i];
            }
        }
        return 0;
    }
};
