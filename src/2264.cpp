#include <iostream>

using namespace std;

class Solution {
public:
    string largestGoodInteger(string num) {
        string tris[10] = {"999", "888", "777", "666", "555", "444", "333", "222", "111", "000"};
        for(int i = 0; i < 10; ++i) {
            if(num.find(tris[i]) != string::npos) {
                return tris[i];
            }
        }
        return "";
    }
};