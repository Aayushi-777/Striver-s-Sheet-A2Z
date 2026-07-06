class Solution:
    def kth_element(self, A, B, k):
        if len(A)>len(B):
            return self.kth_element(B, A,k)
        m, n=len(A), len(B)
        low=max(0, k-n)
        high=min(k, m)
        while low<=high:
            cut1=(low+high)//2
            cut2=k-cut1
            l1=float('inf') if cut1==0 else A[cut1-1]
            l2=float('-inf') if cut2==0 else B[cut2-1]
            r1=float('inf') if cut1==m else A[cut1]
            r2=float('inf') if cut2==n else B[cut2]
            if l1<=r2 and l2<=r1:
                return max(l1, l2)
            elif l1>r2:
                high=cut1-1
            else:
                low=cut1+1

if __name__=="__main__":
    sol=Solution()
    A=[2, 3, 6, 7, 9]
    B=[1, 4, 8, 10]
    k=5
    ans=sol.kth_element(A, B, k)
    print(f"The kth element in both the arrays is: {ans}")