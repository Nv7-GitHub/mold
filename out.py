from lib import *
import tokens
import os

top = read("top.c").replace("uthash.h", os.getcwd() + "/uthash.h")
code = ""

fn = "\targcnt = argc;\n\targval = argv;\n\tsrand(time(0));\n\n"
currFn = "main"
currFnRetType = "int"
variables = ""
indent = 1

mainFn = "\tGC_INIT();\n"
mainIndent = 1

def addVar(code):
  global variables
  variables += "#line " + str(tokens.line+1) + " \"" + tokens.file + "\"\n"
  variables += code

def addFn():
  global code, currFn, currFnRetType, mainFn, fn, indent, mainIndent
  args = ""
  if currFn == "main":
    args = "int argc, char** argv"
  code += currFnRetType + " " + currFn + "(" + args + ") {\n" + fn + "}\n\n"
  currFnRetType = "int"

  currFn = "main"
  fn = mainFn
  indent = mainIndent

def newFn(name):
  global currFnRetType, currFn, fn, mainFn, mainIndent, indent
  currFnRetType = "void"
  currFn = name

  mainFn = fn
  fn = ""
  mainIndent = indent
  indent = 0

def addCode(code):
  global fn
  fn += ("\t" * indent) + "#line " + str(tokens.line+1) + " \"" + tokens.file + "\"\n"
  fn += ("\t" * indent) + code

def build_code():
  global top
  addFn()
  top += variables
  top += "\n"
  top += code
  return top