#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> V;
        sort(potions.begin(), potions.end());
        for(int s : spells) {
            long long thres = (success + s - 1) / s;
            auto iter = lower_bound(potions.begin(), potions.end(), thres);
            V.push_back(potions.end() - iter);
        }
        return V;
    }
};
