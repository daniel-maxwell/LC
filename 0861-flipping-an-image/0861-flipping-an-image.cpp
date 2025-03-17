class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        for (int i = 0; i < image.size(); ++i) {
            int j = 0;
            int k = image[0].size() - 1;
            while (j < k) {
                const int temp = image[i][j];
                image[i][j] = image[i][k];
                image[i][k] = temp;
                ++j;
                --k;
            }
            for (int j = 0; j < image[0].size(); ++j) {
                if (image[i][j] == 0) {
                    image[i][j] = 1;
                } else {
                    image[i][j] = 0;
                }
            }
        }
        return image;
    }
};