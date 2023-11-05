#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int wins = 0, cur = 0, idx = 1;
        if(k > arr.size()) {
            return *max_element(arr.begin(), arr.end());
        }
        while(wins < k) {
            if(cur == idx) {
                idx++;
                continue;
            }
            if(idx >= arr.size()) {
                idx = 0;
                continue;
            }
            if(arr[cur] > arr[idx]) {
                idx++;
                wins++;
            }
            else {
                wins = 1;
                cur = idx;
                idx++;
            }
        }
        return arr[cur];
    }
};
