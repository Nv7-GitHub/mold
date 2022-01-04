from lib import *
import tokens
top = read("top.c")
fn = ""
currFn = "main"
currFnRetType = "int"

def addFn():
  global top
  top += currFnRetType + " " + currFn + "() {\n" + fn + "}\n"

def newFn(name):
  global currFnRetType, currFn, fn
  currFnRetType = "void"
  currFn = name
  fn = ""

def addCode(code):
  global fn
  fn += "\t#line " + str(tokens.line+1) + " \"" + tokens.file + "\"\n"
  fn += "\t" + code

def save():
  addFn()
  with open("out.c", "w") as f:
    f.write(top)