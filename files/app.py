from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from security import check_login  # <-- import your login check logic

# ✅ Create ONE Flask app
app = Flask(__name__, static_folder='static')

# ✅ Configure and link the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'
db = SQLAlchemy(app)

# ===== User model =====
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Create tables
with app.app_context():
    db.create_all()


# ===== Home =====
@app.route("/")
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template("index.html")

# ===== Login POST with security checks =====
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = User.query.filter_by(username=username).first()

    # Use security module
    result = check_login(username, password, user)
    if result is None:
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect(url_for('dashboard'))
    else:
        return result

# ===== Signup POST =====
@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if password != confirm_password:
        return "Passwords do not match."

    if User.query.filter_by(username=username).first():
        return "Username already exists!"
    if User.query.filter_by(email=email).first():
        return "Email already registered!"

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('home'))

# ===== Dashboard =====
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    username = session.get('username', 'User')
    return render_template("dashboard.html", username=username)

# ===== Logout =====
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

# ===== Modals served separately =====
@app.route("/login_modal")
def login_modal():
    return render_template("login.html")

@app.route("/signup_modal")
def signup_modal():
    return render_template("signup.html")