from flask import Flask, request, redirect, render_template
from database import find_user, add_user

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = find_user(email, password)
        if user:
            return render_template('response.html', title="Login Successful", message="Welcome back!", success=True)
        else:
            return render_template('response.html', title="Login Failed", message="Invalid credentials. Please try again.", success=False)

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']# approach 1 to get the data from form
        password = request.form.get('password') # approach 2 to get the data from form

        # Check if the user already exists
        if find_user(email):
            return render_template('response.html', title="Signup Failed", message="User already exists. Please log in.", success=False)

        # Add user to the database
        add_user(name, email, password)
        return render_template('response.html', title="Signup Successful", message="Your account has been created successfully!", success=True)
        
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)