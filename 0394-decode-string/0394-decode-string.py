class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        stack = []
        curr = ''
        nums = 0
        for i in s:
            if i == '[':
                stack.append(nums)
                stack.append(curr)
                curr = ''
                nums = 0
            elif i == ']':
                st = stack.pop()
                num = stack.pop()
                curr = st + curr * num
            elif i.isdigit():
                nums = nums * 10 + int(i)
            else:
                curr += i
        
        return curr
    
            

                