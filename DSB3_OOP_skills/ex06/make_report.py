import sys
from analytics import Research
import config


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file>")
    else:
        try:
            d = Research(sys.argv[1])

            data=d.file_reader()
            print(data)

            a=d.Analytics(data)

            head, tail = a.counts()
            print(head, tail)

            f_head, f_tail = a.fractions(head, tail)
            print(f_head, f_tail)

            predict_data=a.predict_random(config.num_of_steps)
            print(predict_data)
            p_head, p_tail=d.Analytics(predict_data).counts()

            print(a.predict_last())

            text=config.creat_text(data,head,tail,f_head,f_tail,p_head,p_tail)
            a.save_file(text, config.report_name, config.report_extension)

            d.send_report_status(config.token,config.chat_id,config.success_message)

        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found")
            Research('').send_report_status(config.token,config.chat_id,config.error_message)
        except Exception as e:
            print(f"Error: {e}")
            Research('').send_report_status(config.token,config.chat_id,config.error_message)


