from tokens import *
from out import *
from instructions import ref
from instructions.variables import vartyps
import data

def concat_instruction():
  var = get_next_param()
  value = get_next_param()
  ref.ref(value)
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "wrong type for variable: " + var
    return
  if ref.typ != "string":
    data.error = "wrong type for concat: " + ref.typ
    return
  
  addCode("mold_strcat(&" + var + ", " + ref.code + ");\n")