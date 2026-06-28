def run_tm(input_string):
    tape = ['_'] + list(input_string) + ['_']
    head = 1
    state = 'q0'
    step = 0

    while step < 1000:
        step += 1
        symbol = tape[head]

        if state == 'q0':
            if symbol == 'a':
                tape[head] = 'X'
                head += 1
                state = 'q1'
            elif symbol == 'Y':
                head += 1
                state = 'q3'
            else:
                return False

        elif state == 'q1':
            if symbol in ('a', 'Y'):
                head += 1
            elif symbol == 'b':
                tape[head] = 'Y'
                head -= 1
                state = 'q2'
            else:
                return False

        elif state == 'q2':
            if symbol in ('a', 'Y'):
                head -= 1
            elif symbol == 'X':
                head += 1
                state = 'q0'
            else:
                return False

        elif state == 'q3':
            if symbol == 'Y':
                head += 1
            elif symbol == '_':
                return True
            else:
                return False

        if head < 0:
            return False
        if head >= len(tape):
            tape.append('_')

    return False


print("Turing Machine Simulator - Language: a^n b^n")
print()

while True:
    user_input = input("Enter string: ").strip()
    if run_tm(user_input):
        print("Result: ACCEPTED\n")
    else:
        print("Result: REJECTED\n")