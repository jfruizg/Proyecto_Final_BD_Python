from flask import Blueprint, render_template, request, redirect, url_for, flash

user = Blueprint('user', __name__)

@user.route("/login")
def login():
    return render_template("./User/login.html")

@user.route("/register")
def register():
    return render_template("./User/login.html")