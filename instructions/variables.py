from tokens import *
from out import *
from instructions import ref

vartyps = {}
varctyps = {}

def set_instruction():
  name = get_next_param()
  value = get_next_param()
  ref.ref(value)  
  if not name in vartyps:
    vartyps[name] = ref.typ
    varctyps[name] = ref.ctyp
    addVar(ref.ctyp + " " + name + " = " + ref.code + ";\n")
  else:
    addCode(name + " = " + ref.code + ";\n")
  