import timeit

def main():


    email = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    emails = 5*email

    loop=timeit.timeit(lambda:usual_loop(emails),number=90000000)
    listComp=timeit.timeit(lambda:list_comprehension(emails),number=90000000)
    mapGen=timeit.timeit(lambda:map_generator(emails),number=90000000)

    methods = [(loop, 'loop'), (listComp,'list comprehension'), (mapGen,'map')]
    sorted_value=sorted(methods)

    print(f"it is better to use a {sorted_value[0][1]}")
    print(f"{sorted_value[0][0]} vs {sorted_value[1][0]} vs {sorted_value[2][0]}")

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

if __name__ == '__main__':
    main()
