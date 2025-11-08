#!/usr/bin/env python3
"""
Simple Brainfuck Interpreter
Executes Brainfuck programs
"""

import sys


def brainfuck(code):
    """Execute a Brainfuck program"""
    # Remove comments (non-Brainfuck characters)
    code = ''.join(filter(lambda x: x in '><+-.,[]', code))

    # Initialize tape and pointers
    tape = [0] * 30000
    pointer = 0
    code_pointer = 0
    output = []

    # Build jump table for brackets
    bracket_map = {}
    bracket_stack = []
    for i, cmd in enumerate(code):
        if cmd == '[':
            bracket_stack.append(i)
        elif cmd == ']':
            if not bracket_stack:
                raise ValueError(f"Unmatched ] at position {i}")
            start = bracket_stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start

    if bracket_stack:
        raise ValueError(f"Unmatched [ at position {bracket_stack[-1]}")

    # Execute the code
    while code_pointer < len(code):
        cmd = code[code_pointer]

        if cmd == '>':
            pointer += 1
            if pointer >= len(tape):
                tape.extend([0] * 1000)
        elif cmd == '<':
            pointer -= 1
            if pointer < 0:
                raise ValueError("Pointer moved before start of tape")
        elif cmd == '+':
            tape[pointer] = (tape[pointer] + 1) % 256
        elif cmd == '-':
            tape[pointer] = (tape[pointer] - 1) % 256
        elif cmd == '.':
            output.append(chr(tape[pointer]))
        elif cmd == ',':
            char = sys.stdin.read(1)
            tape[pointer] = ord(char) if char else 0
        elif cmd == '[':
            if tape[pointer] == 0:
                code_pointer = bracket_map[code_pointer]
        elif cmd == ']':
            if tape[pointer] != 0:
                code_pointer = bracket_map[code_pointer]

        code_pointer += 1

    return ''.join(output)


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python brainfuck_interpreter.py <file.bf>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            code = f.read()

        output = brainfuck(code)
        print(output, end='')

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
