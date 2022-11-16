#!/usr/bin/python3

import sys
import helloworld

def main(i):
    hw = helloworld.Helloworld(i)
    print(hw)

if __name__ == '__main__':
    main(sys.argv[1])