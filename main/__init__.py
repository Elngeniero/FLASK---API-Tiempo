from flask import Blueprint

main = Blueprint("main", __name__)

from . import routes  # importa las rutas
