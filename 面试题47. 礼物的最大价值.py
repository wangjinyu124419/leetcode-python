"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，
并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        heigth = len(grid)
        max_value =0
        max_value_array = [ [0 for _ in range(width+1)] for _ in range(heigth+1)]
        print(max_value_array)
        for i in range(0,heigth):
            for j in range(0,width):
                max_value_array[i+1][j+1] = max(max_value_array[i][j+1],max_value_array[i+1][j]) + grid[i][j]
                if max_value_array[i+1][j+1]>max_value:
                    max_value = max_value_array[i+1][j+1]
        return max_value
if __name__ == '__main__':
    s = Solution()
    res=s.maxValue([[1,2,5],[3,2,1]])
    print(s)


