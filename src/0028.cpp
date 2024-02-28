#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int head = 0, tail = 0;
        while(tail < haystack.size() - needle.size() + 1) {
            if(head-tail == needle.size()) {
                return tail;
            }
            if(haystack[head] == needle[head-tail]) {
                head++;
            }
            else {
                head = ++tail;
            }
        }
        return head-tail == needle.size() ? tail : -1;
    }
};
