import timeit
import sys
from functools import reduce

def main(method,number_of_calls,number_of_take):

    if method=='loop':
        return timeit.timeit(lambda:usual_loop(number_of_take),number=number_of_calls)
    elif method=='reduce':
        return timeit.timeit(lambda:func_reduce(number_of_take),number=number_of_calls)
    else:
        raise ValueError("Error: <method> must be one of [loop, reduce]")


def usual_loop(value):
    sum=0
    for i in range(1,value+1):
        sum=sum+i*i
    return sum

def func_reduce(value):
    return reduce(lambda acc,x:acc+x*x, range(value+1))


if __name__ == '__main__':
    try:
        if len(sys.argv)!=4:
            raise ValueError("Usage: ./benchmark.py <method> <number_of_calls> <number_of_take>")

        method=sys.argv[1]
        number_of_calls=int(sys.argv[2])
        number_of_take=int(sys.argv[3])


        if number_of_calls <= 0:
            raise ValueError("Error: <number_of_calls> must be a positive integer")
        if number_of_take <= 0:
            raise ValueError("Error: <number_of_take> must be a positive integer")

        print(main(method,number_of_calls,number_of_take))
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Unexpected error:", e)
