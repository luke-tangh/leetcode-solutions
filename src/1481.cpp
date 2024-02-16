#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        unordered_map<int, int> countMap;
        for (int n : arr) {
            countMap[n]++;
        }
        vector<int> countArr;
        for (auto kv : countMap) {
            countArr.push_back(kv.second);
        }
        sort(countArr.begin(), countArr.end());
        int removed = 0;
        for (int n : countArr) {
            if (k >= n) {
                k -= n;
                removed++;
            }
        }
        return countArr.size() - removed;
    }
};
