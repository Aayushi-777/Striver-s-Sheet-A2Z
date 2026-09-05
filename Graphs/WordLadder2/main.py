from collections import deque
class Solution:
    def find_sequence(self, begin_word, target_word, word_list):
        words=set(word_list)
        q=deque([[begin_word]])
        if begin_word in words:
            words.remove(begin_word)
        ans=[]
        level=1
        used=[begin_word]
        while q:
            path=q.popleft()
            if len(path)>level:
                level+=1
                for word in used:
                    words.discard(word)
                used=[]
            word=path[-1]
            if word==target_word:
                if not ans:
                    ans.append(path)
                elif len(path)==len(ans[0]):
                    ans.append(path)
                continue
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word in words:
                        q.append(path+[new_word])
                        used.append(new_word)
        return ans
if __name__=="__main__":
    sol=Solution()
    word_list=["des", "der", "dfr", "dgt", "dfs"]
    begin_word="der"
    target_word="dfs"
    ans=sol.find_sequence(begin_word, target_word, word_list)
    for path in ans:
        print(*path)