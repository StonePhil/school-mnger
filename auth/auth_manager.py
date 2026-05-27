import bcrypt
from database.connection import DBConnection

class AuthManager:
    def __init__(self, db: DBConnection):
        self.db = db

    def login(self) -> dict | None:
        print("\n- SCHOOL MANAGEMENT SYSTEM LOGIN -")

        for attempt in range(3):
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            result = self.db.fetch_all(
                "SELECT UserID, Username, PasswordHash, Role FROM Users WHERE Username = %s",
                (username,)
            )

            if not result:
                print("Invalid credentials.")
                continue

            user = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
                print(f"Login successful! Welcome, {username} ({user[3]})")
                return {
                    "user_id": user[0],
                    "username": user[1],
                    "role": user[3]
                }
            else:
                print("Invalid credentials.")

        print("Too many failed attempts.")
        return None

    def is_admin(self, user: dict) -> bool:
        return user and user["role"] == "Admin"

        def can_delete(self, user: dict) -> bool:
        #only admin can delete entries
            return user and user["role"] == "Admin"

    def is_teacher(self, user: dict) -> bool:
        return user and user["role"] in ["Admin", "Teacher"]

    def can_delete(self, user: dict) -> bool:
        #only admin can modify core entries
        return user and user["role"] == "Admin"
