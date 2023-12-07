class Solution {
public:
    int totalMoney(int n) {
        int weeks = n / 7;
        int last = n % 7;
        return (49 + weeks * 7) * weeks / 2 + (2 * weeks + last + 1) * last / 2;
    }
};
