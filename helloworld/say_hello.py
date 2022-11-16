#!/usr/bin/python3

import sys
import helloworld

def main(i):
    hw = helloworld.Helloworld(i)
    print(f'oh noes! {hw}')


if __name__ == '__main__':
    main(sys.argv[1])