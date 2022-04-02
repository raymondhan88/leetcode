from typing import List
class Solution:
    @classmethod
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sums=[0]
        for num in nums:
            sums.append(sums[-1]+num)
        def generate(sums,left,right):
            if left >= right:
                return 0
            m = (left + right) // 2
            res = generate(sums, left, m) + generate(sums, m + 1, right)
            l, r = m + 1, 0
            for i in range(left,m + 1):
                while l <= right and sums[l] - sums[i] < lower:
                    l += 1
                r = l
                while r <= right and sums[r] - sums[i] <= upper:
                    r += 1
                res += r - l
            temp = []
            i, j = left, m + 1
            while i <= m and j <= right:
                if sums[i] <= sums[j]:
                    temp.append(sums[i])
                    i += 1
                else:
                    temp.append(sums[j])
                    j += 1
            if i <= m:
                temp += sums[i:m + 1]
            else:
                temp += sums[j:right + 1]
            sums[left:right+1]=temp
            """for i in range(right-left+1):
                sums[i+left] = temp[i]"""
            return res


        return generate(sums,0,len(sums)-1)

print(Solution.countRangeSum([0],0, 0))