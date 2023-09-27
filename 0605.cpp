#include <vector>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int max_f = 0, streak = 1;
        for(int f : flowerbed) {
            if(f == 1) {
                if (streak != 0) max_f += (streak - 1) / 2;
                streak = 0;
            }else {
                streak++;
            }
        }
        if (streak != 0) max_f += streak / 2;
        return max_f >= n;
    }
};
