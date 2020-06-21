import os
import getopt
import sys
import time
import logging

logging.basicConfig(level=logging.DEBUG)

def usage():
    print('Usage:')
    print(sys.argv[0] + '--name=the_name')


def main(sleep):
    counter = 1
    while True:
        logging.info('[{}] one line and sleep {}s'.format(counter, sleep))
        time.sleep(int(sleep))
        counter+=1


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:", [
            "help",
            "sleep=",
        ])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    sleep = 5
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--sleep"):
            sleep = a
        else:
            assert False, "unhandled option"

    main(sleep)
