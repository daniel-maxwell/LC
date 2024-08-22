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
    ListNode *swapNodes(ListNode *head, int k) {
    int nodeIdx = 1;
    int length = 0;

    ListNode *ptrA = head;

    while (nodeIdx < k) {
      ptrA = ptrA->next;
      ++nodeIdx;
      ++length;
    }

    ListNode *ptrB = ptrA;

    while (ptrB != nullptr) {
      ptrB = ptrB->next;
      ++length;
    }

    ptrB = head;
    nodeIdx = 1;

    while (nodeIdx <= length - k) {
      ptrB = ptrB->next;
      ++nodeIdx;
    }

    int temp = ptrA->val;
    ptrA->val = ptrB->val;
    ptrB->val = temp;

    return head;
  }
};