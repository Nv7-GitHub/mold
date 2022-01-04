from tokens import *
from instructions import ref
from out import *

def print_instruction():
  par = get_next_param()
  ref.ref(par)
  if ref.typ == "float":
    addCode("printf(\"%f\\n\", " + ref.code + ");\n")
  if ref.typ == "string":
    addCode("printf(\"%s\\n\", " + ref.code + ");\n")
