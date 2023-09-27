class Solution {
public:
    bool isPerfectSquare(int num) {
        int ans = 0;
        for(int i = 0; i <= num; ++i){
            if((long long)i * i <= num){
                ans = i;
            }else {
                break;
            }
        }
        return (long long)ans * ans == num;
    }
};