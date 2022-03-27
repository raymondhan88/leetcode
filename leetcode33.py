from typing import List
class Solution:
    @classmethod
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left + right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[0]:
                if nums[mid]<target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[mid]>target and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
        return left if nums[left] == target else -1

print(Solution.search([3,4,5,6,1,2],1))