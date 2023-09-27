#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> fcount;
        int i = 0, j = 0;
        for(j; j < fruits.size(); j++) {
            fcount[fruits[j]]++;
            if(fcount.size() > 2) {
                if(--fcount[fruits[i]] == 0) {
                    fcount.erase(fruits[i]);
                }
                i++;
            }
        }
        return j-i;
    }
};
