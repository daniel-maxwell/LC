type MyQueue struct {
    q []int
}


func Constructor() MyQueue {
    return MyQueue{}
}


func (this *MyQueue) Push(x int)  {
    this.q = append(this.q, x)
    return
}


func (this *MyQueue) Pop() int {
    val := this.q[0]
    this.q = this.q[1:]
    return val
}


func (this *MyQueue) Peek() int {
    return this.q[0]
}


func (this *MyQueue) Empty() bool {
    if len(this.q) == 0 {
        return true
    } else {
        return false
    }
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */