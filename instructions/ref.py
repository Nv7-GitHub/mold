typ = ""
code = ""

def ref(ref):
  global typ, code
  if ref.isnumeric():
    typ = "float"
    code = str(float(ref))
    return
  
  typ = "string"
  code = "\"" + ref + "\""