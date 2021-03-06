from tokens import *
from out import *
from instructions import ref
from instructions.variables import vartyps
import data
import sys

def setkey_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "dict":
    data.error = "wrong type for variable: " + var
    return

  key = get_next_param()
  ref.ref(key)
  if ref.typ != "string":
    data.error = "wrong type for setkey: " + ref.typ
  keycode = ref.code

  value = get_next_param()
  ref.ref(value)
  if ref.typ != "string":
    data.error = "wrong type for setkey: " + ref.typ
  valuecode = ref.code

  addCode(data.namespace + var + "[" + keycode + "] = " + valuecode + ";\n")

def getkey_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "string":
    data.error = "wrong type for variable: " + var
    return

  table = get_next_param()
  if not table in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[table] != "dict":
    data.error = "wrong type for variable: " + var
    return

  key = get_next_param()
  ref.ref(key)
  if ref.typ != "string":
    data.error = "wrong type for getkey: " + ref.typ
  
  addCode(data.namespace + var + " = " + data.namespace + table + "[" + ref.code + "];\n")

def haskey_instruction():
  var = get_next_param()
  if not var in vartyps:
    data.error = "unknown variable: " + var
    return
  if vartyps[var] != "bool":
    data.error = "wrong type for variable: " + var
    return

  val = get_next_param()
  ref.ref(val)
  if ref.typ != "dict":
    data.error = "wrong type for haskey: " + ref.typ
  valcode = ref.code

  key = get_next_param()
  ref.ref(key)
  if ref.typ != "string":
    data.error = "wrong type for haskey: " + ref.typ
  keycode = ref.code

  addCode(data.namespace + var + " = " + valcode + ".find(" + keycode + ")" + " != " + valcode + ".end();\n")
