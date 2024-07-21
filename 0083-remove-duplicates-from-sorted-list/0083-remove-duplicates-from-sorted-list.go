/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	curr := head
	var prev *ListNode
	for curr != nil {
		prev = curr
		curr = curr.Next
		for curr != nil && prev.Val == curr.Val {
			prev.Next = curr.Next
			curr.Next = nil
			curr = prev.Next
		}
	}
	return head
}