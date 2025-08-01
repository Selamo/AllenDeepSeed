import re
# List of 20+ common passwords
COMMON_PASSWORDS = [
    "123456", "password", "000000000", "11111111111", "jesus", "20005", "superman", "welcome", "iloveyou", "football", "dragon", "handball", "2006", "qwerty", "johndoe"
]
score = 0
#Function to analyze the password
def analyze_password(password):
    score = 0
    suggestions = []
    results = []

#checking the lenth
    if len(password) >= 8:
        score += 20
        results.append("✔Length requirement ")
    else:
        results.append(" Too short( min 8 characters)")
        suggestions.append("Use atleast 8 characters")

        if re.search(r"[A-Z]", password):
            score += 20
            results.append("Contains Uppercase")
        else:
            results.append("No uppercase letters")
            suggestions.append("Add at least one uppercase letter")

        if re.search(r"[a-z]", password):
            score += 20
            results.append("Contains lowercase letters")
        else:
            results.append("No lowercase letters")
            suggestions.append("Add at least one lowercase letter ")

        if re.search(r"\d", password):
            score += 20
            results.append("Contains numbers")
        else:
            results.append("No numbers")
            suggestions.append("Add at least one number (0-9)")

        if re.search(r"[!@#$%^&*_]", password):
            score += 20
            results.append("Contains special characters")
        else:
            results.append("No special characters")
            suggestions.append("Add atleast a special character")
        
        if password.lower() in COMMON_PASSWORDS:
            results.append("Common password detected")
            suggestions.append("Avoid common passwords")
        else:
            score += 20
            results.append("Not a common password")

        if score > 100:
            level = "Excellent"
        elif score > 80:
            level = "Strong"
        elif score > 60:
            level = "Good"
        elif score > 40:
            level = "Fair"
        else:
            level = "Weak"
        
        return score, level, results, suggestions

def main():
    while True:
        print("===  PASSWORD SECURITY ANALYZER ===")
        password = input("Enter password to analyze: ")
        if password == "exit":
            break
        else:
            score, level, results, suggestions = analyze_password(password)
            # if score <= 40:
            #     password = input("Enter password to analyze: ")
            #     score, level, results, suggestions = analyze_password(password)
            # else:
            #     break
            print("\n SECURITY ANALYSIS RESULTS")
            print(f"Password: {password}")
            print(f"Score: {score}/120 ({level})\n")

            for r in results:
                print(r)

            if suggestions:
                print("\n SUGGESTIONS: ")
                for s in suggestions:
                    print(f"- {s}")

            else:
                print("\n Your password is cool")

main()


