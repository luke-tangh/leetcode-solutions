#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int maxl = 0, space = 0;
        for(int i = 0; i < sentences.size(); ++i) {
            space = count(sentences[i].begin(), sentences[i].end(), ' ') + 1;
            if(space > maxl) {
                maxl = space;
            }
        }
        return maxl;
    }
};