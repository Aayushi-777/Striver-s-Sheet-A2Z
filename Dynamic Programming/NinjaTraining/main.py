class Solution:
    def solve(self, day, last, points, dp):
        if dp[day][last]!=-1:
            return dp[day][last]
        if day==0:
            ans=0
            for task in range(3):
                if task!=last:
                    ans=max(ans, points[0][task])
            dp[day][last]=ans
            return ans
        ans=0
        for task in range(3):
            if task!=last:
                score=points[day][task]+self.solve(day-1, task, points, dp)
                ans=max(ans, score)
        dp[day][last]=ans
        return ans
    def ninja_training(self, n, points):
        dp=[[-1]*4 for i in range(n)]
        return self.solve(n-1, 3, points, dp)
    
if __name__=="__main__":
    sol=Solution()
    points=[
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
    ]   
    n=len(points)
    ans=sol.ninja_training(n, points)
    print(f"The maximum points earned by ninja is: {ans}")