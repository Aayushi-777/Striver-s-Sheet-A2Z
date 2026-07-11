class Solution:
    def insert(self, intervals, new_interval):
        result=[]
        i=0
        n=len(intervals)
        while i<n and intervals[i][1]<new_interval[0]:
            result.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=new_interval[1]:
            new_interval[0]=min(new_interval[0], intervals[i][0])
            new_interval[1]=max(new_interval[1], intervals[i][1])
            i+=1
        result.append(new_interval)
        while i<n:
            result.append(intervals[i])
            i+=1
        return result

if __name__=="__main__":
    sol=Solution()
    intervals=[[1, 2], [3, 5], [6, 7], [8,10]]
    new_interval=[4, 8]
    result=sol.insert(intervals, new_interval)
    print(f"The new intervals after inserting is: {result}")