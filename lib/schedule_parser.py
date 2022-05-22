# -*- coding: utf-8 -*-
import re
import numpy as np
from typing import Tuple, List


def parse_schedule(text: str, keywords_tuple: Tuple[str]) -> List[List[str]]:
    elements_list = []
    current_date = None
    last_is_date = False
    keyword_blocks = extract_keyword_blocks(text, keywords_tuple)
    for (i, block) in enumerate(keyword_blocks):
        keyword, lines = extract_lines_from_keyword_block(block)
        lines = lines[0].strip().split('\n')

        if keyword == 'DATES':
            if (current_date is not None) and last_is_date:
                element = [np.nan] * 14
                element[0] = current_date
                elements_list.append(element)

            dates = []
            for line in lines:
                date = parse_keyword_DATE_line(line)
                dates.append(date)

            dates.reverse()
            while len(dates) > 1:
                element = [np.nan] * 14
                element[0] = dates.pop()
                elements_list.append(element)

            current_date = dates.pop()
            last_is_date = True

        if keyword == 'COMPDAT':
            last_is_date = False
            if current_date is None:
                current_date_ = np.nan
            else:
                current_date_ = current_date
            for line in lines:
                compdat = parse_keyword_COMPDAT_line(line)
                element = [np.nan] * 14
                element[0] = current_date_
                for i in range(1, len(element)):
                    element[i] = compdat[i - 1]
                elements_list.append(element)

        if keyword == 'COMPDATL':
            last_is_date = False
            if current_date is None:
                current_date_ = np.nan
            else:
                current_date_ = current_date
            for line in lines:
                compdatl = parse_keyword_COMPDATL_line(line)
                element = [np.nan] * 14
                element[0] = current_date_
                for i in range(1, len(element)):
                    element[i] = compdatl[i - 1]
                elements_list.append(element)

    if (current_date is not None) and last_is_date:
        element = [np.nan] * 14
        element[0] = current_date
        elements_list.append(element)
    print(elements_list)
    return elements_list


def extract_keyword_blocks(text: str, keywords_tuple: Tuple[str]) -> List[Tuple[str]]:
    keyword_indexes, slash_indexes, blocks_list = [], [], []
    keyword_match_counts = 0

    # Поиск индексов ключевых слов, открывающих блок
    for i in range(len(keywords_tuple)):
        for keyword_match in re.finditer('%s\n' % keywords_tuple[i], text):
            keyword_indexes.append(keyword_match.start())
            keyword_match_counts += 1
    keyword_indexes.sort()
    # Поиск индексов слэшей, закрывающих блок
    slash_index = 0
    for slash_match in re.finditer('\n/\n', text):
        if 'WEFAC' not in text[slash_index:slash_match.end()]:
            slash_indexes.append(slash_match.end())
        slash_index = slash_match.end()

    # Поиск блоков по найденным индексам
    for block_match in range(keyword_match_counts):
        block = text[keyword_indexes[block_match]:slash_indexes[block_match]]
        block = (block,)
        blocks_list.append(block)
    return blocks_list


def extract_lines_from_keyword_block(block: Tuple[str]) -> Tuple[str, List[str]]:
    keyword_match = re.search(r'DATES|COMPDATL|COMPDAT', block[0])
    line = (block[0][keyword_match.start():keyword_match.end()], [block[0][keyword_match.end():-2]])
    return line


def parse_keyword_DATE_line(current_date_line: str) -> str:
    current_date_line = ''.join(current_date_line)
    current_date_line = re.sub('\s/', '', current_date_line)
    return current_date_line.strip()


def parse_keyword_COMPDAT_line(well_comp_line: str) -> List[str]:
    well_comp_line = re.sub('\s/', '', well_comp_line)
    well_comp_line = well_comp_line.split()
    well_comp_line.insert(1, np.nan)
    return well_comp_line


def parse_keyword_COMPDATL_line(well_comp_line: str) -> List[str]:
    well_comp_line = re.sub('\s/', '', well_comp_line)
    return well_comp_line.strip().split()


