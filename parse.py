import sys
from lib import *
from tokens import *
import tokens
from instructions import *
import data

tokens.file = sys.argv[1]
tokens.code = read(tokens.file)

instructions = {
  "print": print_instruction,
  "set": set_instruction,
  "add": lambda: math_instruction("+"),
  "sub": lambda: math_instruction("-"),
  "mul": lambda: math_instruction("*"),
  "div": lambda: math_instruction("/"),
  "mod": lambda: math_instruction("%"),
}

while pos < len(tokens.code):
  ended = next_instruction()
  if ended:
    break
  if tokens.next_instr in instructions:
    data.error = ""
    instructions[tokens.next_instr]()
    if data.error != "":
      print(data.error)
      exit(1)
  else:
    print("Unknown instruction: " + tokens.next_instr)
    exit(1)

save()
