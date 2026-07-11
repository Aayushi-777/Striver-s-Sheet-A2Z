class Solution:
    def job_scheduling(self, jobs):
        jobs.sort(key=lambda x:x[2], reverse=True)
        max_deadline=max(job[1] for job in jobs)
        slots=[-1]*(max_deadline+1)
        count=0
        tot_profit=0
        for job_id, deadline, profit in jobs:
            for j in range(deadline, 0, -1):
                if slots[j]==-1:
                    slots[j]=job_id
                    count+=1
                    tot_profit+=profit
                    break
        return count, tot_profit

if __name__=="__main__":
    sol=Solution()
    jobs=[[1, 4, 20], [2, 1, 10], [3, 2, 40], [4, 2, 30]]
    count, profit=sol.job_scheduling(jobs)
    print(f"Jobs done: {count}")
    print(f"Total profit: {profit}")