typ = ""
code = ""

def ref(ref):
  global typ, code
  if ref.isnumeric():
    typ = "float"
    code = float(ref)
    return
  
  typ = "string"
  code = "\"" + ref + "\""