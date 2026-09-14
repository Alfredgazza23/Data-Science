import sys

def main():

    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']

    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if len(sys.argv) != 2:
        raise Exception("Unknown task name. Use: call_center, potential_clients, or loyalty_program")

    menu_list=sys.argv[1]

    result=[]

    if menu_list=='call_center':
        result=not_include(clients,recipients)
    elif menu_list=='potential_clients':
        result=not_include(participants,clients)
    elif menu_list=='loyalty_program':
        result=not_include(clients,participants)
    else:
        raise Exception("Unknown task name. Use: call_center, potential_clients, or loyalty_program")

    for email in result:
        print(email)

def not_include(value_list: list, check_list: list) -> list:
    return list(set(value_list) - set(check_list))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
