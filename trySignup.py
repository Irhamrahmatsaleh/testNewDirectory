import re
import hashlib
import sqlite3

# Database setup
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
       (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT)''')
conn.commit()

def validate_username(username):
  if len(username) < 5:
    return False, "Username must be at least 5 characters long."
  if not re.match("^[a-zA-Z0-9_]+$", username):
    return False, "Username can only contain letters, numbers, and underscores."
  return True, ""

def validate_email(email):
  if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    return False, "Invalid email address."
  return True, ""

def validate_password(password):
  if len(password) < 8:
    return False, "Password must be at least 8 characters long."
  if not re.search("[a-z]", password):
    return False, "Password must contain at least one lowercase letter."
  if not re.search("[A-Z]", password):
    return False, "Password must contain at least one uppercase letter."
  if not re.search("[0-9]", password):
    return False, "Password must contain at least one number."
  if not re.search("[@#$%^&+=]", password):
    return False, "Password must contain at least one special character (@#$%^&+=)."
  return True, ""

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

def signup(username, email, password):
  valid, message = validate_username(username)
  if not valid:
    return False, message

  valid, message = validate_email(email)
  if not valid:
    return False, message

  valid, message = validate_password(password)
  if not valid:
    return False, message

  hashed_password = hash_password(password)

  try:
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
    conn.commit()
  except sqlite3.IntegrityError as e:
    return False, str(e)

  return True, "User registered successfully."

if __name__ == "__main__":
  username = input("Enter username: ")
  email = input("Enter email: ")
  password = input("Enter password: ")

  success, message = signup(username, email, password)
  if success:
    print(message)
  else:
    print("Error:", message)
