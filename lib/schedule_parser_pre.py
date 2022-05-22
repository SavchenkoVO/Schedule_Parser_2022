# -*- coding: utf-8 -*-
import os
import re


def read_schedule(path: str, mode: str, enc: str) -> str:
    if mode == 'reading':
        mode = 'r'
        initial_input = open(file=path, mode=mode, encoding=enc).read()
        return initial_input
    else:
        print('===Возможен только режим чтения!===')


def inspect_schedule(text: str) -> bool:
    if re.search('\sEND\s', text) and re.search('\n/\n', text) \
            and re.search('DATES\n\d{2}\s\w{3}\s\d{4}\s/\n', text) \
            and re.search('COMPDAT\n\W*.+\W*\s+\d+\s+\d+\s+\d+\s+\d+\s+(OPEN|SHUT|AUTO).+\n', text) \
            and re.search('COMPDATL\n\W*.+\W*\s+\W*.+\W*\s+\d+\s+\d+\s+\d+\s+\d+\s+(OPEN|SHUT|AUTO).+\n', text) \
            is not None:
        return text
    else:
        print('===Формат файла не соответствует требованиям!===')
        return False


def clean_schedule(text: str) -> str:
    clean_input = re.sub('--.*', '', text)
    clean_input = re.sub('\s{5,}|\n\t|\n{2,}', '\n', clean_input)
    clean_input = re.sub('/\s*', '/\n', clean_input)
    with open("output_data/handled_schedule.inc", "w") as source_file:
        source_file.writelines(clean_input)
    return clean_input


def pre_transform_schedule(path: str, mode: str, enc: str):
    pre_schedule = read_schedule(path, mode, enc)
    pre_schedule = inspect_schedule(pre_schedule)
    pre_schedule = clean_schedule(pre_schedule)
    return pre_schedule

