import sys
import resource

def read_file(path_file):
    with open(path_file,'r') as f:
        for line in f:
            yield line

def main(path_file):
    for _ in read_file(path_file):
        pass

    usage = resource.getrusage(resource.RUSAGE_SELF)
    print(f"Peak Memory Usage = {usage.ru_maxrss / (1024**2):.3f} GB")
    print(f"User Mode Time + System Mode Time = {usage.ru_utime + usage.ru_stime:.2f}s")


if __name__ == '__main__':
    try:
        if len(sys.argv)!=2:
            raise ValueError("Usage: python3 generator.py <path_file>")

        path_file=sys.argv[1]
        main(path_file)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Unexpected error:", e)
