class Solution:
    def sortStack(self, stack):
        if not stack:
            return
        top = stack.pop()
        self.sortStack(stack)
        self.insertInSortedOrder(stack, top)
        return stack
    def insertInSortedOrder(self, stack, element):
        if not stack or stack[-1] < element:
            stack.append(element)
            return
        top = stack.pop()
        self.insertInSortedOrder(stack, element)
        stack.append(top)
stack=list(map(int,input().split()))
sol=Solution()
print(sol.sortStack(stack))
