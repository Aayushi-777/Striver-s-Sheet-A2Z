class Solution:
    def insert(self, stack, temp):
        if not stack or stack[-1]>=temp:
            stack.append(temp)
            return
        val=stack.pop()
        self.insert(stack, temp)
        stack.append(val)
    def sort_stack(self, stack):
        if stack:
            temp=stack.pop()
            self.sort_stack(stack)
            self.insert(stack, temp)

if __name__=="__main__":
    sol=Solution()
    stack=[4, 1, 3, 2]
    sol.sort_stack(stack)
    print(f"Sorted stack (descending order): {stack}")
