from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="This field is required.")])
    password = PasswordField('Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='Password must be between 4 and 10 characters.')])
    remember = BooleanField('Remember me')
    submit = SubmitField("Sign In")

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='Password must be between 4 and 10 characters.')])
    new_password = PasswordField('New Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='Password must be between 4 and 10 characters.')])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='Password must be between 4 and 10 characters.')])
    submit = SubmitField("Change Password")

class TodoForm(FlaskForm):
    title = StringField("Enter a task", validators=[DataRequired(message="This field is required.")])
    description = StringField("Describe your task", validators=[DataRequired(message="This field is required.")])
    submit = SubmitField("Save")

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="This field is required.")])
    text = TextAreaField('Write your review', validators=[DataRequired(message="This field is required.")])
    rating = IntegerField('Rate it from 1 to 5', validators=[DataRequired(message="This field is required."), NumberRange(min=1, max=5, message="Rating must be between 1 and 5.")])
    submit = SubmitField('Submit')
