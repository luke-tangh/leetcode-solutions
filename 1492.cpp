class Solution {
public:
    int kthFactor(int n, int k) {
        int sn = sqrt(n + 1e-7);
        int nums[1001], top = 0;
        for(int i = 1; i <= sn; ++i) {
            if(n % i == 0) {
                nums[top++] = i;
                if(n / i != i) {
                    nums[top++] = n / i;
                }
            }
        }
        sort(nums, nums+top);
        if(top < k) {
            return -1;
        }else {
            return nums[k-1];
        }
    }
};