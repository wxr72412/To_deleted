#!/usr/bin/env python3

import sys
from typing import List
from time import sleep

DEBUG = False


def load_lines(src_file_name: str) -> List[str]:
    with open(src_file_name, 'r') as f:
        lines = f.readlines()

    return lines


def get_first_letter(lines: List[str]) -> List[str]:
    first_letter_list = []

    for one_line in lines:
        first_letter = one_line[0]
        first_letter_list.append(first_letter)
        sleep(0.01)

    return first_letter_list


def save_to_file(dest_file_name: str, first_letter_list: List[str]):
    first_letter_list = [x.strip()
                         for x in first_letter_list if len(x.strip()) > 0]

    with open(dest_file_name, 'w') as f:
        buffer = '\n'.join(first_letter_list)
        f.write(buffer)


def main():

    src_file_name = ""
    dest_file_name = ""

    if DEBUG:
        src_file_name = 'index.html'
        dest_file_name = 'index.html_out.txt'
    else:
        src_file_name = sys.argv[1]
        dest_file_name = sys.argv[2]

    lines = load_lines(src_file_name)
    first_letter_list = get_first_letter(lines)
    save_to_file(dest_file_name, first_letter_list)


if __name__ == '__main__':
    main()
