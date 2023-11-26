from flask import Blueprint

main_bp = Blueprint('main', __name__)

# Import views after the Blueprint is defined to avoid circular imports
from . import routes
