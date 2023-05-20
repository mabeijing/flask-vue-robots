from flask import Blueprint

bp_l10n = Blueprint('bp_l10n', __name__, url_prefix='/l10n')

from .rules import *
