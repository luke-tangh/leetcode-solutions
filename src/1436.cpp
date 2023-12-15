#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        set<string> S, D;
        vector<string> A;
        for (vector<string> das : paths) {
            S.insert(das[0]);
            D.insert(das[1]);
        }
        set_difference(
            D.begin(), D.end(), S.begin(), S.end(), 
            std::back_inserter(A)
        );
        return *A.begin();
    }
};
