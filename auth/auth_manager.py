# auth/auth_manager.py
"""
Authentication and Authorization Manager
Handles login, password verification, and role checking.
"""

import bcrypt
from database.connection import DBConnection


class AuthManager:
    def __init__(self, db: DBConnection):
        self.db = db

    def login(self) -> dict | None:
        """Prompt for login and return user info if successful."""
        print("\n=== SCHOOL MANAGEMENT SYSTEM LOGIN ===")
        
        for attempt in range(3):
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            # Get user from database
            result = self.db.fetch_all(
                "SELECT UserID, Username, PasswordHash, Role FROM Users WHERE Username = %s",
                (username,)
            )

            if not result:
                print("Invalid username or password.")
                continue

            user = result[0]
            stored_hash = user[2]

            if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                print(f"Login successful! Welcome, {username} ({user[3]})")
                return {
                    "user_id": user[0],
                    "username": user[1],
                    "role": user[3]
                }
            else:
                print("Invalid username or password.")

        print("Too many failed attempts. Exiting...")
        return None

    def is_admin(self, current_user: dict) -> bool:
        """Check if current user has Admin privileges."""
        return current_user and current_user["role"] == "Admin"
