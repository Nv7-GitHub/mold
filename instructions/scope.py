import data
from out import *
import out

def end_instruction():
  if data.scopetype == "proc":
    addFn()
  if data.scopetype == "if" or data.scopetype == "while":
    out.indent -= 1
    addCode("}\n")
  
  data.scopetype = ""