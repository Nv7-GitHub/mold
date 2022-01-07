from lib import *
import tokens
top = read("top.c")
code = ""

fn = ""
currFn = "main"
currFnRetType = "int"
variables = ""
mainFn = ""

def addVar(code):
  global variables
  variables += code

def addFn():
  global code, currFn, currFnRetType, mainFn, fn
  code += currFnRetType + " " + currFn + "() {\n" + fn + "}\n"
  currFnRetType = "int"
  currFn = "main"
  fn = mainFn

def newFn(name):
  global currFnRetType, currFn, fn, mainFn
  currFnRetType = "void"
  currFn = name
  mainFn = fn
  fn = ""

def addCode(code):
  global fn
  fn += "\t#line " + str(tokens.line+1) + " \"" + tokens.file + "\"\n"
  fn += "\t" + code

def save():
  global top
  addFn()
  top += variables
  top += "\n"
  top += code
  with open("out.c", "w") as f:
    f.write(top)