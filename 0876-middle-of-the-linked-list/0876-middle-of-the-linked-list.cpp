/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fastPtr = head->next;
        ListNode* slowPtr = head;
        while (fastPtr != nullptr) {
            fastPtr = fastPtr->next;
            slowPtr = slowPtr->next;
            if (fastPtr == nullptr) {
                break;
            }
            fastPtr = fastPtr->next;
        }
        return slowPtr;
    }
};