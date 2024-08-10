/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func evaluateTree(root *TreeNode) bool {
    if root == nil {
        return false
    }
    
    // If it's a leaf node, return its boolean value
    if root.Left == nil && root.Right == nil {
        return root.Val == 1
    }
    
    // Recursively evaluate the left and right subtree
    leftVal := evaluateTree(root.Left)
    rightVal := evaluateTree(root.Right)
    
    // Apply the operation based on the current node's value
    if root.Val == 2 {
        return leftVal || rightVal
    } else { // root.Val == 3
        return leftVal && rightVal
    }
}