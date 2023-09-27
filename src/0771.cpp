#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        set<string> col;
        int cnt = 0;
        for(int i = 0; i < jewels.size(); ++i) {
            col.insert(jewels.substr(i,1));
        }
        for(int i = 0; i < stones.size(); ++i) {
            if(col.count(stones.substr(i,1))) {
                ++cnt;
            }
        }
        return cnt;
    }
};