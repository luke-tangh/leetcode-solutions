#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        for(int i = 0; i < dist.size(); ++i) {
            dist[i] = (dist[i] - 1) / speed[i];
        }
        sort(dist.begin(), dist.end());
        for(int i = 0; i < dist.size(); ++i) {
            if(dist[i] < i) {
                return i;
            }
        }
        return dist.size();
    }
};
