from out import *
import data
from tokens import *
from instructions import ref
from instructions.proc import fns

switch_count = 0
switch_val_code = ""
default = "NULL"
def switch_instruction():
  global switch_count, switch_val_code

  if data.scopetype != "":
    data.error = "cannot use nested scopes"
    return
  
  v = get_next_param()
  ref.ref(v)
  if ref.typ != "string":
    data.error = "cannot switch on non-string"
    return
  addCode("mold_switch* mold_switchval_" + str(switch_count) + " = NULL;\n")
  switch_count += 1
  data.scopetype = "switch"
  switch_val_code = ref.code

def case_instruction():
  if data.scopetype != "switch":
    data.error = "cannot use case outside of switch"
    return

  global switch_count
  val = get_next_param()
  ref.ref(val)
  if ref.typ != "string":
    data.error = "cannot switch on non-string"
    return
  
  fn = get_next_param()
  if not fn in fns:
    data.error = "unknown function: " + fn
    return

  addCode("mold_switch_add(" + ref.code + ", " + fn + ", &mold_switchval_" + str(switch_count - 1) + ");\n")

def default_instruction():
  if data.scopetype != "switch":
    data.error = "cannot use default outside of switch"
    return

  global default
  fn = get_next_param()
  if not fn in fns:
    data.error = "unknown function: " + fn
    return
  default = fn
