import hashlib

# Simulated user database
users_db = {
  "user1": "5f4dcc3b5aa765d61d8327deb882cf99",  # password: password
  "user2": "e99a18c428cb38d5f260853678922e03"   # password: abc123
}

def hash_password(password):
  return hashlib.md5(password.encode()).hexdigest()

def login(username, password):
  if username in users_db:
    hashed_password = hash_password(password)
    if users_db[username] == hashed_password:
      return "Login successful!"
    else:
      return "Invalid password."
  else:
    return "Username not found."

# Example usage
if __name__ == "__main__":
  username = input("Enter username: ")
  password = input("Enter password: ")
  print(login(username, password))
