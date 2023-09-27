#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        int upper = *max_element(candies.begin(), candies.end());
        for(int c : candies) {
            if (c + extraCandies >= upper) {
                result.push_back(true);
            }else {
                result.push_back(false);
            }
        }
        return result;
    }
};
