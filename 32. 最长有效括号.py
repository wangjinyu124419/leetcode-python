"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for sub in s:
            if not stack:
                stack.insert(0,sub)
            else:
                if sub==')' and stack[0]=='(':
                    stack.pop(0)
                else:
                    stack.insert(0,sub)
        return len(s)-len(stack)

if __name__ == '__main__':
    s = Solution()
    res = s.longestValidParentheses("(()")
    print(res)

