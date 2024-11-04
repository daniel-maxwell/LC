/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const int guessNumber(int n) {
        int l = 1, r = n;
        while (l <= r) {
            int m = l + floor((r - l) / 2);
            const int g = guess(m);
            if (g == -1) r = --m;
            else if (g == 1) l = ++m;
            else return m;
        };
        return 0;
    };
};