static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k(k) {
        nums_.insert(nums_.end(), nums.begin(), nums.end());
        make_heap(nums_.begin(), nums_.end(), greater<>());
        while (nums_.size() > k) {
            pop_heap(nums_.begin(), nums_.end(), greater<>());
            nums_.pop_back();
        }
    }
    
    int add(int val) {
        nums_.push_back(val);
        push_heap(nums_.begin(), nums_.end(), greater<>());
        if (nums_.size() > k) {
            pop_heap(nums_.begin(), nums_.end(), greater<>());
            nums_.pop_back();
        }
        return nums_.front();
    }
    
private:
    vector<int> nums_;
    int k;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */