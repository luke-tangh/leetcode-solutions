#include <set>

using namespace std;

class SmallestInfiniteSet {
public:
    set<int> S;
    int cap;

    SmallestInfiniteSet() {
       cap = 1;
    }
    
    int popSmallest() {
        int val = 0;
        if(S.empty()) {
            val = cap++;
        }else {
            val = *S.begin();
            S.erase(val);
        }
        return val;
    }
    
    void addBack(int num) {
        if(num < cap) {
            S.insert(num);
        }
    }
};
