from werkzeug.security import generate_password_hash, check_password_hash


class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, username, password):
        # Check if username is already taken
        existing_user = self.user_repository.get_user_by_username(username)
        if existing_user:
            raise ValueError('Username is already taken')

        # Hash the password and store the user in the repository
        hashed_password = generate_password_hash(password)
        self.user_repository.add_user(username, hashed_password)

    def authenticate_user(self, username, provided_password):
        # Get the user from the repository based on the username
        user = self.user_repository.get_user_by_username(username)
        if user:
            # Check if the password is correct
            return check_password_hash(user.password, provided_password)
        else:
            return None
