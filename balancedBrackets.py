def isBalanced():
    n = int(input())
    for i in range(0, n):
        s = input()
        stack = []
        brackets = {'{': '}', '(': ')', '[': ']'}
        for char in s:
            if char in ['{', '(', '[']:  # keywords of dictionary
                stack.append(char)
            else:
                if stack:   # brackets in
                    top = stack.pop()
                    if brackets[top] != char:
                        return "NO"
                else:   # empty stack
                    return "NO"
        return "NO" if stack else "YES"

isBalanced()
