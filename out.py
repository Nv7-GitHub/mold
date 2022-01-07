from lib import *
import tokens
import os

top = read("top.c").replace("uthash.h", os.getcwd() + "/uthash.h")
code = ""

fn = ""
currFn = "main"
currFnRetType = "int"
variables = ""
mainFn = "\tGC_INIT();\n"

def addVar(code):
  global variables
  variables += "#line " + str(tokens.line+1) + " \"" + tokens.file + "\"\n"
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

def build_code():
  global top
  addFn()
  top += variables
  top += "\n"
  top += code
  return top