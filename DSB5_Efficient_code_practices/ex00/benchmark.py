import timeit

def main():


    email = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    emails = 5*email

    loop=timeit.timeit(lambda:usual_loop(emails),number=90000000)
    listComp=timeit.timeit(lambda:list_comprehension(emails),number=90000000)

    a='loop'
    b='list comprehension'

    print(f"it is better to use a {b if loop>listComp else a}")
    print(f"{listComp if loop>listComp else loop} vs {loop if loop>listComp else listComp}")


def usual_loop(value):
    result=[]
    for i in value:
        if '@gmail.com' in i:
            result.append(i)
    return result

def list_comprehension(value):
    return [i for i in value if '@gmail.com' in i]

if __name__ == '__main__':
    main()
