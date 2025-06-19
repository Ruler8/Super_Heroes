from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///heroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

# Create models/tables
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(50), nullable=False)
    super_hero_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Hero {self.id}"
    
with app.app_context():
        db.create_all()

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form['hero']
        mask = request.form['mask']
        new_hero = Persona(names=name, super_hero_name=mask)
        try:
            db.session.add(new_hero)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        heroes = Persona.query.order_by(Persona.names).all()
        return render_template("index.html", heroes=heroes)
    
#delete
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_hero = Persona.query.get_or_404(id)
    try:
        db.session.delete(delete_hero)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR: {e}"
    
#update
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    hero = Persona.query.get_or_404(id)
    if request.method == "POST":
        hero.names = request.form['hero']
        hero.super_hero_name = request.form['mask']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template("edit.html", hero=hero)

        
if __name__ == "__main__":
   
    app.run(debug=True)
