#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program


def main():
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process & output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("{0},{1},{2}".format(counter1, counter2, counter3))
    print("Done.")


if __name__ == "__main__":
    main()
