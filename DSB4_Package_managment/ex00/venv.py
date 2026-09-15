#!/usr/bin/env python3
import os

def main():
    print(f"Your current virtual env is {os.getenv('VIRTUAL_ENV')}")

if __name__ == "__main__":
    main()
