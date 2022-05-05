import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

def create_app() -> Flask:
    app = Flask(__name__)
    db = SQLAlchemy()

    app.config["FLASK_AMIND_SWATCH"] = "cerulean"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.getcwd() + "/sqlite3.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Supress warning.
    app.config["SECRET_KEY"] = "i_love_donuts"

    class User(db.Model):  # type: ignore
        __tablename__ = "user"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        posts = db.relationship("Post", backref="user", lazy=True)

        def __repr__(self):
            return f"<{self.__class__.__name__} {repr(self.name)}>"

        def __str__(self):
            return f"I'm {self.__class__.__name__}"

    class Post(db.Model):  # type: ignore
        __tablename__ = "post"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

        def __repr__(self):
            return f"<{self.__class__.__name__} {repr(self.name)}>"

    admin = Admin(app, name="microblog", template_mode="bootstrap3")
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))

    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
