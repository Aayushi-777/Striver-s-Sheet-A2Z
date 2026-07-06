class Solution:
    def largest_rectangle_area(self, heights):
        n=len(heights)
        left_small=[0]*n
        right_small=[0]*n
        stack=[]
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
    def maximal_rectangle(self, matrix):
        if not matrix: return 0
        m=len(matrix[0])
        heights=[0]*m
        max_area=0
        for row in matrix:
            for i in range(m):
                if row[i]=='1':
                    heights[i]+=1
                else:
                    heights[i]=0
            max_area=max(max_area, self.largest_rectangle_area(heights))
        return max_area

if __name__=="__main__":
    sol=Solution()
    matrix=[
        ['1','0','1','0','0'],
        ['1','0','1','1','1'],
        ['1','1','1','1','1'],
        ['1','0','0','1','0']
    ]
    print(sol.maximal_rectangle(matrix))



