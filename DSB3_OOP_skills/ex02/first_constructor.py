import sys
import os

class Research:
    def __init__(self, file):
        self.file = file

    def file_reader(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        header = lines[0].strip()
        count=1
        if header != 'head,tail':
            raise Exception(f"in {os.path.abspath(self.file)} line {count}, Invalid header")
        for line in lines[1:]:
            values = line.strip().split(',')
            count+=1
            if len(values) != 2 or set(values) != {'0', '1'}:
                raise Exception(f"in {os.path.abspath(self.file)} line {count}, Invalid row: {line.strip()}")

        return ''.join(lines)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file>")
    else:
        try:
            print(Research(sys.argv[1]).file_reader())
        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found")
        except Exception as e:
            print(f"Error: {e}")
