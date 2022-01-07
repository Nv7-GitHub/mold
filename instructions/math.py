from tokens import *
from out import *
from instructions import ref
from instructions.variables import vartyps
import data

def math_instruction(op):
  var = get_next_param()
  value = get_next_param()
  ref.ref(value)
  if not var in vartyps:
    data.error = "Unknown variable: " + var
    return
  if vartyps[var] != ref.typ:
    data.error = "Wrong type for variable: " + var
    return
  addCode(var + " " + op + "= " + ref.code + ";\n")


  