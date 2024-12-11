from app.repositories.user_repository import UserRepository

class DataService:
    def process_data(self, user_id):
        user = UserRepository().get_user(user_id)
        # Logic to process user data
        if user:
            print(f"Processing data for user: {user.name}")
        else:
            print("User not found")
