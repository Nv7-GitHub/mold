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
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "float":
    data.error = "wrong type for variable: " + var
    return
  if ref.typ != "float":
    data.error = "wrong type for math: " + ref.typ
    return
  addCode(var + " " + op + "= " + ref.code + ";\n")


  