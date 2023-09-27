#include <vector>

using namespace std;

class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long sum = 0, count = 0;
        for(int n : nums) {
            if(n == 0) {
                count++;
            }else {
                sum += adding(count);
                count = 0;
            }
        }
        sum += adding(count);
        return sum;
    }

    long long adding(long long n) {
        if(n == 0) {
            return 0;
        }else {
            return (n + 1) * n / 2;
        }
    } 
};
