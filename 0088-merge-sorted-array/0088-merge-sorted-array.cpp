auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    const void merge(vector<int>& nums1, const int m, const vector<int>& nums2, int n) {
        if (nums1.empty()) { nums1 = nums2; return; }
        if (nums2.empty()) return;
        int i = nums1.size() - 1;
        int n1Idx = nums1.size() - nums2.size() - 1;
        int n2Idx = nums2.size() - 1;
        while (i >= 0) {
            if (n1Idx == -1) {
                nums1[i] = nums2[n2Idx];
                --n2Idx;
            } else if (n2Idx == -1) {
                nums1[i] = nums1[n1Idx];
                --n1Idx;
            } else if (nums1[n1Idx] >= nums2[n2Idx]) {
                nums1[i] = nums1[n1Idx];
                --n1Idx;
            } else {
                nums1[i] = nums2[n2Idx];
                --n2Idx;
            }
            --i;
        }
        return;
    }
};