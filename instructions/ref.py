from instructions import variables as vars
import data

typ = ""
code = ""
ctyp = ""

# Types: float, bool, dict, string

def ref(ref):
  global typ, ctyp, code
  if ref == "{}":
    typ = "dict"
    ctyp = "std::unordered_map<std::string, std::string>"
    code = ""
    return

  if ref == "()":
    typ = "stack"
    ctyp = "std::stack<std::string>"
    code = ""
    return
  
  if ref == "true":
    typ = "bool"
    ctyp = "bool"
    code = "true"
    return

  if ref == "false":
    typ = "bool"
    ctyp = "bool"
    code = "false"
    return

  if ref.isnumeric():
    typ = "float"
    ctyp = "float"
    code = str(float(ref))
    return

  if ref in vars.vartyps:
    typ = vars.vartyps[ref]
    ctyp = vars.varctyps[ref]
    code = data.namespace + ref
    return

  typ = "string"
  ctyp = "std::string"
  code = "\"" + ref + "\""