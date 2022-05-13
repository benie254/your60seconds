from flask import Blueprint
app = Blueprint('auth',__name__)  # blueprint instance
from . import views, forms