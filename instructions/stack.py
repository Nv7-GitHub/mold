from tokens import *
from out import *
from instructions import ref
from instructions.variables import vartyps
import data

def push_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "stack":
    data.error = "wrong type for variable: " + vartyps[var]
    return

  key = get_next_param()
  ref.ref(key)
  if ref.typ != "string":
    data.error = "wrong type for setkey: " + ref.typ
  
  addCode("mold_stack_push(&" + var + ", " + ref.code + ");\n")

def pop_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "stack":
    data.error = "wrong type for variable: " + var
    return

  addCode("mold_stack_pop(&" + var + ");\n")

def top_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "wrong type for variable: " + var
    return

  stack = get_next_param()
  ref.ref(stack)
  if ref.typ != "stack":
    data.error = "wrong type for top: " + ref.typ
    return

  addCode(var + " = mold_stack_top(&" + ref.code + ");\n")