import heapq
class Solution:
    def sort_nearly_sorted_array(self, arr, k):
        heap=[]
        result=[]
        for i in range(min(k+1, len(arr))):
            heapq.heappush(heap, arr[i])
        for i in range(k+1, len(arr)):
            result.append(heapq.heappop(heap))
            heapq.heappush(heap, arr[i])
        while heap:
            result.append(heapq.heappop(heap))
        return result

if __name__=="__main__":
    sol=Solution()
    arr=[6, 5, 3, 2, 8, 10, 9]
    k=3
    sorted_arr=sol.sort_nearly_sorted_array(arr, k)
    print(*sorted_arr)