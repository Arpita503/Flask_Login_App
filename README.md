

# 🛡️ Flask User Authentication App

-> This is a simple Flask web application designed for user authentication. It provides two main functionalities: Login and Signup. Users can create an account and log in using their credentials. The app verifies the entered information and shows the appropriate response message. 🎉

# Features 🌟

• Login: Users can log in using their email 📧 and password 🔐.

• Signup: Users can create a new account with their name, email, and password.

• Error handling: Displays messages for failed login attempts or when the user already exists. ⚠️

• Success Messages: A success message is shown when the login or signup action is successful. ✅

# Technologies Used ⚙️

• Flask: The Python web framework used to build the app. 🐍

• HTML/CSS: For designing the frontend pages and styling the user interface. 🎨

• Database: Custom database functions to store and retrieve user data (you'll need to implement the database logic). 🗄️

# Setup Instructions 🛠️

-> To run this app locally, follow these steps:

* Prerequisites ⚡

• Python 3.x

• Flask installed

• A custom database.py file with functions like find_user and add_user to interact with a database (you need to set up the actual database).

Step 1: Clone the Repository 🔽

- Clone the repository to your local machine to get started. You can do this with a git clone command.

Step 2: Install Dependencies 📦

- Ensure that Flask is installed. You can do this using the package manager pip to install Flask.

Step 3: Configure the Database 🔑

- Make sure your database.py file is set up with the necessary functions for finding users (find_user) and adding users (add_user).

Step 4: Run the App 🚀

- Start the app by running it locally. It will launch on http://127.0.0.1:5000/. Open this URL in your browser to interact with the app.

# File Structure 📂

• app.py: Main Flask application file that contains routes and logic for login/signup.

• database.py: Contains the logic for interacting with your database (e.g., adding and finding users).

• templates/: Folder containing HTML templates for different pages.

• login.html: Page for users to log in.

• signup.html: Page for users to create a new account.

• response.html: Page to display success or error messages after an action.

• requirements.txt: List of Python dependencies needed for the app.

# Endpoints 🔗

# / - Home Route 🏠

• Redirects users to the /login route.

# /login - Login Page 🔑

• GET: Displays the login form where users can enter their email and password.

• POST: Accepts the login credentials, validates them, and shows the result (either success or failure).

# /signup - Signup Page 📝

• GET: Displays the signup form where users can enter their name, email, and password.

• POST: Accepts the signup information and either adds the new user to the database or shows an error message if the user already exists.

# Template Files 🖥️

• login.html: Contains the login form where users can input their email and password.

• signup.html: Contains the signup form for new users to provide their name, email, and password.

• response.html: Displays success or error messages based on the action performed (login/signup).

# Notes ⚠️

• You will need to implement the actual database functionality in the database.py file for user authentication (e.g., checking for users and adding new ones).

• This app currently only supports basic user login and signup functionality
