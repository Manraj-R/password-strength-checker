# PassGuard: A console-based password strength checker
# Built to evaluate passwords with a human-friendly score and tips
# No external libraries needed, just pure Python

def check_password_strength(password):
    """Evaluate password strength based on length and character types."""
    score = 0
    tips = []

    # Length check: longer passwords get more points
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    elif len(password) >= 4:
        score += 1
    else:
        tips.append("Too short! Use at least 8 characters for better security.")

    # Character type checks
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add some uppercase letters to level up.")
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Mix in lowercase letters for variety.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Include numbers for extra strength.")
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        tips.append("Special characters (e.g., !@#$%) make it stronger.")

    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Okay"
    else:
        strength = "Strong"

    return strength, score, tips

def main():
    """Main function to run the password checker."""
    print("\n=== PassGuard: Password Strength Checker ===")
    print("Enter a password to test its strength (or 'q' to quit).")
    
    while True:
        password = input("\nPassword: ").strip()
        if password.lower() == 'q':
            print("Thanks for using PassGuard! Stay secure!")
            break
        
        strength, score, tips = check_password_strength(password)
        
        # Display results with some flair
        print(f"\nStrength: {strength} (Score: {score}/7)")
        if tips:
            print("Tips to improve:")
            for i, tip in enumerate(tips, 1):
                print(f"  {i}. {tip}")
        else:
            print("Your password is solid! Nice work!")

if __name__ == "__main__":
    main()