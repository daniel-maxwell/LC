/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) return false;
        ListNode* slow = head;
        ListNode* fast = head->next;
    
        while (fast != nullptr) {
            if (slow == fast) {
                return true;
            }
            fast = fast->next;
            if (fast == nullptr) {
                break;
            }
            fast = fast->next;
            slow = slow->next;
        }
        return false;
    }
};