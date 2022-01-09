code = ""
file = ""
pos = 0
line = 0

oldLine = 0
oldPos = 0
oldCode = ""
oldFile = ""

def next_file(name, src):
  global code, file, pos, line, oldLine, oldPos, oldCode, oldFile
  if (oldFile != ""):
    return "imports aren't allowed in imported files!"
  oldCode = code
  oldFile = file
  oldLine = line
  oldPos = pos
  code = src
  file = name
  pos = 0
  line = 0
  return ""

def prev_file():
  global code, file, pos, line, oldLine, oldPos, oldCode, oldFile
  code = oldCode
  file = oldFile
  pos = oldPos
  line = oldLine
  oldCode = ""
  oldFile = ""
  oldPos = 0
  oldLine = 0

next_instr = ""
def next_instruction():
  global code, pos, next_instr, line
  if pos >= len(code)-1:
    return True

  char = code[pos]
  if pos != 0:
    # Get to next line if not at top
    while char != "\n":
      char = code[pos]
      pos += 1
      if char == "\n":
        line += 1
      if pos >= len(code)-1:
        return True

  
  # Get to next char
  char = code[pos]
  if char == "\n":
    line += 1
  
  while char == " " or char == "\t" or char == "\n":
    pos += 1
    if pos >= len(code)-1:
      return True
    char = code[pos]
    if char == "\n":
      line += 1
  
  # Get to end of instruction
  next_instr = ""
  char = code[pos]
  while char != " " and char != "\n":
    next_instr += char
    pos += 1
    if pos >= len(code)-1:
      next_instr += code[pos]
      break
    char = code[pos]
    if char == "\n":
      line += 1
  return False

def get_next_param():
  global code, pos, line

  # Get first char of param
  char = code[pos]
  while char == " ":
    pos += 1
    char = code[pos]
  
  # Get param
  openQuote = False
  running = True
  param = ""
  while running:
    # Check if at end
    if is_paramend():
      running = False

    # if not at end
    if running:
      char = code[pos]
      canAdd = True

      # Quote Check
      if char == "\"":
        openQuote = not openQuote
        canAdd = False
      
      # Check if at end
      if (char == " " or char == "\n") and (not openQuote):
        running = False
        canAdd = False
        if char == "\n":
          line += 1
      
      # Add char to param
      if canAdd:
        param += char
      pos += 1
  return param

def is_paramend():
  return pos >= len(code) or code[pos] == "\n" or code[pos] == "#"