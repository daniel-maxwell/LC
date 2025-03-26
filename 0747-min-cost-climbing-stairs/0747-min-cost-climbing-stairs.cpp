class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int a = cost[0];
        int b = cost[1];

        for (int i = 2; i < cost.size(); ++i) {
            const int temp = min(a, b) + cost[i];
            a = b;
            b = temp;
        }

        return min(a, b);
    }
};