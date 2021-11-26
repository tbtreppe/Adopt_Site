from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Add pet form"""
    name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])
    species = SelectField("Category", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message=None)])
    notes = TextAreaField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Edit Pet Form"""
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")
