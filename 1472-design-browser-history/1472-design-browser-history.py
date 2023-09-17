class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.curr = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        self.history.append(self.curr)
        self.curr.next = ListNode(url)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.history:
            self.curr = self.history.pop()
            steps -= 1

        return self.curr.val  

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.history.append(self.curr)
            self.curr = self.curr.next
            steps -= 1
        
        return self.curr.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)