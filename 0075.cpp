#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red = 0, white = 0, blue = 0;
        bool iswhite = false, isblue = false;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] == 0) {
                nums[red++] = 0;
                iswhite ? nums[white++] = 1 : white++;
                isblue ? nums[blue++] = 2 : blue++;
            }else if(nums[i] == 1) {
                nums[white++] = 1;
                isblue ? nums[blue++] = 2 : blue++;
                iswhite = true;
            }else {
                nums[blue++] = 2;
                isblue = true;
            }
        }
    }
};