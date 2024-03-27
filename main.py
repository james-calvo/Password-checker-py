def check_password(password, difficulty):
    if difficulty == "Easy":
        if len(password) >= 6:
            return True
        else:
            print("Password must be at least 6 characters long")
            return False
    elif difficulty == "Medium":
        if len(password) >= 8 and any(char.isupper() for char in password) \
                and any(char.islower() for char in password) and any(char.isdigit() for char in password):
            return True
        else:
            feedback = []
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long")
            if not any(char.isupper() for char in password):
                feedback.append("Missing uppercase letter")
            if not any(char.islower() for char in password):
                feedback.append("Missing lowercase letter")
            if not any(char.isdigit() for char in password):
                feedback.append("Missing digit")
            print(", ".join(feedback))
            return False
    elif difficulty == "Hard":
        if len(password) >= 8 and any(char.isupper() for char in password) \
                and any(char.islower() for char in password) and any(char.isdigit() for char in password) \
                and any(not char.isalnum() for char in password):
            return True
        else:
            feedback = []
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long")
            if not any(char.isupper() for char in password):
                feedback.append("Missing uppercase letter")
            if not any(char.islower() for char in password):
                feedback.append("Missing lowercase letter")
            if not any(char.isdigit() for char in password):
                feedback.append("Missing digit")
            if not any(not char.isalnum() for char in password):
                feedback.append("Missing special character")
            print(", ".join(feedback))
            return False
    else:
        print("Invalid difficulty level")
        return False


def main():
    while True:
        difficulty = input("Choose difficulty level (Easy, Medium, Hard): ").strip().capitalize()
        if difficulty in {"Easy", "Medium", "Hard"}:
            break
        else:
            print("Invalid difficulty level. Please choose from Easy, Medium, or Hard.")

    while True:
        password = input("Enter your password: ").strip()
        if check_password(password, difficulty):
            print("Password meets complexity requirements.")
            break
        else:
            print("Password does not meet complexity requirements. Please try again.")


if __name__ == "__main__":
    main()
