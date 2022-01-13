import os
import tempfile
from out import build_code
import data

def build():
  code = build_code()
  with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".cpp") as f:
    f.write(code)
    f.close()

    os.system("g++ -std=c++17 " + f.name + " -o " + data.progname)

    os.remove(f.name)
  print(code)