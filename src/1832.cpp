#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    bool checkIfPangram(string sentence) {
        set<char> chars;
        for(char c : sentence) {
            chars.insert(c);
        }
        return chars.size() == 26 ? true : false;
    }
};