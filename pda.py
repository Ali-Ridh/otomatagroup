def run_pda(input_string):
    stack = []
    i = 0

    while i < len(input_string) and input_string[i] == 'a':
        stack.append('A')
        i += 1

    if len(stack) == 0:
        return False

    while i < len(input_string) and input_string[i] == 'b':
        if len(stack) == 0:
            return False
        stack.pop()
        i += 1

    if i != len(input_string):
        return False

    return len(stack) == 0


print("PDA Simulator")
print()

while True:
    user_input = input("Enter string: ").strip()
    if run_pda(user_input):
        print("Result: ACCEPTED\n")
    else:
        print("Result: REJECTED\n")