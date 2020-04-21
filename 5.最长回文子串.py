"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        start = 0
        end = 0
        max_sub_len=0
        length = len(s)
        dp =  [[0 for _ in range(length)] for _ in range(length)]

        for j in range(1,length):
            for i in range(0,j):
                if s[i]==s[j]:
                    if j-i<=2:
                        dp[i][j]=1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 0

                if dp[i][j]:
                    if j-i+1 > max_sub_len:
                        start = i
                        end = j
                        max_sub_len = j-i+1
        if end > start:
            print(s[start:end+1])
        return s[start:end+1]

if __name__ == '__main__':
    s=Solution()
    s.longestPalindrome('caac')





