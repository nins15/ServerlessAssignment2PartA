from flask import Blueprint
#from flask_login import current_user, login_user, logout_user, login_required

views=Blueprint('views',__name__)
@views.route('/')
def home():
    return "<h1>SuccessFully Login</h1>"