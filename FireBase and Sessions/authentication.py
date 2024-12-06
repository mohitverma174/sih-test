import pyrebase

config = {
    'apiKey': "AIzaSyA2gZa08Y4XGBcNw-RTL1dW7HgdT3iJsJE",
    'authDomain': "blind-authentication.firebaseapp.com",
    'projectId': "blind-authentication",
    'storageBucket': "blind-authentication.firebasestorage.app",
    'messagingSenderId': "579975600367",
    'appId': "1:579975600367:web:7d13d1cfe74425c103a31a",
    'measurementId': "G-284WQMWP1K",
    'databaseURL': "https://blind-authentication-default-rtdb.asia-southeast1.firebasedatabase.app/"  # Add your database URL here
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'test@gmail.com'
password = '123456'

#user = auth.create_user_with_email_and_password(email, password)
#print(user)

user = auth.sign_in_with_email_and_password(email, password)

#info = auth.get_account_info(user['idToken'])
# print(info) 

#auth.send_email_verification(user['idToken'])

auth.send_password_reset_email(email)