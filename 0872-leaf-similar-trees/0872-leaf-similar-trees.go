/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
    lvs := []int{}

    var getLeafValSeq func(*TreeNode)
    getLeafValSeq = func(root *TreeNode) {
        if root == nil {
            return
        } else if root.Left == nil && root.Right == nil {
            lvs = append(lvs, root.Val)
            return
        }

        getLeafValSeq(root.Left)
        getLeafValSeq(root.Right)
    }

    getLeafValSeq(root1)
    lvs = append(lvs, -1)
    getLeafValSeq(root2)

    i, j := 0, 0

    for lvs[j] != -1 { j++ }
    j++
    if len(lvs) - j != j - 1 { return false }

    for lvs[i] != -1 && j < len(lvs) {
        if lvs[i] != lvs[j] {
            return false
        }
        i++
        j++
    }
    return true
}