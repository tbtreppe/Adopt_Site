from flask import Flask, render_template, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secrets"
app.config ['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

"""List the pets"""
@app.route('/index')
def list_pets():
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

"""Add a pet on a form """
@app.route('/pets/add', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age =  form.age.data
        notes = form.notes.data
        flash(f"Added a new animal: Name is {name}")

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age)
        db.session.add(pet)
        db.session.commit()
        
        return redirect('/index')

    else:
        return render_template("add_pet_form.html", form=form)

"""Get an edit pet form for a specific pet"""
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    pets = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    
    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        flash(f"Edit complete!")

        pets = Pet(photo_url=photo_url, available=available)
        db.session.add(pets)
        db.session.commit()
        
        return redirect('/index')

    else:
        return render_template('edit_pet_form.html', form=form, pets=pets)
