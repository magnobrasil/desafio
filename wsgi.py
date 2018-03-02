#
# Conteudo do arquivo `wsgi.py`
#
import sys

sys.path.insert(0, "/opt/projeto/desafio-master/")

from main.py import app as application
