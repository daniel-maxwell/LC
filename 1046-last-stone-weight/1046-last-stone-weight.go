type IntHeap []int

// Len is the number of elements in the collection.
func (h IntHeap) Len() int { return len(h) }

// Less reports whether the element with index i should sort before the element with index j.
func (h IntHeap) Less(i, j int) bool { return h[j] < h[i] } // Max-heap

// Swap swaps the elements with indexes i and j.
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

// Push pushes the element x onto the heap.
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

// Pop removes and returns the minimum element (according to Less) from the heap.
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func lastStoneWeight(stones []int) int {
    maxHeap := &IntHeap{}

    for _, val := range stones {
        heap.Push(maxHeap, val)
    }

    for maxHeap.Len() > 0 {
        stone1 := heap.Pop(maxHeap).(int)
        
        if maxHeap.Len() == 0 {
            return stone1
        }
        
        stone2 := heap.Pop(maxHeap).(int)
        
        remainingStone := stone1 - stone2
        if remainingStone > 0 {
            heap.Push(maxHeap, remainingStone)
        }
    }
    return 0
}