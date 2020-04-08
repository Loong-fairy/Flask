from flask import Blueprint

web = Blueprint('web', __name__)

from apps.web import book
from apps.web import user
