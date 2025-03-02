class Solution {
public:
    int shipWithinDays(vector<int> &weights, int days) {
        int l = 1, r = 500 * weights.size();
        int result = r;

        while (l <= r) {
            
            int mid = l + ((r - l) / 2);
            bool canShip = true;
            int capacity = mid;
            int daysLeft = days;

            for (const int &weight : weights) {
                if (weight > mid) {
                    canShip = false;
                    break;
                }
                if (weight > capacity) {
                    if (daysLeft == 1) {
                        canShip = false;
                        break;
                    }
                    --daysLeft;
                    capacity = mid;
                }
                capacity -= weight;
            }

            if (canShip && capacity < 0) {
                if (daysLeft == 1 || weights.back() > mid) {
                    canShip = false;
                }
            }
            if (canShip) {
                result = min(result, mid);
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return result;
    }
};