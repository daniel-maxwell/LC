/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
    var invert func(root *TreeNode)

    invert = func(root *TreeNode) {

        if (root == nil) || 
        ( root.Left == nil && root.Right == nil) {
            return
        }

        temp := root.Left
        root.Left = root.Right
        root.Right = temp
        invert(root.Left)
        invert(root.Right)
    }

    invert(root)
    return root
}