import json
import os

def create_users_file():
    users = []

    print("=" * 50)
    print("Enter users data (enter empty login to stop adding)")

    while True:
        print(f"\nUser {len(users) + 1}:")
        login = input("Login: ").strip()

        if not login:
            break

        email = input("Email: ").strip()
        username = input("Username: ").strip()
        active_input = input("Active? (y/n): ").strip().lower()
        is_active = active_input == 'y'
        last_seen = input("Last seen (DDMMYYYY): ").strip()

        user = {
            "id": len(users) + 1,
            "login": login,
            "email": email,
            "username": username,
            "isActive": is_active,
            "lastSeen": last_seen
        }

        users.append(user)
        print(f"User '{login}' is added!")

    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii=False)

    print("\nFile 'users.json' has been created!")


def read_users_file():
    print("=" * 50)
    if not os.path.exists("users.json"):
        print("File 'users.json' wasn't found!")
        return

    try:
        with open("users.json", "r", encoding="utf-8") as file:
            users = json.load(file)

        print("Users:")

        if not users:
            print("No users in the file")
            return

        for user in users:
            status = "Active" if user["isActive"] else "Inactive"

            date_str = user["lastSeen"]
            if len(date_str) == 8:
                formatted_date = f"{date_str[:2]}.{date_str[2:4]}.{date_str[4:]}"
            else:
                formatted_date = date_str

            print(f"\nid: {user['id']}")
            print(f"Login: {user['login']}")
            print(f"Email: {user['email']}")
            print(f"Username: {user['username']}")
            print(f"Status: {status}")
            print(f"Last seen: {formatted_date}")

        print(f"\nNum of users: {len(users)}")

    except Exception as e:
        print(f"Read error: {e}")

while True:
    print("=" * 50)
    print("JSON Database")
    print("1 - Create new JSON with users")
    print("2 - Show all users")
    print("3 - Exit")

    choice = input("\nChoose (1-3): ").strip()

    if choice == "1":
        create_users_file()
    elif choice == "2":
        read_users_file()
    elif choice == "3":
        print("Goodbye world!")
        break
    else:
        print("Yomayo, nu skazali tebe angliyskim yazykom 'Choose (1-3)'")
