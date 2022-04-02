class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key = lambda x:x[1])
        leftmost = points[0][1]
        res=1
        for point in points:
            if point[0] > leftmost:
                res += 1
                leftmost = point[1]
        return res