class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up,down,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        res=[]
        while up<=down and left<=right:
            for i in range(left,right+1):
                res.append(matrix[up][i])
            for i in range(up+1,down+1):
                res.append(matrix[i][right])
            if up<down and left<right:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[down][i])
                for i in range(down-1,up,-1):
                    res.append(matrix[i][left])
            left+=1
            right-=1
            up+=1
            down-=1
        return res