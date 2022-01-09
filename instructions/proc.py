import data
import out
from tokens import *
from out import *

fns = {}

def proc_instruction():
  if data.get_scope() != "":
    data.error = "cannot define procedure inside of a scope"
    return

  fn_name = get_next_param()
  newFn(fn_name)
  out.indent = 1
  fns[fn_name] = ""
  data.push_scope("proc")
  data.infunc = True

def return_instruction():
  if not data.infunc:
    data.error = "cannot return outside of procedure!"
    return
  addCode("return;\n")

def call_instruction():
  fn_name = get_next_param()
  if fn_name not in fns:
    data.error = "unknown procedure: " + fn_name
    return
  addCode(fn_name + "();\n")
