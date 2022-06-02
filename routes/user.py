from flask import Blueprint, render_template, request, redirect, url_for, flash

user = Blueprint('user', __name__)


@user.route("/login")
def home():
    return render_template('./views/user/login.html')
