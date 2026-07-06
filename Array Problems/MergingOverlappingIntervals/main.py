class Solution:
    def merging_intervals(self, intervals):
        intervals.sort()
        merged=[]
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1], interval[1])
        return merged

if __name__=="__main__":
    sol=Solution()
    intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]
    merged=sol.merging_intervals(intervals)
    print(f"The merged intervals is: {merged}")