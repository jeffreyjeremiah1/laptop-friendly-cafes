from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class AddCafesForm(FlaskForm):
    cafe_name = StringField(validators=[DataRequired()])


class Cafes(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer(), primary_key=True)
    img_url = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(), nullable=False)
    has_sockets = db.Column(db.String(), nullable=False)
    has_toilet = db.Column(db.String(), nullable=False)
    has_wifi = db.Column(db.String(), nullable=False)
    can_take_calls = db.Column(db.String(), nullable=False)
    seats = db.Column(db.Integer(), nullable=False)
    coffee_price = db.Column(db.Integer(), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def get_all_cafes():
    all_cafes = Cafes.query.all()
    print(all_cafes)
    return render_template("cafes.html", all_cafes=all_cafes)


@app.route("/add_cafe", methods=["GET", "POST"])
def add_cafe():
    form = AddCafesForm()
    if request.method == "POST":
        cafe = form.cafe_name.data
        return render_template("cafes.html", cafe=cafe)
    return render_template("add_cafe.html", form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
