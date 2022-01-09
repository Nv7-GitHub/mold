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
  "eq": lambda: comp_instruction("=="),
  "less": lambda: comp_instruction("<"),
  "greater": lambda: comp_instruction(">"),
  "if": if_instruction,
  "else": else_instruction,
  "not": not_instruction,
  "and": lambda: logical_instruction("&&"),
  "or": lambda: logical_instruction("||"),
  "while": while_instruction,
  "length": length_instruction,
  "ftoa": ftoa_instruction,
  "atof": atof_instruction,
  "itoa": itoa_instruction,
  "arg": arg_instruction,
  "ind": ind_instruction,
  "rand": lambda: rand_instruction(False),
  "irand": lambda: rand_instruction(True),
  "include": include_instruction,
  "return": return_instruction,
}

def parse():
  while True:
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
