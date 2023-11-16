#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        vector<int> ints;
        for (string s : nums) {
            ints.push_back(toInt(s));
        }
        sort(ints.begin(), ints.end());
        int i = 0;
        for (int n : ints) {
            if (i == n) { i++; }
            else { break; }
        }
        return toBin(i, nums[0].size());
    }

    int toInt(string bin) {
        int ret = 0;
        int p = bin.size() - 1;
        for (char b : bin) {
            if (b == '1') {
                ret += pow(2, p);
            }
            p--;
        }
        return ret;
    }

    string toBin(int dec, int n) {
        int p = pow(2, n - 1);
        string ret = "";
        for (int i = 0; i < n; ++i) {
            if (dec / p == 0) {
                ret += '0';
            }
            else {
                ret += '1';
                dec -= p;
            }
            p /= 2;
        }
        return ret;
    }
};
