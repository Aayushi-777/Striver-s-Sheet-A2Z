from collections import deque
class Solution:
    def word_ladder_length(self, start_word, target_word, word_list):
        q=deque([(start_word, 1)])
        st=set(word_list)
        if start_word in st:
            st.remove(start_word)
        while q:
            word, steps=q.popleft()
            if word==target_word:
                return steps
            for i in range(len(word)):
                original=word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word in st:
                        st.remove(new_word)
                        q.append((new_word, steps+1))
        return 0
if __name__=="__main__":
    sol=Solution()
    word_list=["des", "der", "dfr", "dgt", "dfs"]
    start_word="der"
    target_word="dfs"
    ans=sol.word_ladder_length(start_word, target_word, word_list)
    print(ans)