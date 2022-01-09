import data
from out import *
import out
from instructions import switch

def end_instruction():
  if data.scopetype == "proc":
    addFn()
  if data.scopetype == "if" or data.scopetype == "while":
    out.indent -= 1
    addCode("}\n")
  if data.scopetype == "switch":
    addCode("mold_switch_run(" + switch.switch_val_code + ", &mold_switchval_" + str(switch.switch_count - 1) + ", " + switch.default + ");\n")
    addCode("mold_switch_free(&mold_switchval_" + str(switch.switch_count - 1) + ");\n")
  
  data.scopetype = ""