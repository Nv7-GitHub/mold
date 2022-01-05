import sys
from lib import *
from tokens import *
import tokens
from instructions import *

tokens.file = sys.argv[1]
tokens.code = read(tokens.file)

instructions = {
  "print": print_instruction,
  "set": set_instruction,
}

while pos < len(tokens.code):
  ended = next_instruction()
  if ended:
    break
  if tokens.next_instr in instructions:
    instructions[tokens.next_instr]()
  else:
    print("Unknown instruction: " + tokens.next_instr)
    exit(1)

save()
