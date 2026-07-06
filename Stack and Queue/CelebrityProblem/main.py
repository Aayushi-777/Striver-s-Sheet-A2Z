class Solution:
    def celebrity(self, matrix):
        n=len(matrix)
        stack=[]
        for i in range(n):
            stack.append(i)
        while len(stack)>1:
            a=stack.pop()
            b=stack.pop()
            if matrix[a][b]==1:
                stack.append(b)
            else:
                stack.append(a)
        candidate=stack.pop()
        for i in range(n):
            if i!=candidate:
                if matrix[candidate][i]==1 or matrix[i][candidate]==0:
                    return -1
        return candidate

if __name__=="__main__":
    sol=Solution()
    matrix=[
        [0,1,1,0],
        [0,0,0,0],
        [1,1,0,0],
        [0,1,1,0]
    ]
    cel=sol.celebrity(matrix)
    print(f"The celebrity is: Person {cel}")