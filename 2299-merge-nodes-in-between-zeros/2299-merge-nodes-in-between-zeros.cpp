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
    ListNode* mergeNodes(ListNode* head) {

        ListNode* cur = head;
        ListNode* endNode = getNextZeroNode(cur->next);

        while (endNode != nullptr) {
            while (cur->next != endNode) {
                cur->val += cur->next->val;
                cur->next = cur->next->next;
            }
            cur->val += cur->next->val;
            cur->next = cur->next->next;
            cur = cur->next;
            endNode = getNextZeroNode(cur);
        }

        return head;
    }

    ListNode* getNextZeroNode(ListNode* cur) {
        while (cur != nullptr && cur->val != 0) {
            cur = cur->next;
        }
        return cur;
    }
};