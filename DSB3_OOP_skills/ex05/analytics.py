import os
from random import randint

class Research:
    def __init__(self, file):
        self.file = file

    def file_reader(self, has_header=True):
        with open(self.file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        header = lines[0].strip()
        if header in ('1,0', '0,1'):
            has_header = False

        if has_header:
            if header != 'head,tail':
                raise Exception(f"Invalid header")

        start = 1 if has_header else 0
        result = []

        for line in lines[start:]:
            values = line.strip().split(',')
            if len(values) != 2 or set(values) != {'0', '1'}:
                raise Exception(f"Invalid row: {line.strip()}")

            result.append([int(i) for i in values])

        return result

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            head = sum(row[0] for row in self.data)
            tail = sum(row[1] for row in self.data)
            return head, tail

        def fractions(self, head, tail):
            total = head + tail
            return head / total * 100, tail / total * 100

    class Analytics(Calculations):
        def predict_random(self, n):
            result = []
            for _ in range(n):
                x = randint(0, 1)
                result.append([x, int(not(x))])
            return result

        def predict_last(self):
            return self.data[len(self.data)-1]

        def save_file(self, data, name, exe):
            fileName = f'{name}.{exe}'
            data = str(data)
            with open(fileName, 'w', encoding='utf-8') as f:
                f.write(data)

