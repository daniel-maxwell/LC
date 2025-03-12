class Solution {
public:
    int distMoney(int money, int children) {
        if (money < children) return -1;

        money -= children;

        vector<int> childBalances (children, 1);

        int result = 0;
        int i = 0;

        while (i < childBalances.size()) {
            if (money < 7) {
                if (childBalances[i] + money == 4) { 
                    if (i == childBalances.size() - 1) {
                        --result;
                    }
                } else {
                    childBalances[i] += money;
                    money == 0;
                }
                return result;
            } else {
                childBalances[i] += 7;
                ++result;
                money -= 7;
            }
            ++i;
        }

        if (money > 0) --result;
        return result;
    }
};