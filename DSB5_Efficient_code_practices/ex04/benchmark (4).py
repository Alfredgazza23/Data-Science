import timeit
import random
from collections import Counter

def main():
    data=[random.randint(0,100) for _ in range(1000000)]
    print("my function:", timeit.timeit(lambda: my_count(data), number=1))
    print("Counter:", timeit.timeit(lambda: counter_count(data), number=1))
    print("my top:", timeit.timeit(lambda: my_top_10(data), number=1))
    print("Counter's top:", timeit.timeit(lambda: counter_top_10(data), number=1))

def my_count(values):
    result = {}
    for number in values:
        if number in result:
            result[number] += 1
        else:
            result[number] = 1
    return result

def my_top_10(values):
    counts = my_count(values)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_counts[:10])

def counter_count(values):
    return dict(Counter(values))

def counter_top_10(values):
    return dict(Counter(values).most_common(10))

if __name__ == '__main__':
    main()
