import re
import math


def calculate_entropy(password):
    """Estimate password entropy."""
    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"\d", password):
        charset_size += 10

    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    return len(password) * math.log2(charset_size)


def analyze_password(password):
    score = 0
    feedback = []

    # Length analysis
    if len(password) >= 16:
        score += 30
    elif len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        feedback.append("Consider using at least 12 characters.")
    else:
        feedback.append("Password is too short. Use at least 12 characters.")

    # Character types
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add special characters.")

    # Penalties for common patterns
    common_patterns = [
        r"password",
        r"123456",
        r"qwerty",
        r"admin",
        r"letmein",
    ]

    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            score -= 25
            feedback.append(
                f"Your password contains a common pattern: '{pattern}'."
            )

    # Sequential numbers or letters
    if re.search(r"123|234|345|456|567|678|789", password):
        score -= 10
        feedback.append("Avoid predictable number sequences.")

    if score < 0:
        score = 0

    if score >= 85:
        strength = "VERY STRONG"
    elif score >= 65:
        strength = "STRONG"
    elif score >= 40:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    entropy = calculate_entropy(password)

    return score, strength, entropy, feedback


def main():
    print("\n" + "=" * 55)
    print("       PASSWORDIUM - ADVANCED PASSWORD ANALYZER")
    print("              © 2026 Malek F Saleh")
    print("=" * 55)

    print("\nType 'exit' to close the program.")

    while True:
        password = input("\nEnter a password to analyze: ")

        if password.lower() == "exit":
            print("\nThank you for using Passwordium.")
            break

        if not password:
            print("Please enter a password.")
            continue

        score, strength, entropy, feedback = analyze_password(password)

        print("\n" + "-" * 55)
        print(f"PASSWORD STRENGTH: {strength}")
        print(f"SECURITY SCORE:    {score}/100")
        print(f"ESTIMATED ENTROPY: {entropy:.2f} bits")
        print("-" * 55)

        if feedback:
            print("\nSECURITY RECOMMENDATIONS:")
            for item in feedback:
                print(f"  • {item}")
        else:
            print("\nExcellent password security!")


if __name__ == "__main__":
    main()