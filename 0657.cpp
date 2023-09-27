#include <iostream>

using namespace std;

class Solution {
public:
    bool judgeCircle(string moves) {
        int vert = 0, hori = 0;
        for(char ins : moves) {
            if(ins == 'U') {
                vert++;
            }else if(ins == 'D') {
                vert--;
            }else if(ins == 'L') {
                hori++;
            }else {
                hori--;
            }
        }
        return vert == 0 && hori == 0;
    }
};
