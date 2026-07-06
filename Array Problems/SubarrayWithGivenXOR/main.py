class Solution:
    def subarray_with_xor(self, arr, k):
        freq={0:1}
        prefixXor=0
        count=0
        for num in arr:
            prefixXor^=num
            target=prefixXor^k
            if target in freq:
                count+=freq[target]
            freq[prefixXor]=freq.get(prefixXor, 0)+1
        return count
    
if __name__=="__main__":
    sol=Solution()
    arr=[4, 2, 2, 6, 4]
    k=6
    count=sol.subarray_with_xor(arr, k)
    print(f"The number of subarrays with the XOR k is: {count}")