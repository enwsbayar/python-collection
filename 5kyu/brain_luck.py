# Inspired from real-world Brainf**k, we want to create an interpreter of that language which will support the following instructions:

# > increment the data pointer (to point to the next cell to the right).
# < decrement the data pointer (to point to the next cell to the left).
# + increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
# - decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
# . output the byte at the data pointer.
# , accept one byte of input, storing its value in the byte at the data pointer.
# [ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
# ] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
# The function will take in input...

# the program code, a string with the sequence of machine instructions,
# the program input, a string, possibly empty, that will be interpreted as an array of bytes using each character's ASCII code and will be consumed by the , instruction
# ... and will return ...

# the output of the interpreted code (always as a string), produced by the . instruction.
# Implementation-specific details for this Kata:

# Your memory tape should be large enough - the original implementation had 30,000 cells but a few thousand should suffice for this Kata
# Each cell should hold an unsigned byte with wrapping behavior (i.e. 255 + 1 = 0, 0 - 1 = 255), initialized to 0
# The memory pointer should initially point to a cell in the tape with a sufficient number (e.g. a few thousand or more) of cells to its right. For convenience, you may want to have it point to the leftmost cell initially
# You may assume that the , command will never be invoked when the input stream is exhausted
# Error-handling, e.g. unmatched square brackets and/or memory pointer going past the leftmost cell is not required in this Kata. If you see test cases that require you to perform error-handling then please open an Issue in the Discourse for this Kata (don't forget to state which programming language you are attempting this Kata in).

def brain_luck(code, program_input):
  bracket_map = {}
  stack = []
  for i, c in enumerate(code):
    if c == '[':
      stack.append(i)
    elif c == ']':
      j = stack.pop()
      bracket_map[i] = j
      bracket_map[j] = i

  tape = [0] * 30000
  dp = 0
  pc = 0
  inp = 0
  out = []

  while pc < len(code):
    cmd = code[pc]
    if cmd == '>':
      dp += 1
    elif cmd == '<':
      dp -= 1
    elif cmd == '+':
      tape[dp] = (tape[dp] + 1) & 0xFF
    elif cmd == '-':
      tape[dp] = (tape[dp] - 1) & 0xFF
    elif cmd == '.':
      out.append(chr(tape[dp]))
    elif cmd == ',':
      tape[dp] = ord(program_input[inp])
      inp += 1
    elif cmd == '[':
      if tape[dp] == 0:
        pc = bracket_map[pc]
    elif cmd == ']':
      if tape[dp] != 0:
        pc = bracket_map[pc]
    pc += 1

  return ''.join(out)