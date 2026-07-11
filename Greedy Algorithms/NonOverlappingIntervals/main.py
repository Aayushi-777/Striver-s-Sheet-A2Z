class Solution:
    def remove_overlapping(self, intervals):
        intervals.sort(key=lambda x:x[1])
        count=0
        prev_end=intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0]<prev_end:
                count+=1
            else:
                prev_end=intervals[i][1]
        return count
    
if __name__=="__main__":
    sol=Solution()
    intervals=[[1, 3], [2, 4], [3, 5], [1, 2]]
    count=sol.remove_overlapping(intervals)
    print(f"The number of intervals to be removed to get non-overlapping intervals are: {count}")