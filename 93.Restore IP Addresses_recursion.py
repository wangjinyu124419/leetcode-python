"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
合法的ip格式(0~255).(0~255).(0~255).(0~255)
"""
#直接用的这里的方法https://blog.csdn.net/fuxuemingzhu/article/details/80657420

"这应该是通用的方法"
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        #如果字符串大于最大长度
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i + 1]
            if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], res)



s=Solution()
print(s.restoreIpAddresses('25525511135'))

