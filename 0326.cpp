class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n <= 0){
            return false;
        }
        if(n == 1){
            return true;
        }
        long long ans = 1;
        while(true){
            ans *= 3;
            if(ans == n){
                return true;
            }else if (ans > n){
                return false;
            }
        }
        return false;
    }
};