from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class AddPatient(FlaskForm):
    firstName = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastName = StringField('Last Name',
                            validators=[DataRequired(), Length(min=2, max=20)])
    age = StringField('Age',
                            validators=[DataRequired(), Length(min=2, max=20)])
    gender = RadioField('Gender', validators=[DataRequired()], choices = [('M','Male'),('F','Female')], default='M')
    file_T1 = FileField('Upload T1 File', validators=[DataRequired(), FileAllowed(['nii.gz', 'nii', 'gz', 'jpg'])])
    file_FLAIR = FileField('Upload FLAIR File', validators=[DataRequired(), FileAllowed(['nii.gz', 'nii', 'gz', 'jpg'])])
    file_IR = FileField('Upload IR File', validators=[DataRequired(), FileAllowed(['nii.gz', 'nii', 'gz', 'jpg'])])
    file_y_True = FileField('Y_True File', validators=[FileAllowed(['nii.gz', 'nii', 'gz', 'jpg', 'npy'])])
    submit = SubmitField('Add')