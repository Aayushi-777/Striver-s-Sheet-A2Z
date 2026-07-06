class Solution:
    def insert_at_bottom(self, stack, val):
        if not stack:
            stack.append(val)
            return 
        top_val=stack.pop()
        self.insert_at_bottom(stack, val)
        stack.append(top_val)
    def reverse_stack(self, stack):
        if not stack:
            return
        top_val=stack.pop()
        self.reverse_stack(stack)
        self.insert_at_bottom(stack, top_val)

if __name__=="__main__":
    sol=Solution()
    stack=[4, 1, 3, 2]
    sol.reverse_stack(stack)
    print(f"The reversed stack is: {stack}")