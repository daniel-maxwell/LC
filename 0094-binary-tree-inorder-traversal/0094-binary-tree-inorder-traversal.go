/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    result := []int{}
    var dfs func(node *TreeNode)
    dfs = func (root *TreeNode) {
        if root == nil {
            return
        }
        dfs(root.Left)
        result = append(result, root.Val)
        dfs(root.Right)
    }
    dfs(root)
    return result
}