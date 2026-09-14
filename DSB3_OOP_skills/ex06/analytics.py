from random import randint
import logging
import requests

logging.basicConfig(
    filename='analytics.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class Research:

    def __init__(self, file):

        self.file = file
        logging.info(f"Initialized Research with file: {file}")

    def send_report_status(self, token, chat_id, message):

        logging.info("Send a report in telegram")

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"Telegram send error: {e}")

    def file_reader(self, has_header=True):

        logging.info(f"file_reader() started for: {self.file}")

        try:
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

        except Exception as e:
            logging.error(f"file_reader() error: {e}")
            raise

    class Calculations:

        def __init__(self, data):
            self.data = data

        def counts(self):
            logging.info('Сalculating the counts of heads and tails')

            try:
                head = sum(row[0] for row in self.data)
                tail = sum(row[1] for row in self.data)
                return head, tail
            except Exception as e:
                logging.error(f"counts() error: {e}")
                raise


        def fractions(self, head, tail):
            logging.info('Switching to percentages')

            try:
                total = head + tail
                return head / total * 100, tail / total * 100

            except Exception as e:
                logging.error(f"fractions() error: {e}")
                raise

    class Analytics(Calculations):
        def predict_random(self,n):
            logging.info(f'Prediction of {n} random coin tosses')

            try:
                result=[]
                for _ in range(n):
                    x=randint(0,1)
                    result.append([x,int(not(x))])
                return result

            except Exception as e:
                logging.error(f"predict_random() error: {e}")
                raise

        def predict_last(self):
            logging.info('Showing the last line')
            return self.data[len(self.data)-1]

        def save_file(self, data, name, exe):
            logging.info('Saving the file')

            try:
                fileName=f'{name}.{exe}'
                data=str(data)
                with open(fileName,'w',encoding='utf-8') as f:
                    f.write(data)
            except Exception as e:
                logging.error(f"save_file() error: {e}")
                raise
