from tokens import get_next_param
from instructions import ref
import data
from out import *
from instructions.variables import vartyps

def comp_instruction(op):
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
    addCode(var + " = " + code1 + " " + op + " " + code2 + ";\n")
  if typ1 == "string":
    addCode(var + " = strcmp(" + code1 + ", " + code2 + ") " + op + " 0;\n")
  if typ1 == "dict":
    data.error = "cannot compare dictionaries"

def not_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "bool":
    data.error = "wrong type for variable: " + var
    return

  addCode(var + " = !(" + var + ");\n")

def logical_instruction(op):
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var1
    return
  if vartyps[var] != "bool":
    data.error = "wrong type for variable: " + var1
    return

  val = get_next_param()
  ref.ref(val)
  if ref.typ != "bool":
    data.error = "value must be of type bool"
    return

  addCode(var + " = " + var + " " + op + " (" + ref.code + ");\n")

