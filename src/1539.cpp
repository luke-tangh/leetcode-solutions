#include <vector>

using namespace std;

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int last = 0;
        for(int n : arr) {
            if(n - last > 1) {
                k -= n - last - 1;
                last = n;
                if(k <= 0) { last--; break; }
            }else {
                last = n;
            }
        }
        return last + k;
    }
};
