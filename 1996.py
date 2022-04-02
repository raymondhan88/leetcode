class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        maxdef = properties[0][1]
        res = 0
        for p in properties:
            if p[1]<maxdef:
                res+=1
            else:
                maxdef = p[1]
        return res
