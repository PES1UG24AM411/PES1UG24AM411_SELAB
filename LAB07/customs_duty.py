
import math


def parse_declaration(text):
    if not isinstance(text, str):
        raise ValueError("Declaration must be a string")

    if text.count(":") != 1:
        raise ValueError("Declaration must contain exactly one ':'")

    category, value = text.split(":")

    category = category.strip().lower()

    if not category:
        raise ValueError("Category cannot be empty")

    try:
        value = float(value)
    except ValueError:
        raise ValueError("Value must be numeric")

    if not math.isfinite(value) or value < 0:
        raise ValueError("Value must be finite and non-negative")

    return category, value


def duty_amount(text):
    if not isinstance(text, str):
        raise ValueError("Duty input must be a string")

    if text.count("@") != 1:
        raise ValueError("Input must contain exactly one '@'")

    value, rate = text.split("@")

    try:
        value = float(value)
        rate = float(rate)
    except ValueError:
        raise ValueError("Value and rate must be numeric")

    if not math.isfinite(value) or not math.isfinite(rate):
        raise ValueError("Value and rate must be finite")

    if value < 0 or rate < 0:
        raise ValueError("Value and rate cannot be negative")

    return value * rate / 100


def hs_chapter(code):
    if not isinstance(code, str):
        raise ValueError("HS code must be a string")

    parts = code.strip().split(".")

    if not parts[0].isdigit() or len(parts[0]) < 2:
        raise ValueError("Invalid HS chapter")

    if len(parts) > 2 or any(not part.isdigit() for part in parts):
        raise ValueError("Invalid HS code")

    return int(parts[0][:2])


def main():
    print("==== Running parse_declaration ====")
    user_input = input("Enter category:value (e.g. electronics:25000): ")
    result = parse_declaration(user_input)
    print("Category and Value:", result)

    print("\n==== Running duty_amount ====")
    user_input = input("Enter value@rate (e.g. 25000@20): ")
    result = duty_amount(user_input)
    print("Duty Amount:", result)

    print("\n==== Running hs_chapter ====")
    user_input = input("Enter an HS code (e.g. 8517.12): ")
    result = hs_chapter(user_input)
    print("Chapter:", result)


if __name__ == "__main__":
    main()
