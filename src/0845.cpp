#include <vector>

using namespace std;

class Solution {
public:
    int longestMountain(vector<int>& arr) {
        if(arr.size() < 3) {
            return 0;
        }
        int max_mount = 0;
        for(int i = 0; i < arr.size(); ++i) {
            max_mount = max(max_mount, mountain(arr, i));
        }
        return max_mount;
    }

    int mountain(vector<int>& arr, int idx) {
        int mount = 1, maxidx = arr.size();
        int l = idx, r = idx;
        while(true) {
            if(l-1 < 0 || arr[l-1] >= arr[l]) {
                break;
            }
            if(r+1 >= maxidx || arr[r+1] >= arr[r]) {
                break;
            }
            mount += 2;
            l--; r++;
        }
        if(mount < 3) {
            return 0;
        }
        while(l > 0 && arr[l-1] < arr[l]) {
            mount++;
            l--;
        }
        while(r+1 < maxidx && arr[r+1] < arr[r]) {
            mount++;
            r++;
        }
        return mount;
    }
};
