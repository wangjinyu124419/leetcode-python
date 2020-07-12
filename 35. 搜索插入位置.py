"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""
from typing import List


#循环
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if target > nums[i]:
#                 continue
#             else:
#                 return i
#         return len(nums)
#二分
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while end>=start:
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle+1
            else:
                end = middle - 1
        if nums[end]>target:
            return end  if end >0 else 0
        else:
            return end+1



if __name__ == '__main__':
    s = Solution()
    res = s.searchInsert([1,3,5,6],2)
    print(res)

