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
  addCode(data.namespace + var + " " + op + "= " + ref.code + ";\n")

def rand_instruction(is_int):
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "float":
    data.error = "wrong type for variable: " + var
    return
  
  low = get_next_param()
  ref.ref(low)
  if ref.typ != "float":
    data.error = "wrong type for math: " + ref.typ
    return
  lowcode = ref.code  

  high = get_next_param()
  ref.ref(high)
  if ref.typ != "float":
    data.error = "wrong type for math: " + ref.typ
    return
  highcode = ref.code
  
  fn = "lib_mold_random"
  if is_int:
    fn = "lib_mold_randint"
  addCode(data.namespace + var + " = " + fn + "(" + lowcode + ", " + highcode + ");\n")
  
  