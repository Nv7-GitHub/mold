from tokens import *
from out import *
from instructions import ref
from instructions.variables import vartyps
import data

def concat_instruction():
  var = get_next_param()
  value = get_next_param()
  ref.ref(value)
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "wrong type for variable: " + var
    return
  if ref.typ != "string":
    data.error = "wrong type for concat: " + ref.typ
    return
  
  addCode("mold_strcat(&" + var + ", " + ref.code + ");\n")

def length_instruction():
  var = get_next_param()
  value = get_next_param()
  ref.ref(value)
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "float":
    data.error = "wrong type for variable: " + var
    return
  if ref.typ != "string":
    data.error = "wrong type for length: " + ref.typ
    return
  
  addCode(var + " = (float)strlen(" + ref.code + ");\n")

# Float to string
def ftoa_instruction():
  var = get_next_param()
  value = get_next_param()
  ref.ref(value)
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "wrong type for variable: " + var
    return
  if ref.typ != "float":
    data.error = "wrong type for itoa: " + ref.typ
    return
  
  addCode(var + " = mold_ftoa(" + ref.code + ");\n")

# Float to int to string
def itoa_instruction():
  var = get_next_param()
  value = get_next_param()
  ref.ref(value)
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "wrong type for variable: " + var
    return
  if ref.typ != "float":
    data.error = "wrong type for itoa: " + ref.typ
    return
  
  addCode(var + " = mold_itoa(" + ref.code + ");\n")

# String to float
def atof_instruction():
  var = get_next_param()
  value = get_next_param()
  ref.ref(value)
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "float":
    data.error = "wrong type for variable: " + var
    return
  if ref.typ != "string":
    data.error = "wrong type for itoa: " + ref.typ
    return
  
  addCode(var + " = (float)atof(" + ref.code + ");\n")

# Command line args
def arg_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "wrong type for variable: " + var
    return

  ind = get_next_param()
  ref.ref(ind)
  if ref.typ != "float":
    data.error = "wrong index type for arg: " + ref.typ
    return

  addCode(var + " = mold_arg(" + ref.code + ");\n")
