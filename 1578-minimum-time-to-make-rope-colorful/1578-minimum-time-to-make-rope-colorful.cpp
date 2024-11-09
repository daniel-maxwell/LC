auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const int minCost(const string colors, const vector<int>& neededTime) {
        int i = 0, result = 0;
        while (i < colors.size() - 1) {
            int maxTime = 0, totalTime = 0;
            bool group = false;
            while (i < colors.size() && colors[i] == colors[i+1]) {
                totalTime += neededTime[i];
                maxTime = maxTime < neededTime[i] ? neededTime[i] : maxTime;
                ++i;
                group = true;
            }
            if (group) {
                totalTime += neededTime[i];
                maxTime = maxTime < neededTime[i] ? neededTime[i] : maxTime;
                result += totalTime - maxTime;
            }
            ++i;
        }
        return result;
    }
};