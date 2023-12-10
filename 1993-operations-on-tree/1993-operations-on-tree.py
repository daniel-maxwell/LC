class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.lockedNodes = {}

        self.children = {}

        for i in range(0, len(parent)):
            if parent[i] == -1:
                continue
            else:
                if parent[i] in self.children:
                    self.children[parent[i]].append(i)
                else:
                    self.children[parent[i]] = [i]

        print(self.children)
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.lockedNodes:
            return False
        else:
            self.lockedNodes[num] = user
            return True     


    def unlock(self, num: int, user: int) -> bool:
        if num in self.lockedNodes:
            if self.lockedNodes[num] == user:
                self.lockedNodes.pop(num)
                return True
        return False   


    def upgrade(self, num: int, user: int) -> bool:
        if self.checkForLockedAncestors(num, self.parent):
            return False
        if not self.checkForLockedDescendants(num, self.parent):
            return False

        self.lock(num, user)
        q = deque(self.children[num])

        while q:
            curr = q.popleft()
            if curr in self.lockedNodes:
                self.unlock(curr, self.lockedNodes[curr])

            if curr in self.children:
                for el in self.children[curr]:
                    q.append(el)

        return True


    def checkForLockedAncestors(self, num, arr):
        p = num
        while p != -1:
            if p in self.lockedNodes: return True
            p = arr[p]
        return False


    def checkForLockedDescendants(self, num, arr):
        if num not in self.children:
            return False

        lockedDesc = False
        
        q = deque(self.children[num])

        while q:
            curr = q.popleft()
            if curr in self.lockedNodes:
                lockedDesc = True   

            if curr in self.children:
                for el in self.children[curr]:
                    q.append(el)

        return lockedDesc


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)