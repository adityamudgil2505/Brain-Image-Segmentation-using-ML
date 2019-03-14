from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    patient = db.relationship('Patient', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    age = db.Column(db.String(30), nullable=True)
    gender = db.Column(db.String(6), nullable=True)
    file_t1 = db.Column(db.String(90), nullable=True)
    file_flair = db.Column(db.String(90), nullable=True)
    file_ir = db.Column(db.String(90), nullable=True)
    file_y_true = db.Column(db.String(90), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"Patient('{self.first_name}', '{self.last_name}', '{self.age}', '{self.gender}', '{self.file_t1}','{self.file_flair}','{self.file_ir}', '{self.date_posted}')"