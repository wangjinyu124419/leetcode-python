"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        ans=abs(nums[0]+nums[1]+nums[2] -target)
        min_value = nums[0]+nums[1]+nums[2]
        for i in range(length-1):
            start=i+1
            end = length-1
            while start<end:
                sum = nums[i] + nums[start]+nums[end]
                if abs(sum-target)< ans:
                    ans = abs(sum-target)
                    min_value = sum


                if sum<target:
                    start+=1
                elif sum>target:
                    end-=1
                elif sum==target:
                    return sum
        return min_value
if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([1,1,1,0],-100)



