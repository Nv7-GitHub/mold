import data
from out import *
import out
from instructions import switch

def end_instruction():
  if data.get_scope() == "proc":
    addFn()
    data.infunc = False
  if data.get_scope() == "if" or data.get_scope() == "while":
    out.indent -= 1
    addCode("}\n")
  if data.get_scope() == "switch":
    if switch.need_break:
      addCode("break;\n")
    out.indent -= 1
    addCode("}\n")
  
  data.pop_scope()