import data
from tokens import *
from out import *

fns = {}

def proc_instruction():
  if data.scopetype != "":
    data.error = "cannot nest scopes!"
    return
  
  fn_name = get_next_param()
  newFn(fn_name)
  fns[fn_name] = ""
  data.scopetype = "proc"

def call_instruction():
  fn_name = get_next_param()
  if fn_name not in fns:
    data.error = "unknown procedure: " + fn_name
    return
  addCode(fn_name + "();\n")
