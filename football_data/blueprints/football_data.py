from flask import Blueprint, render_template

football_data_bp = Blueprint('football_data_bp', __name__)

@football_data_bp.route('/')
def index():
    return render_template('football_data/index.html')
