class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> minHeight (height.size());
        int maxHeightL = 0;
        for (int i = 0; i < height.size(); ++i) {
            maxHeightL = max(maxHeightL, height[i]);
            minHeight[i] = maxHeightL;
        }
        int maxHeightR = 0;
        for (int i = height.size()-1; i >= 0; --i) {
            maxHeightR = max(maxHeightR, height[i]);
            minHeight[i] = min(minHeight[i], maxHeightR);
        }

        int totalWaterVolume = 0;
        for (int i = 0; i < minHeight.size(); ++i) {
            const int vol = minHeight[i] - height[i] > 0 ? minHeight[i] - height[i] : 0;
            totalWaterVolume += vol;
        }
        return totalWaterVolume;
    }
};