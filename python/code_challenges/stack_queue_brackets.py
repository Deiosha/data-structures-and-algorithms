from data_structures.queue import Queue


def multi_bracket_validation(input_string):
    # creating an empty list of stack
    stack = []
    # for the character in the value in input_strings
    for char in input_string:
        # if any of the strings are these brackets
        if char in ['(', '{', '[']:
            # append adds chara. to stack
            stack.append(char)
        #     unless the character of these brackets is not return False
        elif char in [')', '}', ']']:
            if not stack:
                return False
            # checking for bracket notation
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack
