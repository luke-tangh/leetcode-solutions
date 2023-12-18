#include <vector>

using namespace std;

class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        int maxA = 0, maxB = 0, minA = 10000, minB = 10000;
        for (int n : nums) {
            if (n > maxB) {
                if (n > maxA) {
                    maxB = maxA;
                    maxA = n;
                }
                else {
                    maxB = n;
                }
            }
            if (n < minB) {
                if (n < minA) {
                    minB = minA;
                    minA = n;
                }
                else {
                    minB = n;
                }
            }
        }
        return maxA * maxB - minA * minB;
    }
};
