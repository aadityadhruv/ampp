import os
import argparse 
def ampp_main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-a', '--action', help='repo help', required=True)
    args = parser.parse_args()



ampp_main()
