#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        char last = ' ';
        int head = 0;
        int count = 1;
        for(int i = 0; i < chars.size(); ++i) {
            if(chars[i] == last) {
                count++;
                continue;
            }
            if(count > 1) {
                int start = head;
                while(count) {
                    chars[head] = count % 10 + '0';
                    head++;
                    count /= 10;
                }
                reverse(chars.begin()+start, chars.begin()+head);
                count = 1;
            }
            last = chars[i];
            chars[head] = chars[i];
            head++;
        }
        if(count > 1) {
            int start = head;
            while(count) {
                chars[head] = count % 10 + '0';
                head++;
                count /= 10;
            }
            reverse(chars.begin()+start, chars.begin()+head);
        }
        chars.resize(head);
        return head;
    }
};
