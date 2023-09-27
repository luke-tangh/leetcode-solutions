#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int, int> nums;
        vector<int> arr;
        for(int n : arr1) {
            if(nums.count(n)) {
                nums[n] += 1;
            }else{
                nums[n] = 1;
            }
        }
        for(int n : arr2) {
            for(int i = 0; i < nums[n]; ++i) {
                arr.push_back(n);
            }
            nums.erase(n);
        }
        for(auto [k, v] : nums) {
            for(int i = 0; i < v; ++i) {
                arr.push_back(k);
            }
        }
        return arr;
    }
};
