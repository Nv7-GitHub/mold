from tokens import get_next_param
from instructions import ref
import data
from out import *
from instructions.variables import vartyps
import out

done_else = False
def if_instruction():
  global done_else

  cond = get_next_param()
  ref.ref(cond)
  if ref.typ != "bool":
    data.error = "condition must be of type bool"
    return
  addCode("if (" + ref.code + ") {\n")
  out.indent += 1
  data.scopetype = "if"
  done_else = False

def else_instruction():
  global done_else
  if data.scopetype != "if":
    data.error = "else must be inside if"
    return

  if done_else:
    data.error = "multiple else statements"
    return
  
  out.indent -= 1
  addCode("} else {\n")
  out.indent += 1

def while_instruction():
  cond = get_next_param()
  ref.ref(cond)
  if ref.typ != "bool":
    data.error = "condition must be of type bool"
    return
  addCode("while (" + ref.code + ") {\n")
  out.indent += 1
  data.scopetype = "while"
  
