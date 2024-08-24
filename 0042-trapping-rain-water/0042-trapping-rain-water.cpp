class Solution {
public:
    int trap(vector<int>& height) {
        int totalVolume = 0;
        int l = 0;
        int r;

        while (l < height.size() - 1) {
            int prevHeightL = (l > 0) ? height[l - 1] : 0;
            int nextHeightL = (l < height.size() - 1) ? height[l+1] : 0;
    
            if (nextHeightL >= height[l]) {
                ++l;
                continue;
            }

            int highestBlockIdx = -1;
            int highestBlockHeight = 0;
            for (int i = l + 1; i < height.size(); ++i) {
                if (height[i] > highestBlockHeight) {
                    highestBlockHeight = height[i];
                    highestBlockIdx = i;
                }
                if (height[i] >= height[l]) {
                    break;
                }
            }
            if (highestBlockIdx == -1) return totalVolume;
            r = highestBlockIdx;

            int ptr = l + 1;
            int blocksInbetween = 0;
            while (ptr < r) {
                blocksInbetween += height[ptr];
                ++ptr;
            }
            int volumeTrapped = min(height[l], height[r]) * (r - l - 1) - blocksInbetween;
            totalVolume += volumeTrapped;
            l = r;
        }
        return totalVolume;
    }
};