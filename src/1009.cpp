class Solution {
public:
    int bitwiseComplement(int n) {
        if(n == 0){
            return 1;
        }
        int k = 0;
        while(1){
            if((1<<k) > n){
                break;
            }
            ++k;
        }
        return (1<<k)-1-n;
    }
};