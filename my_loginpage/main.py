import streamlit as st
import yaml

def load_users():
    try:
        with open('users.yaml', 'r') as file:
            return yaml.safe_load(file) or {}
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.yaml', 'w') as file:
        yaml.dump(users, file, default_flow_style=False)

def login(username, password, users):
    if username in users and users[username] == password:
        st.success("Login Successful")
    else:
        st.error("Incorrect username or password")

def handle_login(users):
    em = st.text_input("Username")
    ps = st.text_input("Password", type="password")
    login_button = st.button("Login")
    
    if login_button:
        login(em, ps, users)

def handle_signup(users):
    em = st.text_input("Email Address")
    ps1 = st.text_input("Password", type="password")
    ps2 = st.text_input("Confirm Password", type="password")
    us1 = st.text_input("Enter your unique username")
    signup_button = st.button("Create My Account")

    if signup_button:
        if us1 in users:
            st.error("Username already exists")
        elif ps1 != ps2:
            st.error("Passwords do not match")
        else:
            users[us1] = ps1
            save_users(users)  # Save new user to YAML file
            st.success("Account created successfully")

users = load_users()

st.title("Welcome to :violet[Codehelp]")
st.markdown("## LOGIN PAGE")

choice = st.selectbox("Login/Sign Up", ["Login", "Sign Up"])

if choice == 'Login':
    handle_login(users)
else:
    handle_signup(users)

