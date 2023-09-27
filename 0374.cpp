/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int front = 1, end = n;
        while(true) {
            int mid = (end - front) / 2 + front;
            int opt = guess(mid);
            if(opt == 0) {
                return mid;
            }else if(opt == 1) {
                front = mid + 1;
            }else {
                end = mid - 1;
            }
        }
    }

    // delete guess api
    int guess(int n) {
        return 0;
    }
};