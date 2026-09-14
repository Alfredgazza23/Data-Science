import sys

def send_letter(search_email):
    try:
        with open("employees.tsv", 'r', encoding='utf-8') as file:
            next(file)  # пропускаем заголовок
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) != 3:
                    continue
                name, _, email = parts
                if email.strip() == search_email.strip():
                    print(
                        f"Dear {name}, welcome to our team. "
                        "We are sure that it will be a pleasure to work with you. "
                        "That’s a precondition for the professionals that our company hires."
                    )
                    return
        print("E-mail not found.")
    except FileNotFoundError:
        print("employees.tsv not found. Please run names_extractor.py first.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <email>")
    else:
        send_letter(sys.argv[1])
