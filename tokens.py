code = ""
file = ""
pos = 0
line = 0

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
      if pos >= len(code)-1:
        return True

    pos += 1
    line += 1
  
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
  while char != " ":
    next_instr += char
    pos += 1
    if pos >= len(code)-1:
      return True
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
  return pos >= len(code) or code[pos] == "\n"