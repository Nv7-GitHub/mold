error = ""
progname = ""
namespace = "mold__"

scope = []
infunc = False
def get_scope():
  if len(scope) == 0:
    return ""
  return scope[-1]

def push_scope(newscope):
  global scope
  scope.append(newscope)

def pop_scope():
  global scope
  scope.pop()