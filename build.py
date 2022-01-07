import os
import tempfile
from out import build_code
import data

def build():
  code = build_code()
  with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".c") as f:
    f.write(code)
    f.close()

    os.system("cc `pkg-config --cflags --libs --static bdw-gc` " + f.name + " -g -o " + data.progname)

    os.remove(f.name)
  print(code)