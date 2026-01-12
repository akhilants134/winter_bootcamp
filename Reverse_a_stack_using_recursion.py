class Solution:
    def reverseStack(self,stack):
        def insertAtBottom(stack,x):
            if not stack:
                stack.append(x)
                return
            top=stack.pop()
            insertAtBottom(stack,x)
            stack.append(top)
        if not stack:
            return
        top=stack.pop()
        self.reverseStack(stack)
        insertAtBottom(stack,top)
        return stack
stack=list(map(int,input().split()))
sol=Solution()
print(sol.reverseStack(stack))
