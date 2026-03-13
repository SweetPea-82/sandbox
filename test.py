import os
import argparse

def myfunc():
    print("hello world")

def parse_arguments():
    parser = argparse.ArgumentParser( 
                                    description='This is the help page. The arguments are below:' 
                                    )

    args = parser.parse_args()

    return args

def main():
    args = parse_arguments()
    myfunc()

if __name__ == "__main__":
    main()