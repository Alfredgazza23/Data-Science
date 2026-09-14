import sys

def extractor(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file, \
             open("employees.tsv", 'w', encoding='utf-8') as employees:
            employees.write("Name\tSurname\tE-mail\n")
            for email in file.read().splitlines():
                try:
                    name_part, domain = email.split('@')
                    first, last = name_part.split('.')
                    first = first.capitalize()
                    last = last.capitalize()
                    employees.write(f"{first}\t{last}\t{email}\n")
                except ValueError:
                    continue
        print("Saved as employees.tsv")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <emails.txt>")
    else:
        extractor(sys.argv[1])
