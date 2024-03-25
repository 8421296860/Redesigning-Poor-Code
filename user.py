from storage import FileStorage

file_storage = FileStorage()

def add_user(name, user_id):
    """
    Add a new user to the system.

    Args:
        name (str): Name of the user.
        user_id (str): User ID of the user.
    """
    # Check if the user already exists
    for existing_user in file_storage.load_users():
        if existing_user['user_id'] == user_id:
            print("User with the same ID already exists.")
            return False

    # Add the user to the storage
    file_storage.save_user(name, user_id)

    print("User added successfully.")
    return True
