from instructions.os import *
from instructions.variables import *
from instructions.math import *
from instructions.strings import *
from instructions.dict import *
from instructions.scope import *
from instructions.proc import *
from tokens import *

def comment_instruction():
  while not is_paramend():
    get_next_param()