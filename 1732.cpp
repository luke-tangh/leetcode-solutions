#include <vector>

using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int high = 0, alt = 0;
        for(int n : gain) {
            alt += n;
            high = max(high, alt);
        }
        return high;
    }
};
