#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        string gs = "MPG";
        int ret = 0;
        for (char c : gs) {
            int time = 0, reach = 0;
            for (int i = 0; i < garbage.size(); ++i) {
                int cs = count(garbage[i].begin(), garbage[i].end(), c);
                if (cs > 0) {
                    time += cs;
                    reach = i;
                }
            }
            time += accumulate(travel.begin(), travel.begin() + reach, 0);
            ret += time;
        }
        return ret;
    }
};
