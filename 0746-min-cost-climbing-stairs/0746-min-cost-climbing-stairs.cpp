class Solution {
public:
    const int minCostClimbingStairs(const vector<int>& cost) {
        int a = cost[0], b = cost[1];
        for (int i = 2; i < cost.size(); ++i) {
            int temp = cost[i] + min(a, b);
            a = b;
            b = temp;
        }
        return min(a,b);
    }
};