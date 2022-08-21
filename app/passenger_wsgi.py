import sys, os

INTERP = "<PATH TO PYTHON3 VIRTUAL ENV>/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from main import app as application
