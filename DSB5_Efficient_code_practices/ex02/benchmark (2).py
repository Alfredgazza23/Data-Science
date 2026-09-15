import timeit
import sys

def main(method,number_of_calls):


    email = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    emails = 5*email

    if method=='loop':
        return timeit.timeit(lambda:usual_loop(emails),number=number_of_calls)
    elif method=='list_comprehension':
        return timeit.timeit(lambda:list_comprehension(emails),number=number_of_calls)
    elif method=='map':
        return timeit.timeit(lambda:map_generator(emails),number=number_of_calls)
    elif method=='filter':
        return timeit.timeit(lambda:filter_generator(emails),number=number_of_calls)
    else:
        raise ValueError("Error: <method> must be one of [loop, list_comprehension, map, filter]")


def usual_loop(value):
    result=[]
    for i in value:
        if '@gmail.com' in i:
            result.append(i)
    return result

def list_comprehension(value):
    return [i for i in value if '@gmail.com' in i]

def map_generator(value):
    return list(map(lambda x: x if '@gmail.com' in x else None, value))

def filter_generator(value):
    return list(filter(lambda x: '@gmail.com' in x , value))

if __name__ == '__main__':
    try:
        if len(sys.argv)!=3:
            raise ValueError("Usage: ./benchmark.py <method> <number_of_calls>")

        method=sys.argv[1]
        number_of_calls=int(sys.argv[2])

        if number_of_calls <= 0:
            raise ValueError("Error: <number_of_calls> must be a positive integer")

        print(main(method,number_of_calls))
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Unexpected error:", e)
