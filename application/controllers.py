from flask import render_template, request, redirect, make_response, Response
from flask import current_app as app
from application.database import db
from application.models import User, List, Card
from functools import wraps
from datetime import datetime


def protected_route(f):
    @wraps(f)
    def decorator():
        user_id = request.cookies.get('user')
        if user_id:
            user_ref = User.query.get(int(user_id))
            request.user = user_ref
            return f()
        return redirect('/login')
    return decorator


def check_user(f):
    @wraps(f)
    def decorator():
        if request.cookies.get('user'):
            return redirect('/')
        return f()
    return decorator


@app.route("/", methods=["GET", "POST"])
@protected_route
def home():
    user_id = request.user.user_id
    lists = List.query.filter_by(user=user_id).all()
    return render_template('home.html', title="Home", lists=lists)


@app.route("/summary", methods=["GET", "POST"])
@protected_route
def summary():
    return render_template("summary.html", title="Summary")


# User routes

@app.route("/register", methods=["GET", "POST"])
@check_user
def register():
    if request.method == "GET":
        return render_template("register.html", title="Register")
    if request.method == "POST":
        form_data = request.form

        email = form_data["email"]
        username = form_data["username"]
        password = form_data["password"]

        new_user = User(email=email, username=username, password=password)

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
@check_user
def login():
    if request.method == "GET":
        return render_template("login.html", title="Login")
    if request.method == "POST":
        form_data = request.form

        username = form_data["username"]
        password = form_data["password"]

        user = User.query.filter_by(username=username).first()

        response = make_response(redirect("/"))
        response.set_cookie('user', str(user.user_id))

        return response


@app.route("/logout", methods=["GET"])
def logout():
    if request.method == "GET":
        response = make_response(redirect("/login"))
        response.set_cookie('user', "")

        return response


# List routes

@app.route("/list/add", methods=["GET", "POST"])
@protected_route
def add_list():
    if request.method == "GET":
        return render_template("add_list.html", title="Add a List")
    if request.method == "POST":
        form_data = request.form

        name = form_data["name"]

        user_id = request.user.user_id

        new_list = List(name=name, user=user_id)
        db.session.add(new_list)
        db.session.commit()

        return redirect("/")


@protected_route
@app.route("/list/edit/<int:list_id>", methods=["GET", "POST"])
def edit_list(list_id):
    if request.method == "GET":
        list = List.query.get(list_id)
        return render_template("edit_list.html", title="Edit a List", list=list)
    if request.method == "POST":
        print('ksngk here ')
        form_data = request.form

        name = form_data["name"]

        list = List.query.get(list_id)

        list.name = name

        db.session.add(list)
        db.session.commit()

        return redirect("/")


@protected_route
@app.route("/list/delete/<int:list_id>", methods=["GET"])
def delete_list(list_id):
    list = List.query.get(list_id)

    db.session.delete(list)

    db.session.commit()

    return redirect('/')


# Card routes

@protected_route
@app.route("/card/add/<int:list_id>", methods=["GET", "POST"])
def add_card(list_id):
    if request.method == "GET":
        return render_template("add_card.html", title="Add a Card", list_id=list_id)
    if request.method == "POST":
        form_data = request.form

        dt = datetime.strptime(form_data["deadline"], '%Y-%m-%d')
        d = dt.date()

        title = form_data["title"]
        content = form_data["content"]
        deadline = d
        completed = form_data["done"]
        list_id = list_id

        new_card = Card(title=title, content=content,
                        deadline=deadline, completed=completed, list=list_id)

        db.session.add(new_card)
        db.session.commit()

        return redirect("/")


@app.route("/card/edit/<int:card_id>", methods=["GET", "POST"])
def edit_card(card_id):
    if request.method == "GET":
        card = Card.query.get(card_id)
        user_id = request.cookies.get('user')
        lists = List.query.filter_by(user=user_id).all()
        return render_template("edit_card.html", title="Edit a Card", lists=lists, card=card)
    if request.method == "POST":
        form_data = request.form

        dt = datetime.strptime(form_data["deadline"], '%Y-%m-%d')
        d = dt.date()

        list_id = form_data["list"]

        title = form_data["title"]
        content = form_data["content"]
        deadline = d
        completed = form_data["done"]
        list_id = list_id

        card = Card.query.get(card_id)

        card.title = title
        card.content = content
        card.deadline = deadline
        card.completed = completed
        card.list = list_id

        db.session.add(card)
        db.session.commit()

        return redirect("/")


@app.route("/card/delete/<int:card_id>", methods=["GET"])
def delete_card(card_id):
    card = Card.query.get(card_id)

    db.session.delete(card)

    db.session.commit()

    return redirect('/')
