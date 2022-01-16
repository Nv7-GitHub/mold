from out import *
import data
from tokens import *
from instructions import ref
import out

need_break = False
def switch_instruction():
  global need_break
  
  v = get_next_param()
  ref.ref(v)
  if ref.typ != "string":
    data.error = "cannot switch on non-string"
    return
  addCode("switch (lib_mold_fnv_32a(" + ref.code + ")) {\n")
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
  addCode("case lib_mold_fnv_32a_const(\"" + val + "\"):\n")
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
