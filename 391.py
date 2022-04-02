from collections import defaultdict
from typing import List

class Solution:
    @classmethod
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area,maxx,maxy,minx,miny = 0, rectangles[0][2], rectangles[0][3], rectangles[0][0], rectangles[0][1]
        dic =  defaultdict(int)
        for rectangle in rectangles:
            area += (rectangle[2]-rectangle[0]) * (rectangle[3]-rectangle[1])
            maxx = max(maxx, rectangle[2])
            maxy = max(maxy, rectangle[3])
            minx = min(minx, rectangle[0])
            miny = min(miny, rectangle[1])

            dic[(rectangle[0],rectangle[2])] +=1
            dic[(rectangle[0],rectangle[3])] +=1
            dic[(rectangle[1],rectangle[2])] +=1
            dic[(rectangle[1],rectangle[3])] +=1

        if area !=  (maxx-minx) * (maxy - miny) or dic[(maxx,maxy)]!=1 or dic[(maxx,miny)]!=1 or dic[(minx,maxy)]!=1 or dic[(minx,miny)]!=1 :
            return False
        del dic[(maxx,maxy)], dic[(maxx,miny)], dic[(minx,maxy)], dic[(minx,miny)]

        return all(c==2 or c==4 for c in dic.values())

print(Solution.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))