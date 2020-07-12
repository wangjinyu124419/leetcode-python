from typing import List


class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur_index = 0
        for num in nums2:
            for index in range(cur_index,len(nums1)):
                if num <= nums1[index]:

                    if index == 0:
                        nums1.insert(0,num)
                    else:
                        nums1.insert(index-1,nums1)
                        cur_index = index
            nums1.append(num)
        print(nums1)
if __name__ == '__main__':
    s = Solution()
    s.merge([1,2,3],[4,5,6])



