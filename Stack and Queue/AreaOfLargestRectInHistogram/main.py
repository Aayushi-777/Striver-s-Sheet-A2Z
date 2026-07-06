class Solution:
    def largest_rectangle_area(self, heights):
        n=len(heights)
        stack=[]
        left_small=[0]*n
        right_small=[0]*n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            left_small[i]=0 if not stack else stack[-1]+1
            stack.append(i)
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            right_small[i]=n-1 if not stack else stack[-1]-1
            stack.append(i)
        max_area=0
        for i in range(n):
            width=right_small[i]-left_small[i]+1
            max_area=max(max_area, heights[i]*width)
        return max_area

if __name__=="__main__":
    sol=Solution()
    heights=[2, 1, 5, 6, 2, 3]
    ans=sol.largest_rectangle_area(heights)
    print(f"The area of largest rectangle in the histogram is: {ans}")