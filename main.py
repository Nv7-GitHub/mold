from parse import parse
from build import build
import sys
import tokens
from lib import read
import data

tokens.file = sys.argv[1]
tokens.code = read(tokens.file)
data.progname = sys.argv[2]

parse()
build()
