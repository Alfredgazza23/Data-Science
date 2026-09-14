import os
from random import randint

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file>")
    else:
        try:
            from analytics import Research
            d = Research(sys.argv[1])
            data = d.file_reader()
            print(data)

            from analytics import Research
            a = Research.Analytics(data)

            head, tail = a.counts()
            print(head, tail)

            f_head, f_tail = a.fractions(head, tail)
            print(f_head, f_tail)

            predict_data = a.predict_random(5)
            print(predict_data)

            from analytics import Research
            p_head, p_tail = Research.Analytics(predict_data).counts()

            print(a.predict_last())

            from config import creat_text, report_name, report_extension
            text = creat_text(data, head, tail, f_head, f_tail, p_head, p_tail)
            a.save_file(text, report_name, report_extension)

        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found")
        except Exception as e:
            print(f"Error: {e}")

