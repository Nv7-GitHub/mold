from out import *
import data
from tokens import *
from instructions import ref
from instructions.proc import fns
import out

FNV_32_PRIME = 16777619
FNV1_32_INIT = -2128831035

def fnv_32a(val):
  hval = FNV1_32_INIT
  for char in val:
    hval ^= ord(char)
    hval *= FNV_32_PRIME
    hval %= 2**32 # Done in C by hitting maximum cap of int32
  return hval

need_break = False
def switch_instruction():
  global switch_val_code, need_break
  
  v = get_next_param()
  ref.ref(v)
  if ref.typ != "string":
    data.error = "cannot switch on non-string"
    return
  addCode("switch (mold_fnv_32a_str(mold_cstring(" + ref.code + "))) {\n")
  out.indent += 1
  data.push_scope("switch")
  need_break = False

def case_instruction():
  if data.get_scope() != "switch":
    data.error = "cannot use case outside of switch"
    return

  global need_break
  val = get_next_param()
  if need_break:
    addCode("break;\n")

  out.indent -= 1
  hashed = str(fnv_32a(val))
  addCode("case " + hashed + ":\n")
  out.indent += 1
  need_break = True


def default_instruction():
  if data.get_scope() != "switch":
    data.error = "cannot use default outside of switch"
    return

  global need_break
  if need_break:
    addCode("break;\n")
  out.indent -= 1
  addCode("default:\n")
  out.indent += 1
