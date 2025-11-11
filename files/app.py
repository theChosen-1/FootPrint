from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Set up the database URI (using SQLite for this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications
app.secret_key = 'your_secret_key_here'  # Required for session management
db = SQLAlchemy(app)

# Model for users (for login/registration)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

with app.app_contect():
    db.create_all()
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # User chose to log in
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id  # Store user ID in session
            return redirect(url_for('home'))  # Redirect to home page
        else:
            return "Invalid credentials, please try again."

    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # 1️⃣ Check if passwords match
        if password != confirm_password:
            return "Passwords do not match. Please try again."

        # 2️⃣ Check if username or email already exists
        if User.query.filter_by(username=username).first():
            return "Username already exists!"
        if User.query.filter_by(email=email).first():
            return "Email already registered!"

        # 3️⃣ Hash the password and create the user
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        # 4️⃣ Redirect to login page after successful registration
        return redirect(url_for('login'))

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)

