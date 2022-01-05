from instructions import variables as vars

typ = ""
code = ""
ctyp = ""

def ref(ref):
  global typ, ctyp, code
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