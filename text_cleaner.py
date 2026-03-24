import re

def clean_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def to_lowercase(text):
    return text.lower()

def to_uppercase(text):
    return text.upper()

def count_words(text):
    words = text.split()
    return len(words)

def save_to_file(text, filename="output.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"\n✅ Text saved to {filename}")
    except Exception as e:
        print("❌ Error saving file:", e)

def main():
    print("=== TEXT CLEANER TOOL ===\n")

    try:
        user_text = input("Enter your text:\n")
    except Exception:
        print("❌ Input not supported in this environment.")
        return

    if not user_text.strip():
        print("❌ No text entered. Exiting.")
        return

    print("\nChoose an option:")
    print("1 - Clean extra spaces")
    print("2 - Convert to lowercase")
    print("3 - Convert to UPPERCASE")
    print("4 - Count words")
    print("5 - Do everything")

    choice = input("\nEnter option (1-5): ").strip()

    result = user_text

    if choice == "1":
        result = clean_spaces(result)
    elif choice == "2":
        result = to_lowercase(result)
    elif choice == "3":
        result = to_uppercase(result)
    elif choice == "4":
        print(f"\nWord count: {count_words(result)}")
        return
    elif choice == "5":
        result = clean_spaces(result)
        result = to_lowercase(result)
        print(f"\nWord count: {count_words(result)}")
    else:
        print("❌ Invalid choice.")
        return

    print("\n=== RESULT ===")
    print(result)

    save_option = input("\nDo you want to save result to file? (y/n): ").strip().lower()
    if save_option == "y":
        save_to_file(result)

if __name__ == "__main__":
    main()
