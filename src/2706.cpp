#include <vector>

using namespace std;

class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int fst = 101, snd = 101;
        for (int p : prices) {
            if (p < snd) {
                if (p < fst) {
                    snd = fst;
                    fst = p;
                }
                else {
                    snd = p;
                }
            }
        }
        int ret = money - fst - snd;
        return ret >= 0 ? ret : money;
    }
};
