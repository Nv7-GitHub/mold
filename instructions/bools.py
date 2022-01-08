from tokens import get_next_param
from instructions import ref
import data
from out import *
from instructions.variables import vartyps
import out

def eq_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "bool":
    data.error = "wrong type for variable: " + var
    return

  val1 = get_next_param()
  ref.ref(val1)
  typ1 = ref.typ
  code1 = ref.code

  val2 = get_next_param()
  ref.ref(val2)
  typ2 = ref.typ
  code2 = ref.code

  if typ1 != typ2:
    data.error = "values must be of same type"
    return

  if typ1 == "float" or typ1 == "bool":
    addCode(var + " = " + code1 + " == " + code2 + ";\n")
  if typ1 == "string":
    addCode(var + " = mold_streq(" + code1 + ", " + code2 + ");\n")
  if typ1 == "dict":
    data.error = "cannot compare dictionaries"

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
  
