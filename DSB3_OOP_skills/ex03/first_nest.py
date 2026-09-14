import sys

class Research:

    def __init__(self, file):
        self.file = file

    def file_reader(self, has_header=True):
        with open(self.file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        header = lines[0].strip()
        if header in ('1,0', '0,1'):
            has_header=False

        if has_header:
            if header != 'head,tail':
                raise Exception(f"Invalid header")

        start = 1 if has_header else 0

        result= []

        for line in lines[start:]:
            values = line.strip().split(',')
            if len(values) != 2 or set(values) != {'0', '1'}:
                raise Exception(f"Invalid row: {line.strip()}")

            result.append([int(i) for i in values])

        return result

    class Calculations:
        def counts(self, data):
            head = sum(row[0] for row in data)
            tail = sum(row[1] for row in data)
            return head, tail

        def fractions(self, head, tail):
            total = head + tail
            f_head = f"{head / total:.5f}"  # 6 знаков = "0.xxxxx"
            f_tail = f"{tail / total:.5f}"
            return f_head[:6], f_tail[:6]    # Берем первые 7 символов "0.xxxx"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file>")
    else:
        try:
            d = Research(sys.argv[1])
            data=d.file_reader()
            print(data)
            head, tail = d.Calculations().counts(data)
            print(head, tail)
            f_head, f_tail = d.Calculations().fractions(head, tail)
            print(f_head, f_tail)

        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found")
        except Exception as e:
            print(f"Error: {e}")
