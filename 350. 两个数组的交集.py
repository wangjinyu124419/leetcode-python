"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        target_list = []
        hash_dict={}
        if len(nums1) < len(nums2):
            min_list= nums1
            larget_list = nums2
        else:
            min_list= nums2
            larget_list = nums1
        for value in min_list:
            if hash_dict.get(value):
                hash_dict[value]+=1
            else:
                hash_dict[value]=1

        for value in larget_list:
            if hash_dict.get(value):
                target_list.append(value)
                hash_dict[value]-=1
                if hash_dict[value]==0:
                    hash_dict.pop(value)
        return target_list