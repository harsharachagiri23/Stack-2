class Solution: 
    def isValid(self, s: str) -> bool:
        map = {
              ")" : "(",
            "}" :  "{",
            "]" : "["
        }
        stack = []

        for val in s:
            if val in "({[":
                stack.append(val)
            elif val in map:
                if not stack or stack[-1] != map[val]:
                    return False 
                stack.pop()
            else:
                return False
        return not stack


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([])"))