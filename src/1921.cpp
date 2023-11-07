#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        for(int i = 0; i < dist.size(); ++i) {
            if(dist[i] % speed[i] == 0) {
                dist[i] = (dist[i] / speed[i]) - 1;
            }
            else {
                dist[i] = dist[i] / speed[i];
            }
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
