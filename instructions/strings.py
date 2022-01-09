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
  
  addCode("mold_strcat(" + var + ", " + ref.code + ");\n")

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
  
  addCode(var + " = (float)(" + ref.code + "->len);\n")

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
  
  addCode(var + " = (float)atof(mold_cstring(" + ref.code + "));\n")

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

# String index
def ind_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "wrong type for variable: " + var
    return

  val = get_next_param()
  ref.ref(val)
  if ref.typ != "string":
    data.error = "wrong type for index: " + ref.typ
    return
  valcode = ref.code

  ind = get_next_param()
  ref.ref(ind)
  if ref.typ != "float":
    data.error = "wrong index type for ind: " + ref.typ
    return

  addCode(var + " = mold_strind(" + valcode + ", " + ref.code + ");\n")

# Numeric
def numeric_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "bool":
    data.error = "wrong type for variable: " + var
    return
  str = get_next_param()
  ref.ref(str)
  if ref.typ != "string":
    data.error = "wrong type for numeric: " + ref.typ
    return
  addCode(var + " = mold_isnumeric(" + ref.code + ");\n")

