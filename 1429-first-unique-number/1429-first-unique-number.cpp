static const bool Init() {
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}
class FirstUnique {
public:
    FirstUnique(vector<int> nums) : nums(std::move(nums)) {
        for (int i = 0; i < this->nums.size(); ++i) {
            if (firstOccurences.contains(this->nums[i])) {
                this->nums[firstOccurences[this->nums[i]]] = -1;
                this->nums[i] = -1;
            } else {
                firstOccurences[this->nums[i]] = i;
            } 
        }
        while (firstUniqueIdx < this->nums.size() && this->nums[firstUniqueIdx] < 0) {
            ++firstUniqueIdx;
        }     
    }
    
    const int showFirstUnique() {
        return firstUniqueIdx < this->nums.size() ? this->nums[firstUniqueIdx] : -1;
    }
    
    void add(int value) {
        if (firstOccurences.contains(value)) {
            this->nums[firstOccurences[value]] = -1;
            this->nums.push_back(-1);
        } else {
            firstOccurences[value] = this->nums.size();
            this->nums.push_back(value);
        }
        while (firstUniqueIdx < this->nums.size() && this->nums[firstUniqueIdx] < 0)
            ++firstUniqueIdx;
    }

private:
    unordered_map<int, int> firstOccurences;
    int firstUniqueIdx = 0;
    vector<int> nums;
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */