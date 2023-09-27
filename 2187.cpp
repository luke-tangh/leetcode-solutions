#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
        auto over = [&](long long x) {
            long long sum = 0;
            for(int n : time) {
                sum += x / n;
                if(sum >= totalTrips) return true;
            }
            return sum >= totalTrips;
        };
        long long low = 1;
        long long high = (long long)totalTrips * *min_element(time.begin(), time.end());
        while(low < high) {
            long long mid = low + (high - low) / 2;
            if(over(mid)) {
                high = mid;
            }else {
                low = mid + 1;
            }
        }
        return low;
    }
};
