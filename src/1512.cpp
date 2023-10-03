#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> M;
        int pairs = 0;
        for(int n : nums) {
            pairs += M[n]++;
        }
        return pairs;
    }
};
