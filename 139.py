class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic=set(wordDict)
        valid=[False]*(len(s)+1)
        valid[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if valid[j] and s[j:i] in dic:
                    valid[i]=True
                    break
        return valid[-1]