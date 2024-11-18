static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* start = list1;
        ListNode* prevStart = nullptr;
        ListNode* end = list1;
        while (b > 0) {
            if (a > 0) {
                prevStart = start;
                start = start->next;
                --a;
            }
            end = end->next;
            --b;
        }
        if (prevStart != nullptr) prevStart->next = list2;
        ListNode* list2Ptr = prevStart->next;
        while (list2Ptr->next != nullptr) list2Ptr = list2Ptr->next;
        list2Ptr->next = end->next;
        list2 = nullptr;
        return list1;
    }
};