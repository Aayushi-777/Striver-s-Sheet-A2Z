class Solution:
    def pascal_triangle(self, N):
        row=[]
        val=1
        row.append(val)
        for k in range(1, N):
            val=val*(N-k)//k
            row.append(val)
        return row
if __name__=="__main__":
    sol=Solution()
    N=5
    nth_row=sol.pascal_triangle(N)
    print(*nth_row)
    