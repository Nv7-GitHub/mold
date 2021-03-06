from tokens import *
from instructions import ref
from out import *
import data
from instructions.variables import vartyps

def print_instruction():
  par = get_next_param()
  ref.ref(par)
  if ref.typ == "float" or ref.typ == "string":
    addCode("std::cout << " + ref.code + " << std::endl;\n")
  elif ref.typ == "bool":
    addCode("std::cout << (" + ref.code + " ? \"true\" : \"false\") << std::endl;\n")
  else:
    data.error = "print: cannot print composite value"

def read_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "cannot read into non-string variable: " + var
    return

  filename = get_next_param()
  ref.ref(filename)

  if ref.typ != "string":
    data.error = "read: filename must be a string"
    return

  addCode(data.namespace + var + " = lib_mold_read(" + ref.code + ");\n")

def write_instruction():
  file = get_next_param()
  ref.ref(file)
  if ref.typ != "string":
    data.error = "write: filename must be a string"
    return
  filename = ref.code

  val = get_next_param()
  ref.ref(val)
  if ref.typ != "string":
    data.error = "write: value must be a string"
    return
  value = ref.code

  addCode("lib_mold_write(" + filename + ", " + value + ");\n")

def cmd_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "cannot read output into non-string variable: " + var
    return

  val = get_next_param()
  ref.ref(val)
  if ref.typ != "string":
    data.error = "cmd: command must be a string"
    return

  addCode(data.namespace + var + " = lib_mold_system(" + ref.code + ");\n")

def rm_instruction():
  file = get_next_param()
  ref.ref(file)
  if ref.typ != "string":
    data.error = "rm: file must be a string"
    return

  addCode("lib_mold_remove(" + ref.code + ");\n")

def exit_instruction():
  code = get_next_param()
  ref.ref(code)
  if ref.typ != "float":
    data.error = "exit: code must be a number"
    return
  addCode("exit((int)" + ref.code + ");\n")
