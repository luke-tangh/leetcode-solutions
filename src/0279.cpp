#include <algorithm>
#include <cmath>

class Solution {  
public:  
    int is_square(int n) {  
        int sqrt_n = (int)(sqrt(n));  
        return (sqrt_n*sqrt_n == n);  
    }
    
    int numSquares(int n) {  
        if(is_square(n)) {
            return 1;  
        }
        while(n % 4 == 0) {
            n >>= 2;  
        }
        if(n % 8 == 7) {
            return 4;
        }
        int sqrt_n = sqrt(n); 
        for(int i = 1; i <= sqrt_n; i++) {  
            if (is_square(n - i*i)) {
                return 2;  
            }
        } 
        return 3;  
    }  
};
