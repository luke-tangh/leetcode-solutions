#include <iostream>

using namespace std;

class Solution {
public:
    string convertToTitle(int columnNumber) {
        string col;
        char c;
        while(columnNumber) {
            int cnum = columnNumber % 26;
            if(cnum == 0) {
                c = 'Z';
                col = c + col;
                columnNumber--;
            }else {
                c = 'A' + cnum - 1;
                col = c + col;
            }
            if(columnNumber == 26) {
                break;
            }
            columnNumber /= 26;
        }
        return col;
    }
};