from tokens import *
import tokens
from lib import *

def include_instruction():
  import parse

  file = get_next_param()
  src = read(file)
  err = tokens.next_file(file, src)
  if err != "":
    data.error = err
    return
  parse.parse()
  tokens.prev_file()