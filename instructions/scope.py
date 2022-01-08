import data
from out import *

def end_instruction():
  if data.scopetype == "proc":
    addFn()

  data.scopetype = ""