from flask_wft import Form
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, RecaptchaField
from wtforms.validators import DataRequired, Length, EqualTo, URL
from webapp.models import User

class LoginForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired(). Length(max=255)])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        if not check_validate:
            return False

        user = User.query.filter_by(username=self.username.data).first()

        if not user:
            self.username.errors.append('Invalid username or password.')
            return False
        if not self.user.check_passwrod(self.password.data):
            self.username.errors.append('Invalid username or password.')
            return False
        return True

class RegisterForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired(), Length(max=255)])
    confirm = PasswordField('Confirm', [DataRequired(), EqualTo('password')])

    recaptcha = RecaptchaField()

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        if not check_validate:
            return False
        
        user = User.query.filter_by(username=self.username.data).first()

        if user:
            self.username.errors.append("User with that name already exists.")

            return False
        
        return True


class PostForm(Form):
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Content', [DataRequired()])


class CommentForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    text = TextAreaField(u'Comment', validators=[DataRequired()])
