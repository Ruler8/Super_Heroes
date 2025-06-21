from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///heroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# --------------------- MODELS ---------------------

# Main Hero Table
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(50), nullable=False)
    super_hero_name = db.Column(db.String(50), nullable=False)

    powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Hero {self.id} - {self.names} ({self.super_hero_name})>"


#Power Lookup Table
class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    hero_powers = db.relationship('HeroPower', backref='power', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Power {self.id} - {self.name}>"


# Linking Table with strength info
class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)

    def __repr__(self):
        return f"<HeroPower {self.id} - Hero:{self.hero_id} Power:{self.power_id} Strength:{self.strength}>"


# Create tables
with app.app_context():
    db.create_all()

# --------------------- ROUTES ---------------------

# Home Route
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form['hero']
        mask = request.form['mask']
        if not name or not mask:
            return "Hero name and Super Hero name are required.", 400

        new_hero = Persona(names=name, super_hero_name=mask)
        try:
            db.session.add(new_hero)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        heroes = Persona.query.order_by(Persona.names).all()
        return render_template("index.html", heroes=heroes)


# Delete Hero
@app.route("/delete/<int:id>")
def delete(id):
    delete_hero = Persona.query.get_or_404(id)
    try:
        db.session.delete(delete_hero)
        db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        return f"ERROR: {e}"


# Update Hero
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    hero = Persona.query.get_or_404(id)
    if request.method == "POST":
        hero.names = request.form['hero']
        hero.super_hero_name = request.form['mask']
        try:
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template("edit.html", hero=hero)


# Add Power
@app.route("/add_power", methods=["GET", "POST"])
def add_power():
    if request.method == "POST":
        name = request.form['power_name']
        if not name:
            return render_template("add_power.html", error="Power name is required.", powers=Power.query.all())

        existing_power = Power.query.filter_by(name=name).first()
        if existing_power:
            return render_template("add_power.html", error="This power already exists.", powers=Power.query.all())

        power = Power(name=name)
        try:
            db.session.add(power)
            db.session.commit()
            return redirect(url_for("add_power"))
        except Exception as e:
            return f"ERROR: {e}"

    powers = Power.query.order_by(Power.id).all()
    return render_template("add_power.html", powers=powers)



# Assign Power
@app.route("/assign_power", methods=["GET", "POST"])
def assign_power():
    if request.method == "POST":
        hero_id = request.form['hero_id']
        power_id = request.form['power_id']
        strength = request.form['strength']

        if not hero_id or not power_id or not strength:
            return "All fields are required.", 400

        hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
        try:
            db.session.add(hero_power)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return f"ERROR: {e}"
    else:
        heroes = Persona.query.order_by(Persona.names).all()
        powers = Power.query.order_by(Power.name).all()
        return render_template("assign_power.html", heroes=heroes, powers=powers)


#update power assignment
@app.route("/update_power/<int:id>", methods=["GET", "POST"])
def update_power(id):
    hero_power = HeroPower.query.get_or_404(id)
    if request.method == "POST":
        hero_power.power_id = request.form["power_id"]
        hero_power.strength = request.form["strength"]

        try:
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return f"Error updating power: {e}"
    else:
        heroes = Persona.query.all()
        powers = Power.query.all()
        return render_template("update_power.html", hero_power=hero_power, heroes=heroes, powers=powers)


#delete power assignment
@app.route("/delete_power/<int:id>")
def delete_power(id):
    hero_power = HeroPower.query.get_or_404(id)
    try:
        db.session.delete(hero_power)
        db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        return f"Error deleting power: {e}"


#update power
@app.route("/edit_power/<int:id>", methods=["GET", "POST"])
def edit_power(id):
    power = Power.query.get_or_404(id)
    if request.method == "POST":
        new_name = request.form['power_name']
        if not new_name:
            return render_template("edit_power.html", power=power, error="Power name cannot be empty.")
        power.name = new_name
        db.session.commit()
        return redirect(url_for('add_power'))
    return render_template("edit_power.html", power=power)






# --------------------- MAIN ---------------------
if __name__ == "__main__":
    app.run(debug=True)
