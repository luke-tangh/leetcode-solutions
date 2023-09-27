#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        while(stones.size() > 1) {
            sort(stones.begin(), stones.end());
            int wy = stones.back();
            stones.pop_back();
            int wx = stones.back();
            stones.pop_back();
            if(wy > wx) {
                stones.push_back(wy - wx);
            }
        }
        if(stones.size() == 1) {
            return stones[0];
        }else {
            return 0;
        }
    }
};
