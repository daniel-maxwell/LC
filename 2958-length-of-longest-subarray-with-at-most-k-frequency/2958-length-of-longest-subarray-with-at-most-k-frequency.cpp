auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
const size_t BUFFER_SIZE = 0x6fafffff;
alignas(std::max_align_t) char buffer[BUFFER_SIZE];
size_t buffer_pos = 0;
void* operator new(size_t size) {
    constexpr std::size_t alignment = alignof(std::max_align_t); // Default maximum alignment
    size_t padding = (alignment - (buffer_pos % alignment)) % alignment;
    size_t total_size = size + padding;
    char* aligned_ptr = &buffer[buffer_pos + padding];
    buffer_pos += total_size;
    return aligned_ptr;
}
void operator delete(void* ptr) {}
void operator delete[](void* ptr) {}

class Solution {
public:
    const int maxSubarrayLength(const vector<int>& nums, const int k) {
        int l = 0, r = 0;
        int result = 0;
        int currMaxFreq = 1;
        unordered_map<int, int> freqs;
        while (r < nums.size()) {
            ++freqs[nums[r]];
            currMaxFreq = max(currMaxFreq, freqs[nums[r]]);
            while (freqs[nums[r]] > k) {
                --freqs[nums[l]];
                ++l;
            }
            result = max(result, r - l + 1);
            ++r;
        }
        return result;
    }
};