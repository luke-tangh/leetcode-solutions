#include <set>

using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        set<int> seen;
        bool loop = false;
        while(not loop) {
            n = digitSum(n);
            if(n == 1) {
                return true;
            }
            if(seen.count(n)) {
                loop = true;
            }else {
                seen.insert(n);
            }
        }
        return false;
    }

    int digitSum(int n) {
        int digsum = 0;
        while(n) {
            int place;
            place = n % 10;
            n = n / 10;
            digsum += place * place;
        }
        return digsum;
    }
};