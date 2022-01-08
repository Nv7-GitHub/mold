from instructions import variables as vars

typ = ""
code = ""
ctyp = ""

# Types: float, bool, dict, string

def ref(ref):
  global typ, ctyp, code
  if ref == "{}":
    typ = "dict"
    ctyp = "struct hash_entry*"
    code = "NULL"
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
    code = ref
    return

  typ = "string"
  ctyp = "char*"
  code = "\"" + ref + "\""