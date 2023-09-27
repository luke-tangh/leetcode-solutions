#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int boats = people.size();
        if(boats == 1) {
            return 1;
        }
        int l = 0, r = boats - 1;
        while(r > 0 && people[r] > limit) {
            r--;
        }
        while(r > l) {
            if(people[l] + people[r] <= limit) {
                boats--;
                l++;
                r--;
            }else {
                r--;
            }
        }
        return boats;
    }
};