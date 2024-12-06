from flask import Flask, session, render_template, request, redirect
import pyrebase

app = Flask(__name__)

# Firebase Config
config = {
    'apiKey': "AIzaSyA2gZa08Y4XGBcNw-RTL1dW7HgdT3iJsJE",
    'authDomain': "blind-authentication.firebaseapp.com",
    'projectId': "blind-authentication",
    'storageBucket': "blind-authentication.firebasestorage.app",
    'messagingSenderId': "579975600367",
    'appId': "1:579975600367:web:7d13d1cfe74425c103a31a",
    'measurementId': "G-284WQMWP1K",
    'databaseURL': "https://blind-authentication-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app.secret_key = 'secret'

@app.route('/', methods=['GET'])
def index():
    # return render_template('blind.html')
    return render_template('index.html')
@app.route('/message')
def message():
    return render_template('message.html')
# Login Route
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            # Authenticate user
            user = auth.sign_in_with_email_and_password(email, password)

            # Fetch user data from Firebase Realtime Database
            users = db.child("users").get().val()
            for key, value in users.items():
                if value['email'] == email:
                    session['user'] = value['name']
                    return redirect('/message')  # Redirect to the message page

            return "User not found in the database."
        except Exception as e:
            return f"Error: {e}"

    return render_template('login.html')



#signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        try:
            # Create user in Firebase Authentication
            user = auth.create_user_with_email_and_password(email, password)

            # Save user data to Firebase Realtime Database
            data = {
                "name": name,
                "email": email
            }
            db.child("users").push(data)

            # Redirect to the login page
            return redirect('/login')
        except Exception as e:
            return f"Error: {e}"

    return render_template('signup.html')



# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user from session
    return redirect('/')  # Redirect to the login page

if __name__ == '__main__':
    app.run(port=1111, debug=True)
