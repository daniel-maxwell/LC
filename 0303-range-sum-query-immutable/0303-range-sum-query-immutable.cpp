class NumArray {
public:
    NumArray(const vector<int>& nums) : Nums(nums) {
    }

    const int sumRange(int left, int right) {
        int result = 0;
        for (int i = left; i <= right; ++i) {
            result += Nums[i];
        }
        return result;
    }

private:
    const vector<int>& Nums;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */