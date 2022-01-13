from tokens import *
from out import *
from instructions import ref
import data

vartyps = {}
varctyps = {}

def set_instruction():
  name = get_next_param()
  value = get_next_param()
  ref.ref(value)  
  if not name in vartyps:
    vartyps[name] = ref.typ
    varctyps[name] = ref.ctyp
    addVar(ref.ctyp + " " + data.namespace + name + ";\n")
  if ref.code != "":
    addCode(data.namespace + name + " = " + ref.code + ";\n")
  