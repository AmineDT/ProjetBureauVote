from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

# Initialize Flask app and login manager
app = Flask(__name__)
app.secret_key = 'secret'
login_manager = LoginManager()
login_manager.init_app(app)

# Configure database connection
db_connection = psycopg2.connect(
    host='localhost',
    port=5433,
    dbname='mydb',
    user='uic',
    password='abcd1234'
)

# User model
# User model
class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.is_active = True
    
    def get_id(self):
        return str(self.id)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def get_by_username(username):
        cursor = db_connection.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return User(result[0], result[1], result[2])
        else:
            return None

    @staticmethod
    def get_by_id(id):
        cursor = db_connection.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return User(result[0], result[1], result[2])
        else:
            return None
        
    @property
    def is_authenticated(self):
        return True


# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

# Routes
@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', current_user=current_user)
    else:
        return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.get_by_username(username)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cursor = db_connection.cursor()
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, generate_password_hash(password)))
        db_connection.commit()
        cursor.close()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Start Flask app
if __name__ == '__main__':
    app.run(debug=True)