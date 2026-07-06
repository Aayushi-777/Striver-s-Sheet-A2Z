class Solution:
    def letter_combinations(self, digits):
        if not digits:
            return []
        mapping={'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res=[]
        def backtrack(index, path):
            if index==len(digits):
                res.append(path)
                return
            for ch in mapping[digits[index]]:
                backtrack(index+1, path+ch)
        backtrack(0, "")
        return res

if __name__=="__main__":
    sol=Solution()
    digits="23"
    res=sol.letter_combinations(digits)
    print(*res)