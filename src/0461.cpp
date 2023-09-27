class Solution {
public:
    int hammingDistance(int x, int y) {
        return countOnes(x ^ y);
    }
    
    int countOnes(int x){
        int cut = 0;
        while(x){
            x &= (x-1);
            ++cut;
        }
        return cut;
    }
};