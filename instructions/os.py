from tokens import *
from instructions import ref
from out import *

def print_instruction():
  par = get_next_param()
  ref.ref(par)
  if ref.typ == "float":
    addCode("printf(\"%f\\n\", " + ref.code + ");\n")
  if ref.typ == "string":
    addCode("printf(\"%s\\n\", mold_cstring(" + ref.code + "));\n")
  if ref.typ == "bool":
    addCode("puts(" + ref.code + " ? \"true\" : \"false\");\n")
