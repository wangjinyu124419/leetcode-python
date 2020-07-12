class Solution:
    stack = []
    def isValid(self, s: str) -> bool:
        for item in s:
            if not self.stack:
                self.stack.append(item)

            elif item == ')':
                if self.stack[-1]=='(':
                    self.stack.pop()
                else:
                    self.stack.append(item)
                    # return False
            elif item == ']':
                if self.stack[-1]=='[':
                    self.stack.pop()
                else:
                    self.stack.append(item)
                    # return False
            elif item == '}':
                if self.stack[-1]=='{':
                    self.stack.pop()
                else:
                    self.stack.append(item)
                    # return False
            else:
                self.stack.append(item)
        if self.stack:
            return False
        else:
            return True
if __name__ == '__main__':
    s=Solution()
    res=s.isValid("{[]}")
    print(res)



