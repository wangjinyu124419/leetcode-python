"""
你将获得 k 个鸡蛋，并可以使用一栋从 1 到 n  共有 n 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= n 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= n）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    kn_map = {}
    def superEggDrop(self, k: int, n: int) -> int:
        if k <= 1:
            return n
        if n <= 1:
            return 1
        # if (k,n) in self.kn_map:
        #     return self.kn_map[(k,n)]
        temp_list = []
        for i in range(1,n+1):
            temp_value = (max(self.superEggDrop(k-1,i-1),self.superEggDrop(k,n-i))) +1
            temp_list.append(temp_value)
        min_value = min(temp_list)
        # self.kn_map[(k,n)] = mim_value
        return min_value
        # return self.kn_map[(k,n)]
if __name__ == '__main__':
    s=Solution()
    res = s.superEggDrop(3,14)
    print(res)





