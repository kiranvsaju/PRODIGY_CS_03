import re

def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))
    
    # Feedback based on criteria
    feedback = []
    all_criteria_met = True
    
    if length_criteria:
        feedback.append("Length: Good (8 or more characters)")
    else:
        feedback.append("Length: Weak (less than 8 characters)")
        all_criteria_met = False
    
    if lowercase_criteria:
        feedback.append("Lowercase Letters: Present")
    else:
        feedback.append("Lowercase Letters: Missing")
        all_criteria_met = False
    
    if uppercase_criteria:
        feedback.append("Uppercase Letters: Present")
    else:
        feedback.append("Uppercase Letters: Missing")
        all_criteria_met = False
    
    if number_criteria:
        feedback.append("Numbers: Present")
    else:
        feedback.append("Numbers: Missing")
        all_criteria_met = False
    
    if special_char_criteria:
        feedback.append("Special Characters: Present")
    else:
        feedback.append("Special Characters: Missing")
        all_criteria_met = False
    
    # Calculate strength score
    strength_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])
    
    # Determine strength level
    if strength_score == 5:
        strength_level = "Very Strong"
    elif strength_score == 4:
        strength_level = "Strong"
    elif strength_score == 3:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"
    
    return feedback, strength_level, all_criteria_met

def main():
    while True:
        password = input("Enter a password to assess its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Exiting the program.")
            break
        feedback, strength_level, all_criteria_met = assess_password_strength(password)
        print("\nPassword Strength Assessment:")
        for line in feedback:
            print(f"- {line}")
        print(f"Overall Strength: {strength_level}\n")
        
        if not all_criteria_met:
            print("Your password does not meet all criteria. Please consider changing your password to make it stronger.\n")

if __name__ == "__main__":
    main()
