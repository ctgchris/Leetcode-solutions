class Solution:
    def isValid(self, s: str) -> bool:
        #set of correct c, if present 
        hash_map = {")": "(", "]": "[", "}": "{"}

        stack=[]
        for c in s:
            if c not in hash_map:
                stack.append(c)
            else:
                if not stack or stack[-1] != hash_map[c]:
                    return False
                stack.pop()
        return not stack
        