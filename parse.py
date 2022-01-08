import sys
from lib import *
from tokens import *
import tokens
from instructions import *
import data
from build import *

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
  "concat": concat_instruction,
  "setkey": setkey_instruction,
  "getkey": getkey_instruction,
  "proc": proc_instruction,
  "call": call_instruction,
  "end": end_instruction,
  "#": comment_instruction,
}

while pos < len(tokens.code):
  ended = next_instruction()
  if ended:
    break

  if tokens.next_instr in instructions:
    data.error = ""
    instructions[tokens.next_instr]()
    if data.error != "":
      print(tokens.file + ":" + str(tokens.line) + ": " + data.error, file=sys.stderr)
      exit(1)
  else:
    print(tokens.file + ":" + str(tokens.line) + ": " + "unknown instruction: " + tokens.next_instr, file=sys.stderr)
    exit(1)

build()
