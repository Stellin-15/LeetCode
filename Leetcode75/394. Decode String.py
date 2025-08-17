class Solution(object):
    def decodeString(self, s):
        stack = []      # will hold pairs: (prev_string, repeat_count)                        
        current = []    # list of characters for current segment
        k = 0           # current repeat count being parsed

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)  # build multi-digit number
            elif char == "[":
                stack.append(("".join(current),k))  # push current context, reset for new bracketed segment
                current = []
                k = 0
            elif char == "]":
                prev, repeat = stack.pop()  # pop context and expand
                current = [prev + ''.join(current)* repeat]
            else:
                current.append(char)
        
        return ''.join(current)

            
