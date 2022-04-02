from typing import List, Counter


class Solution:
    @classmethod
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq= Counter(s1.split()) + Counter(s2.split())
        res=[]
        for word,occ in freq.items():
            if occ==1:
                res.append(word)
        return res

print(Solution.uncommonFromSentences("this apple is sweet", "this apple is sour"))