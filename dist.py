import os

def create_directory(path):
  try:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")
  except OSError as error:
    print(f"Error creating directory '{path}': {error}")

if __name__ == "__main__":
  directory_path = "new_directory"
  create_directory(directory_path)
