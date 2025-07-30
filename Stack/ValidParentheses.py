def ValidParentheses(s: str) -> bool:
    bracketMap = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char in bracketMap:
            top_element = stack.pop() if stack else '#'
            if bracketMap[char] != top_element:
                return False
        else:
            stack.append(char)


    return not stack

s = "()[]{}"
result = ValidParentheses(s)
print(result)